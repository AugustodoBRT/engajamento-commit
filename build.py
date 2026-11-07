#!/usr/bin/env python3
"""Junta membros.json + posts/*.json em data.js (o dashboard abre por file://)."""
import json, glob, pathlib
d = pathlib.Path(__file__).parent
membros = json.loads((d/"membros.json").read_text())
posts = [json.loads(open(f).read()) for f in sorted(glob.glob(str(d/"posts"/"*.json")))]
(d/"data.js").write_text("window.DATA = " + json.dumps({"membros": membros, "posts": posts}, ensure_ascii=False) + ";\n")
print(f"{len(membros)} membros, {len(posts)} posts -> data.js")
