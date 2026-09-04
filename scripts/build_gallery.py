#!/usr/bin/env python3
"""Build a live WeChat component-theme gallery from semantic HTML."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


THEMES = {
    "product-green": {
        "name": "产品绿",
        "note": "SaaS 产品、教程与工具发布",
        "swatch": "#059669",
        "roles": {
            "article": "max-width:677px;margin:0 auto;padding:24px 0 36px;background:#fff;color:#374151;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;line-height:1.8;letter-spacing:.5px;overflow-x:hidden",
            "hero": "margin:0 20px 30px;padding:30px 24px 26px;background:#fff;border:1.5px solid rgba(5,150,105,.18);border-radius:20px;box-shadow:0 8px 28px rgba(15,23,42,.07)",
            "eyebrow": "margin:0 0 14px;font-size:11px;font-weight:700;letter-spacing:2px;color:#9CA3AF",
            "hero-title": "margin:0;font-size:28px;font-weight:900;line-height:1.08;letter-spacing:-1.5px;color:#111827",
            "hero-accent": "margin:4px 0 0;font-size:28px;font-weight:900;line-height:1.08;letter-spacing:-1.5px;color:#059669",
            "hero-subtitle": "margin:18px 0 0;font-size:13px;line-height:1.8;color:#6B7280",
            "chip-row": "margin:18px 0 0;display:block",
            "chip": "display:inline-block;margin:0 6px 6px 0;padding:4px 9px;border-radius:20px;background:#ECFDF5;color:#047857;font-size:10px;font-weight:700",
            "body": "margin:0 20px 18px;font-size:14px;line-height:1.9;color:#374151;text-align:justify",
            "highlight": "background:linear-gradient(120deg,#FDE68A 0%,rgba(255,255,255,0) 100%);padding:0 4px;border-radius:2px;font-weight:700;color:#111827",
            "section-header": "margin:44px 20px 26px;display:flex;align-items:center",
            "section-no": "display:inline-block;margin-right:14px;font-size:28px;font-weight:900;line-height:1;color:#059669",
            "section-copy": "display:inline-block;padding-left:14px;border-left:1px solid #E5E7EB",
            "section-title": "margin:0;font-size:17px;font-weight:900;line-height:1.5;color:#111827",
            "section-kicker": "margin:2px 0 0;font-size:11px;color:#9CA3AF",
            "callout": "margin:0 20px 24px;padding:14px 16px;border-radius:10px;background:#ECFDF5;border-left:3px solid #059669",
            "callout-label": "margin:0 0 4px;font-size:11px;font-weight:800;letter-spacing:1px;color:#059669",
            "callout-text": "margin:0;font-size:14px;line-height:1.85;color:#065F46",
            "quote": "margin:0 20px 26px;padding:18px;border:0;border-radius:14px;background:#111827;color:#fff;font-size:17px;line-height:1.65;font-weight:800",
            "feature-grid": "margin:0 20px 22px",
            "feature-card": "margin:0 0 10px;padding:15px 16px;border-radius:12px;background:#FAFAFA;border:1px solid #F3F4F6",
            "feature-icon": "display:inline-block;width:24px;height:24px;line-height:24px;text-align:center;border-radius:7px;background:#ECFDF5;color:#059669;font-weight:900;margin-right:8px",
            "feature-title": "display:inline;margin:0;font-size:14px;font-weight:800;color:#111827",
            "feature-text": "margin:6px 0 0;padding-left:34px;font-size:13px;line-height:1.75;color:#6B7280",
            "steps": "margin:0 20px 24px",
            "step-card": "margin:0 0 9px;padding:11px 14px;border-radius:9px;background:#F9FAFB;border:1px solid #E5E7EB",
            "step-no": "color:#059669;font-size:13px;font-weight:900;margin-right:8px",
            "step-text": "font-size:14px;line-height:1.8;color:#374151",
            "terminal": "margin:0 20px 24px;border:1.5px solid #E5E7EB;border-radius:12px;overflow:hidden;background:#fff",
            "terminal-bar": "padding:9px 12px;background:#FAFAFA;border-bottom:1px solid #F3F4F6;font-size:10px;color:#9CA3AF",
            "terminal-body": "padding:15px;font-family:'SF Mono',Consolas,monospace;font-size:13px;line-height:2;color:#374151;word-break:break-all",
            "figure": "margin:0 20px 24px;padding:8px;border-radius:14px;background:#FAFAFA;border:1px solid #E5E7EB",
            "caption": "margin:5px 0 2px;font-size:10px;line-height:1.6;color:#9CA3AF;text-align:center",
            "summary": "margin:44px 20px 0;padding:20px 18px;border-radius:14px;background:#111827",
            "summary-title": "margin:0 0 10px;font-size:11px;color:#6EE7B7;font-weight:800;letter-spacing:1.5px",
            "summary-text": "margin:0;font-size:15px;line-height:1.8;color:#E5E7EB",
            "divider": "margin:28px 20px;border:0;border-top:1px solid #E5E7EB",
            "svg-accent": "fill:#059669;stroke:#059669",
            "svg-soft": "fill:#ECFDF5;stroke:#A7F3D0",
            "svg-ink": "fill:#111827",
            "svg-muted": "fill:#6B7280",
        },
    },
    "bytedance-blue": {
        "name": "字节蓝", "note": "AI、科技解读与现代工具", "swatch": "#3370FF",
        "roles": {}
    },
    "github-paper": {
        "name": "GitHub 纸", "note": "开源项目、开发教程与技术文档", "swatch": "#24292F",
        "roles": {}
    },
    "sspai-red": {
        "name": "少数派红", "note": "中文科技媒体式产品推荐", "swatch": "#D71920",
        "roles": {}
    },
    "editorial-ink": {
        "name": "编辑墨黑", "note": "深度分析、观点与长文", "swatch": "#171717",
        "roles": {}
    },
    "warm-story": {
        "name": "暖色故事", "note": "个人创作、经验分享与叙事", "swatch": "#C26D3B",
        "roles": {}
    },
}


def derived(base: dict[str, str], accent: str, soft: str, ink: str, body: str,
            radius: str, shadow: str, serif: bool = False) -> dict[str, str]:
    """Derive a complete but structurally different component system."""
    r = dict(base)
    family = "Georgia,'Songti SC','SimSun',serif" if serif else "-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif"
    replacements = {
        "#059669": accent, "#047857": accent, "#065F46": body,
        "#ECFDF5": soft, "#A7F3D0": soft, "#111827": ink, "#374151": body,
    }
    for key, value in list(r.items()):
        for old, new in replacements.items():
            value = value.replace(old, new)
        value = re.sub(r"border-radius:(20|14|12|10|9|7)px", f"border-radius:{radius}", value)
        value = value.replace("box-shadow:0 8px 28px rgba(15,23,42,.07)", f"box-shadow:{shadow}")
        value = re.sub(r"font-family:[^;]+", f"font-family:{family}", value)
        r[key] = value
    return r


BASE = THEMES["product-green"]["roles"]
THEMES["bytedance-blue"]["roles"] = derived(BASE, "#3370FF", "#EEF4FF", "#10214A", "#344563", "16px", "0 10px 30px rgba(51,112,255,.12)")
THEMES["github-paper"]["roles"] = derived(BASE, "#24292F", "#F6F8FA", "#1F2328", "#3B434B", "6px", "0 2px 8px rgba(31,35,40,.08)")
THEMES["sspai-red"]["roles"] = derived(BASE, "#D71920", "#FFF1F1", "#222222", "#444444", "4px", "0 6px 20px rgba(215,25,32,.08)")
THEMES["editorial-ink"]["roles"] = derived(BASE, "#171717", "#F5F2EC", "#171717", "#34312D", "0px", "none", serif=True)
THEMES["warm-story"]["roles"] = derived(BASE, "#C26D3B", "#FBF1E8", "#3B2921", "#59463C", "18px", "0 10px 28px rgba(95,58,36,.10)", serif=True)

# Structural overrides make themes different component systems, not recolors.
THEMES["bytedance-blue"]["roles"].update({
    "hero": "margin:0 20px 30px;padding:30px 24px 26px;background:linear-gradient(145deg,#F5F8FF,#EEF4FF);border:0;border-radius:18px;box-shadow:0 12px 32px rgba(51,112,255,.14)",
    "section-no": "display:inline-block;margin-right:12px;padding:5px 8px;border-radius:8px;background:#3370FF;color:#fff;font-size:15px;font-weight:900;line-height:1",
    "section-copy": "display:inline-block;padding-left:12px;border-left:0",
    "feature-card": "margin:0 0 10px;padding:15px 16px;border-radius:12px;background:#F5F8FF;border:0;box-shadow:inset 0 0 0 1px #E1E9FF",
})
THEMES["github-paper"]["roles"].update({
    "hero": "margin:0 20px 30px;padding:26px 22px;background:#F6F8FA;border:1px solid #D0D7DE;border-radius:6px;box-shadow:none",
    "eyebrow": "margin:0 0 12px;font-family:'SF Mono',Consolas,monospace;font-size:11px;font-weight:700;letter-spacing:1px;color:#57606A",
    "section-no": "display:inline-block;margin-right:12px;padding:5px 7px;border:1px solid #D0D7DE;border-radius:6px;background:#F6F8FA;color:#24292F;font-family:'SF Mono',Consolas,monospace;font-size:13px;font-weight:800;line-height:1",
    "feature-card": "margin:0 0 8px;padding:14px 15px;border-radius:6px;background:#fff;border:1px solid #D0D7DE",
    "callout": "margin:0 20px 24px;padding:13px 15px;border-radius:6px;background:#F6F8FA;border:1px solid #D0D7DE;border-left:4px solid #24292F",
})
THEMES["sspai-red"]["roles"].update({
    "hero": "margin:0 20px 30px;padding:28px 22px;background:#fff;border:0;border-left:7px solid #D71920;border-radius:0;box-shadow:0 6px 22px rgba(215,25,32,.09)",
    "hero-accent": "margin:4px 0 0;font-size:28px;font-weight:900;line-height:1.08;letter-spacing:-1.5px;color:#D71920",
    "section-header": "margin:42px 20px 24px;padding:0 0 8px;display:flex;align-items:center;border-bottom:3px solid #D71920",
    "section-no": "display:inline-block;margin-right:10px;color:#D71920;font-size:15px;font-weight:900;line-height:1",
    "section-copy": "display:inline-block;padding-left:10px;border-left:1px solid #E5E7EB",
    "feature-card": "margin:0 0 10px;padding:15px 16px;border-radius:4px;background:#fff;border-left:3px solid #D71920;box-shadow:0 4px 14px rgba(0,0,0,.06)",
})
THEMES["editorial-ink"]["roles"].update({
    "hero": "margin:0 20px 34px;padding:24px 0 22px;background:#fff;border:0;border-top:4px solid #171717;border-bottom:1px solid #171717;border-radius:0;box-shadow:none",
    "hero-title": "margin:0;font-family:Georgia,'Songti SC','SimSun',serif;font-size:29px;font-weight:800;line-height:1.22;letter-spacing:-1px;color:#171717",
    "hero-accent": "margin:5px 0 0;font-family:Georgia,'Songti SC','SimSun',serif;font-size:29px;font-weight:800;line-height:1.22;letter-spacing:-1px;color:#171717",
    "section-header": "margin:46px 20px 25px;padding-bottom:8px;display:block;border-bottom:1px solid #171717",
    "section-no": "display:block;margin:0 0 5px;font-size:11px;font-weight:700;letter-spacing:2px;color:#777",
    "section-copy": "display:block;padding:0;border:0",
    "feature-card": "margin:0;padding:14px 0;border-radius:0;background:#fff;border:0;border-bottom:1px solid #DDD8CF",
    "callout": "margin:0 20px 24px;padding:15px 0;border-radius:0;background:#fff;border:0;border-top:1px solid #171717;border-bottom:1px solid #171717",
})
THEMES["warm-story"]["roles"].update({
    "hero": "margin:0 20px 30px;padding:32px 24px 28px;background:#FBF1E8;border:0;border-radius:24px;box-shadow:0 12px 30px rgba(95,58,36,.10)",
    "section-header": "margin:46px 20px 26px;padding:13px 16px;display:flex;align-items:center;background:#FBF1E8;border-radius:18px",
    "section-no": "display:inline-block;margin-right:12px;color:#C26D3B;font-size:22px;font-weight:900;line-height:1",
    "section-copy": "display:inline-block;padding-left:12px;border-left:1px solid #E8CDBA",
    "feature-card": "margin:0 0 11px;padding:16px;border-radius:18px;background:#FFF9F4;border:1px solid #F1DED0",
    "quote": "margin:0 20px 26px;padding:20px;border:0;border-radius:20px;background:#3B2921;color:#fff;font-family:Georgia,'Songti SC','SimSun',serif;font-size:17px;line-height:1.75;font-weight:700",
})


def extract_article(raw: str) -> str:
    match = re.search(r"<!--\s*ARTICLE HTML START\s*-->(.*?)<!--\s*ARTICLE HTML END\s*-->", raw, re.S | re.I)
    fragment = match.group(1).strip() if match else raw.strip()
    if 'data-wx-role="article"' not in fragment and "data-wx-role='article'" not in fragment:
        raise ValueError('Input must contain an outer element with data-wx-role="article"')
    return fragment


def build(fragment: str, title: str, default_theme: str) -> str:
    themes_json = json.dumps(THEMES, ensure_ascii=False).replace("</", "<\\/")
    safe_title = html.escape(title)
    buttons = "".join(
        f'<button data-theme="{key}" onclick="applyTheme(\'{key}\')"><i style="background:{theme["swatch"]}"></i><b>{html.escape(theme["name"])}</b><small>{html.escape(theme["note"])}</small></button>'
        for key, theme in THEMES.items()
    )
    return f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{safe_title}</title>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#fff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif;color:#111827}}.studio{{max-width:1120px;margin:0 auto;padding:18px}}.toolbar{{background:#fff;border:1px solid #e5e7eb;border-radius:16px;padding:16px;margin-bottom:24px}}.toolbar h1{{font-size:18px;margin:0 0 5px}}.toolbar p{{font-size:12px;color:#6b7280;margin:0 0 13px}}.themes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px}}.themes button{{position:relative;text-align:left;background:#fff;border:1px solid #e5e7eb;border-radius:10px;padding:10px;cursor:pointer;color:#111827}}.themes button.active{{border:2px solid #111827;padding:9px}}.themes i{{display:block;width:18px;height:18px;border-radius:50%;margin-bottom:7px}}.themes b{{display:block;font-size:13px}}.themes small{{display:block;margin-top:3px;font-size:10px;line-height:1.4;color:#9ca3af}}.actions{{display:flex;gap:8px;margin-top:12px}}.actions button{{border:0;border-radius:8px;padding:10px 14px;font-size:13px;font-weight:700;cursor:pointer}}#copy{{background:#111827;color:#fff}}#top{{background:#f3f4f6;color:#111827}}#article-content{{max-width:677px;margin:0 auto}}@media(max-width:600px){{.studio{{padding:10px}}.toolbar{{border-radius:12px}}}}</style></head>
<body><main class="studio"><section class="toolbar"><h1>{safe_title}</h1><p>选择风格后可直接复制正文到公众号。</p><div class="themes">{buttons}</div><div class="actions"><button id="copy" onclick="copyArticle()">复制当前风格 HTML</button><button id="top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">回到顶部</button></div></section><div id="article-content">{fragment}</div></main>
<script>const THEMES={themes_json};function applyTheme(id){{if(!THEMES[id])id='{default_theme}';const t=THEMES[id];document.querySelectorAll('[data-wx-role]').forEach(el=>{{const role=el.dataset.wxRole;if(t.roles[role])el.setAttribute('style',t.roles[role])}});document.querySelectorAll('[data-theme]').forEach(b=>b.classList.toggle('active',b.dataset.theme===id));document.title=t.name+' · {safe_title}';localStorage.setItem('wechat-design-theme',id)}}function copyArticle(){{const root=document.getElementById('article-content');const clone=root.cloneNode(true);clone.querySelectorAll('[data-wx-role]').forEach(el=>el.removeAttribute('data-wx-role'));const payload=clone.innerHTML;navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([payload],{{type:'text/html'}}),'text/plain':new Blob([payload],{{type:'text/plain'}})}})]).then(()=>{{const b=document.getElementById('copy');b.textContent='已复制 ✓';setTimeout(()=>b.textContent='复制当前风格 HTML',1800)}})}}const requested=new URLSearchParams(location.search).get('theme');applyTheme(requested||localStorage.getItem('wechat-design-theme')||'{default_theme}');</script></body></html>'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--title", default="WeChat Design Studio")
    parser.add_argument("--default-theme", choices=THEMES, default="product-green")
    args = parser.parse_args()
    raw = args.input.read_text(encoding="utf-8")
    fragment = extract_article(raw)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build(fragment, args.title, args.default_theme), encoding="utf-8")
    print(f"Built: {args.output}")
    print("Themes: " + ", ".join(THEMES))


if __name__ == "__main__":
    main()
