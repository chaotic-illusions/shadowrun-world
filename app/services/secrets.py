"""
Secret retrieval utilities.

Resolution order:
  1. Windows Credential Manager (via keyring) -- for local development
  2. Environment variable -- for Docker / CI / production
"""
import os


def get_api_key() -> str | None:
    """Return the Anthropic API key, or None if not configured."""
    try:
        import keyring
        key = keyring.get_password("shadowrun-world", "ANTHROPIC_API_KEY")
        if key and key.strip():
            return key.strip()
    except Exception:
        pass
    return os.environ.get("ANTHROPIC_API_KEY", "").strip() or None
