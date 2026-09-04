#!/usr/bin/env python3
"""Build a WeChat wide cover, center-square crop, and safe-area proof."""
import argparse
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageFilter

W,H=900,383
FONT_CANDIDATES=[
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
]

def font(size):
    for p in FONT_CANDIDATES:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()

def bold_font(size):
    p="/System/Library/Fonts/Hiragino Sans GB.ttc"
    if Path(p).exists(): return ImageFont.truetype(p,size,index=3)
    return font(size)

def latin_font(size):
    p="/System/Library/Fonts/Avenir Next.ttc"
    if Path(p).exists(): return ImageFont.truetype(p,size,index=3)
    return font(size)

def tracked_text(draw,center_y,text,f,fill,tracking=1.8):
    widths=[draw.textlength(ch,font=f) for ch in text]
    total=sum(widths)+tracking*max(0,len(text)-1)
    x=W/2-total/2
    for ch,cw in zip(text,widths):
        draw.text((x,center_y),ch,font=f,anchor="lm",fill=fill)
        x+=cw+tracking

def cover_crop(im):
    ratio=W/H; iw,ih=im.size
    if iw/ih>ratio:
        nw=int(ih*ratio); left=(iw-nw)//2; box=(left,0,left+nw,ih)
    else:
        nh=int(iw/ratio); top=(ih-nh)//2; box=(0,top,iw,top+nh)
    return im.crop(box).resize((W,H),Image.Resampling.LANCZOS)

def fit_title(draw,text,max_width,max_size=38,min_size=20):
    for size in range(max_size,min_size-1,-1):
        f=font(size); box=draw.textbbox((0,0),text,font=f,stroke_width=1)
        if box[2]-box[0]<=max_width:return f
    return font(min_size)

def build(inp,out_dir,title,eyebrow,style,accent):
    out_dir.mkdir(parents=True,exist_ok=True)
    base=cover_crop(Image.open(inp).convert("RGB"))
    wide=base.convert("RGBA"); overlay=Image.new("RGBA",wide.size,(0,0,0,0)); d=ImageDraw.Draw(overlay)
    safe_left=(W-H)//2; safe_right=safe_left+H
    if style=="shelf":
        # Centered translucent title shelf, entirely inside the square-safe zone.
        d.rounded_rectangle((safe_left+18,14,safe_right-18,105),radius=16,fill=(6,13,28,188),outline=(74,222,128,105),width=2)
        ef=font(11); d.text((W/2,30),eyebrow,font=ef,anchor="mm",fill=(134,239,172,255),stroke_width=0)
        tf=fit_title(d,title,H-76); d.text((W/2,68),title,font=tf,anchor="mm",fill="white",stroke_width=2,stroke_fill=(5,12,25,190))
    else:
        lines=title.split("|",1)
        ef=latin_font(9); tracked_text(d,22,eyebrow,ef,(104,113,125,255),tracking=1.5)
        first=bold_font(41)
        d.text((W/2,61),lines[0],font=first,anchor="mm",fill=(17,20,24,255))
        if len(lines)>1:
            second=bold_font(44)
            d.text((W/2,108),lines[1],font=second,anchor="mm",fill=accent)
            d.rounded_rectangle((W/2-18,136,W/2+18,139),radius=2,fill=accent)
    wide=Image.alpha_composite(wide,overlay).convert("RGB")
    wide_path=out_dir/"cover-wide-900x383.jpg"; wide.save(wide_path,quality=90,optimize=True)
    square=wide.crop((safe_left,0,safe_right,H)); square_path=out_dir/"cover-square-383x383.jpg"; square.save(square_path,quality=90,optimize=True)
    proof=wide.copy(); pd=ImageDraw.Draw(proof); pd.rectangle((safe_left,0,safe_right-1,H-1),outline=(74,222,128),width=4); pd.text((safe_left+8,H-18),"CENTER SQUARE SAFE AREA",font=font(9),fill=(255,255,255),stroke_width=2,stroke_fill=(0,0,0))
    proof_path=out_dir/"cover-safe-area-proof.jpg"; proof.save(proof_path,quality=88,optimize=True)
    print(wide_path);print(square_path);print(proof_path)

if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--input",required=True,type=Path);ap.add_argument("--output-dir",required=True,type=Path);ap.add_argument("--title",required=True);ap.add_argument("--eyebrow",default="");ap.add_argument("--style",choices=["shelf","clean"],default="shelf");ap.add_argument("--accent",default="#20BFE8");a=ap.parse_args();build(a.input,a.output_dir,a.title,a.eyebrow,a.style,a.accent)
