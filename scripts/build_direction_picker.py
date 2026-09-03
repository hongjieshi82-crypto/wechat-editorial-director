#!/usr/bin/env python3
"""Build a pre-layout picker from three editorial-direction proposals."""
import argparse, html, json
from pathlib import Path

FIELDS = {"id","name","concept","why","opening","rhythm","visuals","typography","palette","tradeoff"}
def e(x): return html.escape(str(x))

def load(path):
    data=json.loads(path.read_text(encoding="utf-8")); proposals=data.get("proposals",[])
    if len(proposals)!=3: raise ValueError("Exactly three proposals are required")
    ids=set()
    for p in proposals:
        missing=FIELDS-set(p)
        if missing: raise ValueError("Missing fields: "+", ".join(sorted(missing)))
        if p["id"] in ids: raise ValueError("Proposal ids must be unique")
        ids.add(p["id"])
    return data

def build(data):
    title=e(data.get("article_title","公众号文章")); diagnosis=data.get("diagnosis",{})
    cards=[]
    for i,p in enumerate(data["proposals"],1):
        visuals="".join(f"<li>{e(v)}</li>" for v in p["visuals"])
        cards.append(f'''<article data-id="{e(p['id'])}" onclick="pick('{e(p['id'])}')"><b class="num">0{i}</b><small>EDITORIAL DIRECTION</small><h2>{e(p['name'])}</h2><p class="concept">{e(p['concept'])}</p><dl><dt>为什么适合</dt><dd>{e(p['why'])}</dd><dt>开场构图</dt><dd>{e(p['opening'])}</dd><dt>阅读节奏</dt><dd>{e(p['rhythm'])}</dd><dt>配图语言</dt><dd><ul>{visuals}</ul></dd><dt>字体</dt><dd>{e(p['typography'])}</dd><dt>色彩角色</dt><dd>{e(p['palette'])}</dd><dt>取舍</dt><dd>{e(p['tradeoff'])}</dd></dl><button>选择这个方向</button></article>''')
    # script[type=application/json] is a raw-text element: HTML-escaping quotes
    # makes JSON.parse fail. Only neutralize a possible closing script sequence.
    payload=json.dumps(data,ensure_ascii=False).replace("</", "<\\/")
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · 编辑方向</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#f3f4f6;color:#111827;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif}}main{{max-width:1160px;margin:auto;padding:38px 20px 60px}}header{{max-width:760px;margin:0 auto 28px;text-align:center}}header small{{letter-spacing:3px;color:#9ca3af;font-weight:800}}h1{{font-size:30px;line-height:1.2;margin:10px}}header p{{font-size:14px;line-height:1.8;color:#6b7280}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}article{{background:#fff;padding:23px;border:2px solid transparent;border-radius:18px;box-shadow:0 7px 25px #0f172a12;cursor:pointer}}article.selected{{border-color:#111827}}.num{{display:block;font:800 38px Georgia;color:#e5e7eb}}article small{{font-size:9px;letter-spacing:2px;color:#9ca3af}}h2{{font-size:21px;margin:8px 0}}.concept{{min-height:68px;font-size:13px;line-height:1.75;color:#4b5563}}dl{{margin:16px 0}}dt{{margin-top:12px;font-size:11px;font-weight:800}}dd{{margin:4px 0;font-size:12px;line-height:1.7;color:#6b7280}}ul{{margin:0;padding-left:17px}}button{{width:100%;border:0;border-radius:9px;padding:11px;background:#111827;color:white;font-weight:800}}#result{{display:none;max-width:760px;margin:24px auto 0;padding:17px;background:#111827;border-radius:13px;color:white;text-align:center}}#result p{{font-size:12px;color:#d1d5db}}#result button{{width:auto;background:white;color:#111827}}@media(max-width:850px){{.grid{{grid-template-columns:1fr}}.concept{{min-height:0}}}}
</style></head><body><main><header><small>EDITORIAL DIRECTION</small><h1>{title}</h1><p>{e(diagnosis.get('summary','先选编辑方向，再开始排版和配图。'))}</p></header><section class="grid">{''.join(cards)}</section><section id="result"><strong id="chosen"></strong><p>复制指令发给 Agent，它才会开始完整设计。</p><button onclick="copyChoice(event)">复制选择指令</button></section></main><script id="data" type="application/json">{payload}</script><script>
const D=JSON.parse(document.getElementById('data').textContent);let selected='';function pick(id){{selected=id;document.querySelectorAll('article').forEach(x=>x.classList.toggle('selected',x.dataset.id===id));const p=D.proposals.find(x=>x.id===id);document.getElementById('chosen').textContent='已选：'+p.name;document.getElementById('result').style.display='block';document.getElementById('result').scrollIntoView({{behavior:'smooth'}})}}function copyChoice(ev){{const p=D.proposals.find(x=>x.id===selected),t='我选择编辑方向「'+p.name+'」（'+p.id+'）。请按它制作 design-recipe、image-plan 和公众号预览。';navigator.clipboard.writeText(t).then(()=>ev.target.textContent='已复制 ✓')}}
</script></body></html>'''

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True,type=Path); ap.add_argument("--output",required=True,type=Path); a=ap.parse_args(); d=load(a.input); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(build(d),encoding="utf-8"); print("Built:",a.output)
