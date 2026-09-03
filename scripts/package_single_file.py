#!/usr/bin/env python3
"""Embed local article images into a versioned self-contained HTML preview."""
import argparse,base64,mimetypes,re
from pathlib import Path

IMG=re.compile(r'(<img\b[^>]*?\bsrc=["\'])([^"\']+)(["\'][^>]*>)',re.I)

def package(src:Path,out:Path):
    text=src.read_text(encoding="utf-8"); count=0
    def repl(m):
        nonlocal count
        url=m.group(2)
        if url.startswith(("data:","http://","https://")): return m.group(0)
        path=(src.parent/url).resolve()
        if not path.is_file(): raise FileNotFoundError(f"Missing image: {url}")
        mime=mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        data=base64.b64encode(path.read_bytes()).decode("ascii");count+=1
        return m.group(1)+f"data:{mime};base64,{data}"+m.group(3)
    text=IMG.sub(repl,text)
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(text,encoding="utf-8")
    print(f"Packaged {count} local image(s): {out}")

if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--input",required=True,type=Path);ap.add_argument("--output",required=True,type=Path);a=ap.parse_args()
    if a.input.resolve()==a.output.resolve(): raise SystemExit("Output must use a new versioned filename")
    package(a.input,a.output)
