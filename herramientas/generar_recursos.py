#!/usr/bin/env python3
"""Genera los recursos originales del README ANSIBLE.

Requisitos: Python 3.10+ y Pillow. No consulta servicios externos.
Uso: python herramientas/generar_recursos.py
Son ilustraciones de interfaz y diagramas, no capturas del laboratorio.
"""
from __future__ import annotations

import argparse
import math
from functools import lru_cache
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ANIM = ROOT / "recursos" / "animaciones"
STILL = ROOT / "recursos" / "imagenes"
SCALE = 2
W = 1200
BG = "#0b1120"
PANEL = "#111d31"
EDGE = "#293a51"
TEXT = "#f0f6ff"
MUTED = "#a4b5ca"
CYAN = "#57d9f5"
GREEN = "#79e7bd"
RED = "#ff6c7c"
AMBER = "#f4c784"


def rgb(color):
    color = color.lstrip("#")
    return tuple(int(color[k:k + 2], 16) for k in (0, 2, 4))


@lru_cache(maxsize=None)
def font(size=20, kind="sans"):
    names = {
        "sans": ("DejaVuSans.ttf", "arial.ttf"),
        "bold": ("DejaVuSans-Bold.ttf", "arialbd.ttf"),
        "mono": ("DejaVuSansMono.ttf", "consola.ttf"),
    }
    roots = [Path("/usr/share/fonts/truetype/dejavu"), Path("C:/Windows/Fonts")]
    for directory in roots:
        for name in names[kind]:
            if (directory / name).exists():
                return ImageFont.truetype(str(directory / name), size * SCALE)
    raise RuntimeError("Instala las fuentes DejaVu Sans / Mono o indica una ruta local en font().")


def txt(d, xy, value, size=20, fill=TEXT, kind="sans", anchor=None):
    d.text((int(xy[0] * SCALE), int(xy[1] * SCALE)), value, fill=fill,
           font=font(size, kind), anchor=anchor, stroke_width=0)


def line(d, points, fill=EDGE, width=1):
    d.line([(int(x * SCALE), int(y * SCALE)) for x, y in points], fill=fill,
           width=max(1, int(width * SCALE)), joint="curve")


def rect(d, box, fill=PANEL, outline=None, radius=12, width=1):
    d.rounded_rectangle(tuple(int(x * SCALE) for x in box), radius=int(radius * SCALE),
                        fill=fill, outline=outline, width=int(width * SCALE))


def dot(d, x, y, r=3, color=CYAN):
    d.ellipse(((x-r)*SCALE, (y-r)*SCALE, (x+r)*SCALE, (y+r)*SCALE), fill=color)


def pill(d, box, label, color=CYAN, size=13, fill="#142638"):
    rect(d, box, fill=fill, outline=color, radius=(box[3]-box[1])/2)
    txt(d, ((box[0]+box[2])/2, (box[1]+box[3])/2-1), label, size, color, "mono", "mm")


def base(height):
    im = Image.new("RGB", (W*SCALE, height*SCALE), BG)
    d = ImageDraw.Draw(im)
    top, bottom = rgb("#101c30"), rgb("#090f1d")
    for y in range(height*SCALE):
        f = y / (height*SCALE-1)
        c = tuple(round(top[k]*(1-f)+bottom[k]*f) for k in range(3))
        d.line((0, y, W*SCALE, y), fill=c)
    rect(d, (1, 1, W-2, height-2), fill=None, outline=EDGE, radius=22)
    return im


def dashed(d, a, b, color=EDGE, width=2, dash=8, gap=7):
    length = math.hypot(b[0]-a[0], b[1]-a[1])
    n = 0.
    while n < length:
        q = min(n+dash, length)
        p1 = (a[0]+(b[0]-a[0])*n/length, a[1]+(b[1]-a[1])*n/length)
        p2 = (a[0]+(b[0]-a[0])*q/length, a[1]+(b[1]-a[1])*q/length)
        line(d, [p1, p2], color, width)
        n += dash+gap


