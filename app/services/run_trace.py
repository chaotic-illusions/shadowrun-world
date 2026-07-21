"""
Per-action engine computation trace (developer / GM observability).

Opt-in via the ``SR_TRACE`` environment flag. When the flag is OFF (the default -- normal
play and the whole test suite), :func:`trace` is a cheap no-op and nothing is written, so
there is no behavior change and no measurable overhead. When the flag is ON, the matrix-run
engine primitives (``matrix_engine``) append human-readable computation steps to a
per-request buffer held in a ``ContextVar``; the matrix-run action endpoints wrap themselves
with the :func:`trace_action`-style dependency, which flushes each action's collected steps to
``data/traces/run_<id>.log``.

The buffer lives in a ``ContextVar`` so concurrent requests never cross-contaminate: each
request that calls :func:`start` gets its own list, and :func:`trace` only appends when a
buffer has been started for the current context.
"""
from __future__ import annotations

import os
from contextvars import ContextVar
from datetime import datetime, UTC
from pathlib import Path

# The active per-request trace buffer, or None when tracing is not running for this context.
_buffer: ContextVar[list[str] | None] = ContextVar("matrix_trace_buffer", default=None)

_TRACE_DIR = Path("data/traces")


def is_enabled() -> bool:
    """True when engine tracing is switched on via the ``SR_TRACE`` env flag.

    Read live (not cached) so the flag can be flipped by relaunching the process without any
    code change. Cheap enough to call per request.
    """
    return os.getenv("SR_TRACE", "").strip().lower() in ("1", "true", "yes", "on")


def start() -> None:
    """Begin a fresh trace buffer for the current request context. No-op when disabled."""
    if is_enabled():
        _buffer.set([])


def trace(message: str) -> None:
    """Append one computation step to the active buffer.

    No-op when tracing is off or when no buffer was started for this context (e.g. the test
    suite and any non-request caller of the engine), so it is safe to sprinkle freely.
    """
    buf = _buffer.get()
    if buf is not None:
        buf.append(message)


def collect() -> list[str]:
    """Return the current buffer's lines and clear it (so the next action starts clean)."""
    buf = _buffer.get()
    _buffer.set(None)
    return list(buf) if buf else []


def flush_run(run_id: int, header: str, lines: list[str]) -> None:
    """Append one action's trace block to ``data/traces/run_<id>.log``.

    Best-effort and defensive: observability must never break gameplay, so any filesystem
    error is swallowed. No-op when there is nothing to write.
    """
    if not lines:
        return
    try:
        _TRACE_DIR.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
        block = [f"===== {stamp} | {header} ====="]
        block.extend(f"  {ln}" for ln in lines)
        block.append("")
        with (_TRACE_DIR / f"run_{run_id}.log").open("a", encoding="utf-8") as fh:
            fh.write("\n".join(block) + "\n")
    except Exception:
        pass
