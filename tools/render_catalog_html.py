"""Render docs/matrix-action-outcome-matrix.md to a styled, navigable HTML page.

Content is copied verbatim from the markdown -- no data is altered. Only presentation
(sidebar nav, collapsible entries, styled tables) is added.
"""
import io
import re
import html as _html

SRC = "docs/matrix-action-outcome-matrix.md"
OUT = "docs/matrix-action-outcome-matrix.html"

with io.open(SRC, "r", encoding="utf-8") as f:
    md = f.read()

lines = md.split("\n")


def slugify(text):
    t = re.sub(r"<[^>]+>", "", text)
    t = t.replace("&mdash;", "-").replace("&amp;", "and")
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t


def inline(text):
    """Convert inline markdown (code, bold, links) to HTML. Text may already
    contain intentional HTML entities (&mdash; etc.) and <a id> anchors."""
    # protect existing anchor tags
    anchors = []

    def _stash(m):
        anchors.append(m.group(0))
        return "\x00A%d\x00" % (len(anchors) - 1)

    text = re.sub(r"<a id=\"[^\"]+\"></a>", _stash, text)

    # escape everything else, but keep &entity; intact
    # temporarily protect entities
    ents = []

    def _stashent(m):
        ents.append(m.group(0))
        return "\x00E%d\x00" % (len(ents) - 1)

    text = re.sub(r"&[a-zA-Z]+;|&#\d+;", _stashent, text)
    text = _html.escape(text, quote=False)

    # inline code first (protect its contents)
    codes = []

    def _stashcode(m):
        codes.append(m.group(1))
        return "\x00C%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", _stashcode, text)

    # links [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), text)
    # bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)

    # restore code (contents were captured AFTER escaping, so do not re-escape)
    def _unstashcode(m):
        return "<code>%s</code>" % codes[int(m.group(1))]
    text = re.sub(r"\x00C(\d+)\x00", _unstashcode, text)
    # restore entities
    text = re.sub(r"\x00E(\d+)\x00", lambda m: ents[int(m.group(1))], text)
    # restore anchors
    text = re.sub(r"\x00A(\d+)\x00", lambda m: anchors[int(m.group(1))], text)
    return text


out = []          # html body chunks
toc = []          # (level, id, title) for sidebar
open_details = 0  # nesting count of open <details> for entry sections

i = 0
n = len(lines)


def close_details():
    global open_details
    while open_details > 0:
        out.append("</div></details>")
        open_details -= 1