def hero(t=0, static=False):
    im = base(460)
    d = ImageDraw.Draw(im)
    for x in range(745, 1190, 28):
        for y in range(85, 365, 28):
            dot(d, x, y, .8, "#25344b")
    txt(d, (52, 31), "LUBO616  /  LABORATORIO DE AUTOMATIZACIÓN", 15, MUTED, "mono")
    pill(d, (918, 30, 1147, 62), "INVESTIGACIÓN APLICADA", CYAN, 11)
    txt(d, (48, 87), "ANSIBLE", 108, TEXT, "bold")
    rect(d, (55, 216, 104, 221), CYAN, radius=2)
    rect(d, (111, 216, 131, 221), RED, radius=2)
    txt(d, (51, 240), "Infraestructura con criterio.", 30, TEXT, "bold")
    phrases = ["Investigar antes de cambiar.", "Automatizar con evidencia.", "Documentar para reproducir."]
    if static:
        phrase = "Investigar. Automatizar. Demostrar."
    else:
        p = int(t // 3) % len(phrases)
        f = t % 3
        s = phrases[p]
        if t < .75:
            phrase = phrases[0]
        elif f < .6:
            phrase = s[:int(len(s)*f/.6)]
        elif f > 2.7:
            phrase = s[:int(len(s)*(3-f)/.3)]
        else:
            phrase = s
    txt(d, (55, 301), "> " + phrase, 21, CYAN, "mono")
    if not static and int(t*2)%2 == 0:
        tw = d.textlength("> "+phrase, font=font(21,"mono"))/SCALE
        rect(d, (59+tw, 305, 70+tw, 328), CYAN, radius=0)
    cx, cy = 956, 232
    for r, c in [(139,"#23354c"),(116,"#1d3047"),(94,"#264055")]:
        d.ellipse(((cx-r)*SCALE,(cy-r)*SCALE,(cx+r)*SCALE,(cy+r)*SCALE), outline=c, width=2*SCALE)
    angle = t/9*math.pi*2-.7
    for off, color in [(0,CYAN),(math.pi,RED)]:
        px,py=cx+139*math.cos(angle+off),cy+139*math.sin(angle+off)
        dot(d,px,py,7,color)
        dot(d,px,py,2,TEXT)
    for ax,ay in [(819,154),(1098,211),(935,361)]:
        line(d, [(cx,cy),(ax,ay)], "#385971",2)
        u=(t/3)%1
        dot(d,cx+(ax-cx)*u,cy+(ay-cy)*u,3,GREEN)
    rect(d, (886, 177, 1026, 287), "#122d40", CYAN, 19, 2)
    txt(d,(956,213),">_",31,GREEN,"mono","mm")
    txt(d,(956,256),"AAP",24,TEXT,"bold","mm")
    for ax,ay,lab,col in [(819,154,"{ }",CYAN),(1098,211,"SSH",GREEN),(935,361,"GIT",RED)]:
        rect(d,(ax-29,ay-24,ax+29,ay+24),"#152136",col,10)
        txt(d,(ax,ay),lab,15,col,"mono","mm")
    line(d,[(53,397),(1147,397)], EDGE)
    txt(d,(54,417),"ESPAÑOL  /  CÓDIGO + DECISIONES + EVIDENCIAS",13,MUTED,"mono")
    dot(d,941,427,4,GREEN)
    txt(d,(954,417),"LAB EN EVOLUCIÓN",13,GREEN,"mono")
    return im.resize((W,460),Image.Resampling.LANCZOS)


def terminal(t=0, static=False):
    im=base(478)
    d=ImageDraw.Draw(im)
    rect(d,(1,1,1197,57),"#172438",None,22)
    rect(d,(1,30,1197,57),"#172438",None,0)
    for x,c in [(30,RED),(50,AMBER),(70,GREEN)]: dot(d,x,28,5,c)
    txt(d,(97,17),"PRUEBA 01 / CONECTIVIDAD",16,TEXT,"mono")
    txt(d,(857,19),"RECREACIÓN DIDÁCTICA",13,MUTED,"mono")
    complete=static or t<.7 or t>6.0
    command="$ ansible nodo-demo -m ansible.builtin.ping"
    if complete:
        visible=command
    else:
        visible=command[:max(2,min(len(command),int((t-.7)/2.2*len(command))))]
    txt(d,(42,86),visible,22,CYAN,"mono")
    if not complete and t<3.0:
        tw=d.textlength(visible,font=font(22,"mono"))/SCALE
        rect(d,(45+tw,92,55+tw,115),CYAN,radius=0)
    txt(d,(43,137),"SSH por llave · cuenta dedicada · sin elevación de privilegios",16,MUTED)
    if complete or t>=3.1:
        for i,(val,col) in enumerate([
            ("nodo-demo | SUCCESS => {",GREEN),
            ('    "changed": false,',TEXT),
            ('    "ping": "pong"',GREEN),
            ("}",TEXT),
        ]):
            if complete or t >= 3.1+i*.48:
                txt(d,(43,193+39*i),val,24,col,"mono")
    rect(d,(859,191,1147,358),"#102a2b", "#28524a",18)
    if complete or t>=5:
        txt(d,(1003,237),"pong",54,GREEN,"mono","mm")
        txt(d,(1003,299),"Conexión + Python",17,TEXT,"sans","mm")
        txt(d,(1003,328),"Respuesta esperada",14,MUTED,"sans","mm")
    else:
        txt(d,(1003,254),"Conectando…",19,CYAN,"mono","mm")
        for j in range(3): dot(d,979+j*24,300,4,CYAN if int(t*4)%3==j else "#315257")
    line(d,[(42,409),(1147,409)],EDGE)
    txt(d,(42,430),"DATOS DE EJEMPLO / NO ES UNA CAPTURA DE EJECUCIÓN",14,MUTED,"mono")
    return im.resize((W,478),Image.Resampling.LANCZOS)


def architecture(t=0, static=False):
    im=base(430)
    d=ImageDraw.Draw(im)
    txt(d,(43,30),"DEL CÓDIGO A LA EVIDENCIA",28,TEXT,"bold")
    txt(d,(44,75),"Arquitectura lógica · alcance actual del laboratorio",17,MUTED)
    # El enlace Git -> AAP aún es un objetivo, no una integración validada.
    dashed(d,(335,211),(439,211),"#6d6170",2)
    txt(d,(387,186),"pendiente",12,AMBER,"mono","mm")
    line(d,[(750,211),(810,211),(810,174),(864,174)],CYAN,2)
    line(d,[(810,211),(810,292)],"#465269",2)
    dashed(d,(810,292),(864,292),"#617189",2)
    if not static:
        pts=[(750,211),(810,211),(810,174),(864,174)]
        lengths=[60,37,54]
        pos=(t/2.6)%1*sum(lengths)
        for j,l in enumerate(lengths):
            if pos<=l:
                a,b=pts[j],pts[j+1]
                dot(d,a[0]+(b[0]-a[0])*pos/l,a[1]+(b[1]-a[1])*pos/l,5,GREEN)
                break
            pos-=l
    rect(d,(43,143,335,298),PANEL,EDGE,16)
    txt(d,(66,161),"01 / FUENTE",13,MUTED,"mono")
    txt(d,(65,190),"GitHub",33,TEXT,"bold")
    txt(d,(66,242),"Código y documentación",16,MUTED)
    txt(d,(66,269),"Integración con AAP pendiente",13,AMBER)
    rect(d,(439,143,750,298),"#12293b",CYAN,16)
    txt(d,(463,161),"02 / ORQUESTACIÓN",13,CYAN,"mono")
    txt(d,(462,190),"AAP",33,TEXT,"bold")
    txt(d,(463,242),"Entorno de ejecución",17,MUTED)
    txt(d,(463,269),"Inventario + credencial SSH",13,TEXT)
    rect(d,(864,126,1157,221),"#102a2b","#365c51",14)
    txt(d,(883,139),"03 / DESARROLLO",13,GREEN,"mono")
    txt(d,(883,165),"Nodo Linux",22,TEXT,"bold")
    txt(d,(883,196),"ping + facts validados",13,GREEN)
    rect(d,(864,244,1157,339),PANEL,EDGE,14)
    txt(d,(883,258),"04 / QA",13,MUTED,"mono")
    txt(d,(883,284),"Nodo de pruebas",21,TEXT,"bold")
    txt(d,(883,315),"Ejecución pendiente",13,AMBER)
    line(d,[(44,368),(1155,368)],EDGE)
    txt(d,(44,387),"LÍNEA CONTINUA: VALIDADO",12,GREEN,"mono")
    txt(d,(429,387),"LÍNEA DISCONTINUA: PENDIENTE",12,AMBER,"mono")
    txt(d,(966,387),"MAPA CONCEPTUAL",12,MUTED,"mono")
    return im.resize((W,430),Image.Resampling.LANCZOS)


def save_gif(name, renderer, seconds, fps):
    renderer(0,static=True).save(STILL/f"{name}.png", optimize=True)
    frames=[]
    # Paleta compartida para que fondos y tipografía no cambien entre fotogramas.
    samples=[renderer(t) for t in (0,seconds*.22,seconds*.55,seconds*.8)]
    sheet=Image.new("RGB",(W,samples[0].height*4))
    for i,sample in enumerate(samples): sheet.paste(sample,(0,i*sample.height))
    palette=sheet.quantize(colors=128,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE)
    for i in range(round(seconds*fps)):
        frame=renderer(i/fps).quantize(palette=palette,dither=Image.Dither.NONE)
        frames.append(frame)
    frames[0].save(ANIM/f"{name}.gif",save_all=True,append_images=frames[1:],
                   duration=round(1000/fps/10)*10,loop=0,optimize=True,disposal=1)
    print(f"{name}.gif: {(ANIM/f'{name}.gif').stat().st_size/1024:.0f} KiB / {len(frames)} fotogramas")


def svg_assets():
    techs=[("ANSIBLE",CYAN,178),("AAP 2.7",RED,188),("RHEL",GREEN,166),
           ("PODMAN",CYAN,182),("PROXMOX",AMBER,200),("GIT / GITHUB",MUTED,226)]
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="58" viewBox="0 0 1200 58" role="img" aria-label="Tecnologías del laboratorio: Ansible, AAP, RHEL, Podman, Proxmox y GitHub"><title>Tecnologías del laboratorio</title>']
    x=0
    for name,c,width in techs:
        parts += [f'<rect x="{x+2}" y="6" width="{width-10}" height="44" rx="10" fill="{PANEL}" stroke="{EDGE}"/>',
                  f'<circle cx="{x+23}" cy="28" r="3" fill="{c}"/>',
                  f'<text x="{x+39}" y="34" fill="{c}" font-family="DejaVu Sans,Arial,sans-serif" font-size="16" font-weight="700">{escape(name)}</text>']
        x+=width
    parts.append('</svg>')
    (STILL/'tecnologias.svg').write_text(''.join(parts),encoding='utf-8')
    (STILL/'proyecto-001.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="226" viewBox="0 0 1200 226" role="img" aria-label="Proyecto 001: Descubrimiento Linux. En desarrollo. Ping y facts validados.">
<title>Proyecto 001 · Descubrimiento Linux</title>
<rect x="1" y="1" width="1198" height="224" rx="20" fill="#101c30" stroke="#293a51"/>
<rect x="1" y="25" width="5" height="176" rx="2" fill="#57d9f5"/>
<text x="40" y="74" fill="#57d9f5" font-family="DejaVu Sans Mono,monospace" font-size="18">PROYECTO 001</text>
<text x="38" y="130" fill="#f0f6ff" font-family="DejaVu Sans,Arial,sans-serif" font-size="43" font-weight="700">Descubrimiento Linux</text>
<text x="41" y="164" fill="#a4b5ca" font-family="DejaVu Sans,Arial,sans-serif" font-size="18">Conocer el sistema antes de automatizar cambios.</text>
<text x="41" y="197" fill="#79e7bd" font-family="DejaVu Sans,Arial,sans-serif" font-size="15">Hito actual: conexión SSH + recopilación de facts</text>
<rect x="928" y="38" width="228" height="34" rx="17" fill="#30291f" stroke="#6f5636"/>
<text x="1042" y="60" fill="#f4c784" text-anchor="middle" font-family="DejaVu Sans Mono,monospace" font-size="13">EN DESARROLLO</text>
<path d="M1051 123 H1110 M1096 109 L1111 123 L1096 137" fill="none" stroke="#57d9f5" stroke-width="3"/>
<text x="920" y="191" fill="#a4b5ca" font-family="DejaVu Sans Mono,monospace" font-size="14">EXPLORAR PROYECTO</text>
</svg>''',encoding='utf-8')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--solo-estaticas', action='store_true')
    args=parser.parse_args()
    ANIM.mkdir(parents=True,exist_ok=True)
    STILL.mkdir(parents=True,exist_ok=True)
    svg_assets()
    renderers=[('portada',hero,9,12),('terminal',terminal,9,10),('arquitectura',architecture,6,12)]
    for name,renderer,seconds,fps in renderers:
        if args.solo_estaticas:
            renderer(0,static=True).save(STILL/f'{name}.png',optimize=True)
        else:
            save_gif(name,renderer,seconds,fps)


if __name__=='__main__':
    main()
