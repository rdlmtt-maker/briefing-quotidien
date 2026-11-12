"""Construit un fichier HTML autonome (toutes les éditions incluses), lisible hors ligne."""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent / "public"
data = {"editions/index.json": json.loads((root / "editions/index.json").read_text())}
for e in data["editions/index.json"]:
    f = root / "editions" / f"{e['date']}.json"
    if f.exists():
        data[f"editions/{e['date']}.json"] = json.loads(f.read_text())
html = (root / "index.html").read_text()
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = html.replace("<script src=\"https://cdnjs", f"<script>window.__SH_DATA={blob};</script>\n<script src=\"https://cdnjs", 1)
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "six-heures.html")
out.write_text(html)
print(out, len(html))