while i < n:
    line = lines[i]
    stripped = line.strip()

    # --- fenced code block --------------------------------------------------
    if stripped.startswith("```"):
        lang = stripped[3:].strip()
        buf = []
        i += 1
        while i < n and not lines[i].strip().startswith("```"):
            buf.append(lines[i])
            i += 1
        i += 1  # skip closing fence
        code = _html.escape("\n".join(buf), quote=False)
        cls = " class=\"lang-%s\"" % lang if lang else ""
        out.append("<pre><code%s>%s</code></pre>" % (cls, code))
        continue

    # --- standalone anchor line --------------------------------------------
    if re.match(r"^<a id=\"[^\"]+\"></a>\s*$", stripped):
        out.append(stripped)
        i += 1
        continue

    # --- headings -----------------------------------------------------------
    m = re.match(r"^(#{1,6})\s+(.*)$", line)
    if m:
        level = len(m.group(1))
        title = m.group(2).strip()
        hid = slugify(title)
        html_title = inline(title)

        if level == 1:
            close_details()
            out.append('<h1 id="%s">%s</h1>' % (hid, html_title))
        elif level == 2:
            close_details()
            toc.append((2, hid, title))
            out.append('<h2 id="%s">%s</h2>' % (hid, html_title))
        elif level == 3:
            # entry-level: collapsible
            close_details()
            toc.append((3, hid, title))
            out.append('<details class="entry" open id="%s"><summary>%s</summary><div class="entry-body">' % (hid, html_title))
            open_details = 1
        else:  # level >= 4
            out.append('<h%d id="%s" class="sub">%s</h%d>' % (level, hid, html_title, level))
        i += 1
        continue

    # --- horizontal rule ----------------------------------------------------
    if stripped == "---":
        out.append("<hr>")
        i += 1
        continue

    # --- table --------------------------------------------------------------
    if stripped.startswith("|") and i + 1 < n and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
        header = [c.strip() for c in stripped.strip("|").split("|")]
        i += 2  # skip header + separator
        rows = []
        while i < n and lines[i].strip().startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            rows.append(cells)
            i += 1
        thtml = ["<div class=\"table-wrap\"><table>", "<thead><tr>"]
        for h in header:
            thtml.append("<th>%s</th>" % inline(h))
        thtml.append("</tr></thead><tbody>")
        for r in rows:
            thtml.append("<tr>")
            for c in r:
                thtml.append("<td>%s</td>" % inline(c))
            thtml.append("</tr>")
        thtml.append("</tbody></table></div>")
        out.append("".join(thtml))
        continue

    # --- blockquote ---------------------------------------------------------
    if stripped.startswith(">"):
        buf = []
        while i < n and lines[i].strip().startswith(">"):
            buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
            i += 1
        out.append("<blockquote>%s</blockquote>" % inline(" ".join(b.strip() for b in buf)))
        continue

    # --- lists (ordered + unordered) ---------------------------------------
    if re.match(r"^\s*([-*]|\d+\.)\s+", line):
        items = []
        ordered = bool(re.match(r"^\s*\d+\.\s+", line))
        while i < n and re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]):
            content = re.sub(r"^\s*([-*]|\d+\.)\s+", "", lines[i])
            # gather wrapped continuation lines (indented, not a new item/blank)
            i += 1
            while i < n and lines[i].strip() and not re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]) \
                    and not lines[i].startswith("#") and not lines[i].strip().startswith("|") \
                    and lines[i].startswith(("  ", "\t")):
                content += " " + lines[i].strip()
                i += 1
            items.append(content)
        tag = "ol" if ordered else "ul"
        out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % inline(it) for it in items), tag))
        continue

    # --- blank line ---------------------------------------------------------
    if stripped == "":
        i += 1
        continue

    # --- paragraph (gather wrapped lines) ----------------------------------
    buf = [line]
    i += 1
    while i < n and lines[i].strip() and not re.match(r"^(#{1,6})\s", lines[i]) \
            and not lines[i].strip().startswith(("|", ">", "```", "-", "*")) \
            and not re.match(r"^\s*\d+\.\s", lines[i]) and lines[i].strip() != "---" \
            and not re.match(r"^<a id=", lines[i].strip()):
        buf.append(lines[i])
        i += 1
    out.append("<p>%s</p>" % inline(" ".join(b.strip() for b in buf)))

close_details()

# --- sidebar TOC ------------------------------------------------------------
nav = ['<nav id="toc"><div class="toc-inner">', '<div class="toc-title">Catalog</div>']
for level, hid, title in toc:
    cls = "toc-l2" if level == 2 else "toc-l3"
    label = re.sub(r"<[^>]+>", "", inline(title))
    nav.append('<a class="%s" href="#%s">%s</a>' % (cls, hid, label))
nav.append("</div></nav>")

