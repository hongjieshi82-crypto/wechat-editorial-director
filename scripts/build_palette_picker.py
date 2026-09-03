#!/usr/bin/env python3
"""Build a live picker for three palettes after an art direction is chosen."""
import argparse, html, json
from pathlib import Path

ROLES={"canvas","surface","ink","body","muted","border","accent","accent_soft","highlight","dark_stage","dark_text"}
FIELDS={"id","name","rationale","roles","tradeoff"}
def e(v): return html.escape(str(v))

def load(path):
    d=json.loads(path.read_text(encoding="utf-8")); ps=d.get("proposals",[])
    if len(ps)!=3: raise ValueError("Exactly three palette proposals are required")
    ids=set()
    for p in ps:
        missing=FIELDS-set(p)
        if missing: raise ValueError("Missing proposal fields: "+", ".join(sorted(missing)))
        missing_roles=ROLES-set(p["roles"])
        if missing_roles: raise ValueError("Missing color roles: "+", ".join(sorted(missing_roles)))
        if p["id"] in ids: raise ValueError("Palette ids must be unique")
        ids.add(p["id"])
    return d

def build(d):
    title=e(d.get("article_title","公众号文章")); direction=e(d.get("direction","已选编辑方向"))
    cards=[]
    for p in d["proposals"]:
        r=p["roles"]; swatches="".join(f'<i title="{e(k)}" style="background:{e(r[k])}"></i>' for k in ["dark_stage","ink","accent","accent_soft","highlight","canvas"])
        cards.append(f'''<article data-id="{e(p['id'])}" onclick="pick('{e(p['id'])}')"><div class="swatches">{swatches}</div><small>COLOR SYSTEM</small><h2>{e(p['name'])}</h2><p>{e(p['rationale'])}</p><div class="sample" style="background:{e(r['canvas'])};border-color:{e(r['border'])}"><div class="stage" style="background:{e(r['dark_stage'])};color:{e(r['dark_text'])}"><b>视觉舞台</b><em style="color:{e(r['accent'])}">交互信号</em></div><h3 style="color:{e(r['ink'])}">章节标题 <u style="background:{e(r['highlight'])}">重点</u></h3><p style="color:{e(r['body'])}">正文由中性色承担，主色只负责导航和交互。</p><blockquote style="background:{e(r['accent_soft'])};color:{e(r['ink'])};border-color:{e(r['accent'])}">这是提示框的实际效果。</blockquote></div><p class="trade"><b>取舍：</b>{e(p['tradeoff'])}</p><button>选择这套配色</button></article>''')
    payload=json.dumps(d,ensure_ascii=False).replace("</","<\\/")
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · 配色选择</title><style>*{{box-sizing:border-box}}body{{margin:0;background:#f3f4f6;color:#111827;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif}}main{{max-width:1120px;margin:auto;padding:36px 20px 60px}}header{{text-align:center;margin-bottom:26px}}header small,article>small{{letter-spacing:2px;color:#9ca3af;font-weight:800;font-size:10px}}h1{{font-size:28px;margin:8px}}header p{{color:#6b7280;font-size:13px}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}article{{padding:22px;background:white;border:2px solid transparent;border-radius:18px;box-shadow:0 7px 24px #0f172a12;cursor:pointer}}article.selected{{border-color:#111827}}.swatches{{display:flex;margin-bottom:16px}}.swatches i{{width:30px;height:30px;border-radius:50%;margin-right:-5px;border:2px solid white;box-shadow:0 0 0 1px #ddd}}h2{{font-size:20px;margin:8px 0}}article>p{{font-size:12px;line-height:1.7;color:#6b7280}}.sample{{margin:16px 0;padding:12px;border:1px solid;border-radius:12px}}.stage{{padding:14px;border-radius:8px}}.stage b,.stage em{{display:block;font-style:normal;font-size:12px}}.sample h3{{font-size:15px}}.sample h3 u{{text-decoration:none;padding:0 3px}}.sample p{{font-size:11px;line-height:1.7}}.sample blockquote{{margin:10px 0 0;padding:10px;border-left:3px solid;font-size:11px}}.trade{{min-height:58px}}button{{width:100%;border:0;border-radius:9px;background:#111827;color:white;padding:11px;font-weight:800}}#result{{display:none;margin:24px auto 0;max-width:700px;padding:17px;border-radius:12px;background:#111827;color:white;text-align:center}}#result button{{width:auto;background:white;color:#111827}}@media(max-width:820px){{.grid{{grid-template-columns:1fr}}}}</style></head><body><main><header><small>PALETTE DIRECTION</small><h1>{title}</h1><p>已选编辑方向：{direction}。现在只选色彩系统，不改变文章结构。</p></header><section class="grid">{''.join(cards)}</section><section id="result"><strong id="chosen"></strong><p>选定后才进入完整排版与配图。</p><button onclick="copyChoice(event)">复制配色选择</button></section></main><script id="data" type="application/json">{payload}</script><script>const D=JSON.parse(document.getElementById('data').textContent);let selected='';function pick(id){{selected=id;document.querySelectorAll('article').forEach(x=>x.classList.toggle('selected',x.dataset.id===id));const p=D.proposals.find(x=>x.id===id);document.getElementById('chosen').textContent='已选：'+p.name;document.getElementById('result').style.display='block';document.getElementById('result').scrollIntoView({{behavior:'smooth'}})}}function copyChoice(ev){{const p=D.proposals.find(x=>x.id===selected);navigator.clipboard.writeText('我选择配色「'+p.name+'」（'+p.id+'）。请把该配色角色写入 design-recipe 并开始完整排版配图。').then(()=>ev.target.textContent='已复制 ✓')}};</script></body></html>'''

if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--input",required=True,type=Path);ap.add_argument("--output",required=True,type=Path);a=ap.parse_args();d=load(a.input);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(build(d),encoding="utf-8");print("Built:",a.output)
