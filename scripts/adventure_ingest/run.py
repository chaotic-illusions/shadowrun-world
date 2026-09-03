"""Load one adventure spec into the API and/or render its prep doc.

    python scripts/adventure_ingest/run.py silver_angel --doc          # write docs/adventure-prep/*.md only
    python scripts/adventure_ingest/run.py silver_angel --dry          # show what would be pushed
    SR_ADMIN_TOKEN=... python scripts/adventure_ingest/run.py silver_angel --base https://sr.crymson.org

Token comes from --token or the SR_ADMIN_TOKEN env var. Re-running is idempotent (see loader.py).
"""
import argparse
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from loader import Api, Loader, render_doc  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", help="module name under specs/, e.g. silver_angel")
    ap.add_argument("--base", default=os.environ.get("SR_API_BASE", "https://sr.crymson.org"))
    ap.add_argument("--token", default=os.environ.get("SR_ADMIN_TOKEN"))
    ap.add_argument("--dry", action="store_true", help="resolve and print, but do not write")
    ap.add_argument("--doc", action="store_true", help="only render docs/adventure-prep/<NN>-<slug>.md")
    args = ap.parse_args()

    spec = importlib.import_module(f"specs.{args.spec}")
    spec.SLUG = args.spec

    doc_path = os.path.join(ROOT, "docs", "adventure-prep", f"{int(getattr(spec, 'ORDER', 0)):02d}-{args.spec.replace('_', '-')}.md")
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)
    with open(doc_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_doc(spec))
    print(f"wrote {os.path.relpath(doc_path, ROOT)}")
    if args.doc:
        return

    if not args.token:
        sys.exit("no admin token: pass --token or set SR_ADMIN_TOKEN")
    report = Loader(Api(args.base, args.token), spec, dry=args.dry).run()
    print(json.dumps(report, indent=1))
    if report["warnings"]:
        sys.exit(2)


if __name__ == "__main__":
    main()