CSS = """
:root{
  --bg:#0d1117; --panel:#161b22; --panel2:#1c2230; --border:#30363d;
  --fg:#c9d1d9; --dim:#8b949e; --accent:#58a6ff; --accent2:#3fb950;
  --amber:#d29922; --red:#f85149; --code:#79c0ff;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--fg);
  font:15px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
}
a{color:var(--accent); text-decoration:none}
a:hover{text-decoration:underline}
.layout{display:flex; align-items:flex-start}
#toc{
  position:sticky; top:0; height:100vh; flex:0 0 300px;
  background:var(--panel); border-right:1px solid var(--border);
  overflow-y:auto; padding:0;
}
.toc-inner{padding:18px 14px}
.toc-title{
  font-weight:700; font-size:13px; letter-spacing:.08em; text-transform:uppercase;
  color:var(--dim); margin:0 0 10px 6px;
}
#toc a{display:block; color:var(--dim); padding:3px 8px; border-radius:6px; font-size:13px}
#toc a:hover{background:var(--panel2); color:var(--fg); text-decoration:none}
#toc a.toc-l2{margin-top:12px; font-weight:700; color:var(--fg); font-size:13.5px}
#toc a.toc-l3{margin-left:10px; border-left:1px solid var(--border)}
main{flex:1 1 auto; max-width:1200px; padding:34px 46px 120px; min-width:0}
h1{font-size:30px; margin:.2em 0 .5em; padding-bottom:.3em; border-bottom:2px solid var(--border)}
h2{
  font-size:23px; margin:2.2em 0 .7em; padding:10px 16px;
  background:linear-gradient(90deg,var(--panel2),transparent);
  border-left:4px solid var(--accent); border-radius:6px;
}
h4.sub,h5.sub,h6.sub{font-size:15px; color:var(--amber); margin:1.4em 0 .4em}
p{margin:.7em 0}
code{
  background:var(--panel2); color:var(--code); padding:.12em .4em;
  border-radius:5px; font-size:.88em; font-family:"Cascadia Code",Consolas,monospace;
}
pre{
  background:#0a0e14; border:1px solid var(--border); border-radius:8px;
  padding:14px 16px; overflow-x:auto; margin:1em 0;
}
pre code{background:none; color:#cdd9e5; padding:0; font-size:12.5px; line-height:1.5}
blockquote{
  margin:1em 0; padding:10px 16px; border-left:4px solid var(--amber);
  background:var(--panel); border-radius:0 6px 6px 0; color:var(--dim);
}
hr{border:none; border-top:1px solid var(--border); margin:1.6em 0}
ul,ol{margin:.6em 0; padding-left:1.4em}
li{margin:.25em 0}
.table-wrap{overflow-x:auto; margin:1em 0; border:1px solid var(--border); border-radius:8px}
table{border-collapse:collapse; width:100%; font-size:13px}
thead th{
  background:var(--panel2); color:var(--fg); text-align:left; font-weight:700;
  padding:9px 12px; border-bottom:2px solid var(--border); position:sticky; top:0;
  vertical-align:top;
}
tbody td{padding:9px 12px; border-top:1px solid var(--border); vertical-align:top}
tbody tr:nth-child(even){background:rgba(255,255,255,.02)}
tbody tr:hover{background:rgba(88,166,255,.06)}
details.entry{
  margin:16px 0; border:1px solid var(--border); border-radius:10px;
  background:var(--panel); overflow:hidden;
}
details.entry>summary{
  cursor:pointer; padding:12px 18px; font-weight:600; font-size:15.5px;
  list-style:none; background:var(--panel2); user-select:none;
}
details.entry>summary::-webkit-details-marker{display:none}
details.entry>summary::before{content:"\\25B8"; color:var(--accent); margin-right:10px; font-size:12px}
details.entry[open]>summary::before{content:"\\25BE"}
details.entry>summary:hover{color:#fff}
details.entry>summary code{background:#0a0e14}
.entry-body{padding:6px 18px 16px}
.controls{
  position:sticky; top:0; z-index:5; display:flex; gap:10px; align-items:center;
  padding:12px 0; margin-bottom:6px; background:var(--bg);
}
.controls button{
  background:var(--panel2); color:var(--fg); border:1px solid var(--border);
  border-radius:6px; padding:6px 14px; cursor:pointer; font-size:13px;
}
.controls button:hover{border-color:var(--accent); color:#fff}
.controls input{
  flex:1; max-width:340px; background:var(--panel2); color:var(--fg);
  border:1px solid var(--border); border-radius:6px; padding:6px 12px; font-size:13px;
}
@media (max-width:900px){
  #toc{display:none}
  main{padding:20px}
}
"""

JS = """
const q=document.getElementById('filter');
const entries=[...document.querySelectorAll('details.entry')];
q.addEventListener('input',()=>{
  const t=q.value.toLowerCase();
  entries.forEach(e=>{
    const hit=!t||e.textContent.toLowerCase().includes(t);
    e.style.display=hit?'':'none';
    if(t&&hit)e.open=true;
  });
});
document.getElementById('expand').onclick=()=>entries.forEach(e=>e.open=true);
document.getElementById('collapse').onclick=()=>entries.forEach(e=>e.open=false);
"""

controls = (
    '<div class="controls">'
    '<button id="expand">Expand all</button>'
    '<button id="collapse">Collapse all</button>'
    '<input id="filter" type="search" placeholder="Filter entries (e.g. A3, black_hammer, tie)...">'
    "</div>"
)

doc = (
    "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
    "<title>Matrix-Run Action-Outcome Catalog</title>"
    "<style>%s</style></head><body><div class=\"layout\">%s<main>%s%s</main></div>"
    "<script>%s</script></body></html>"
) % (CSS, "\n".join(nav), controls, "\n".join(out), JS)

with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(doc)

print("wrote", OUT, "-", len(doc), "bytes,", len(toc), "toc entries")
