"""Server-side generation of the filled SR2 character-sheet PDF.

The AcroForm field mapping lives in ``tools/fill_sr2_sheet.py`` (the single source, also used by the
standalone CLI). ``pypdf`` and the template PDF (``docs/SR2_Official_Sheet_Fillable.pdf``) ship in the
image -- see ``.dockerignore``. The tool module is imported lazily so a missing pypdf/template
degrades to a 503 at the endpoint rather than crashing app startup.
"""
from __future__ import annotations

import io


def render_character_sheet(char: dict, contacts: list[tuple]) -> bytes:
    """Return the filled SR2 character sheet as PDF bytes.

    ``char`` = the character's columns as a dict (JSON columns already deserialized by the ORM);
    ``contacts`` = ``(name, profession, contact_type)`` tuples. Raises ``ImportError`` when pypdf is
    unavailable (caught by the endpoint -> 503).
    """
    from tools.fill_sr2_sheet import build_fields, fill_pdf  # lazy: pypdf/template optional at import

    fields = build_fields(char, contacts)
    buf = io.BytesIO()
    fill_pdf(fields, buf)
    return buf.getvalue()
