#!/usr/bin/env python3
"""Rich flat-vector scenes for news-image-20261125, drawn in code.

Each of the 13 top cards (3 leads + 10 features) gets one full layered
scene: an environment background + 2-4 layered elements with scale
contrast (one big motif up front, one small motif far away) + one small
detail + the stat ribbon inside the scene. Flat colours only — no
gradients, no photos, no AI images, no icon libraries.

Lead scenes: viewBox 320x56, artwork y 0..33, ribbon y 33..56.
Feature scenes: viewBox 190x40, artwork y 0..23, ribbon y 23..40.
scene_svg() is called from gen_entry.py with REGIONS/TINTS passed in.

Every scene is written fresh for this edition from the ILLUSTRATION
line in news.md. Similar scenes are kept apart on purpose:
Hormuz (blue strait between ochre cliffs, two tankers, mine) vs
Canary (open deep-blue Atlantic, one crowded wooden boat + orange
rescue vessel) vs Gaza (dusk seafront, apartment blocks, smoke);
Netanyahu (Jerusalem court + gavel + Knesset dome) vs Ramaphosa
(Cape Town court + green roof + sofa full of banknotes); Poland
(jet + dashed red border + radar) vs Sudan (river town + drones +
red-cross tent) vs Ras Tanura (night refinery + drones + sparks).
"""
NAVY = "#14264d"
INK = "#141414"
PAPER = "#fffdf4"
GOLD = "#d8b45a"
RED = "#a31621"


def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def _cloud(cx, cy, s=1.0):
    return (
        f'<ellipse cx="{cx}" cy="{cy}" rx="{13 * s:.1f}" ry="{3.6 * s:.1f}" fill="{PAPER}"/>'
        f'<ellipse cx="{cx + 15 * s:.1f}" cy="{cy - 2 * s:.1f}" rx="{9 * s:.1f}" '
        f'ry="{3 * s:.1f}" fill="{PAPER}"/>'
    )


def _bird(cx, cy, s=1.0):
    return (f'<path d="M{cx} {cy} q{3 * s:.1f} {-3 * s:.1f} {6 * s:.1f} 0 '
            f'q{3 * s:.1f} {-3 * s:.1f} {6 * s:.1f} 0" fill="none" '
            f'stroke="{NAVY}" stroke-width="1"/>')


def _sun(cx, cy, r, fill=GOLD):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'


def _wave_row(y, width, color, phase=0, opacity=0.55):
    n = int(width // 20) + 2
    d = f"M{-10 + phase} {y} q10 -3 20 0 " + "t20 0 " * n
    return (f'<path d="{d}" fill="none" stroke="{color}" '
            f'stroke-width="1.1" opacity="{opacity}"/>')


def _smoke(cx, cy, s=1.0):
    return "".join(
        f'<circle cx="{cx + dx * s:.1f}" cy="{cy + dy * s:.1f}" r="{r * s:.1f}" '
        f'fill="#8a8a86" opacity="0.85"/>'
        for dx, dy, r in ((0, 0, 3.2), (4, -3, 2.6), (-3, -4, 2.4), (7, -6, 2.0))
    )


def _flame(cx, cy, s=1.0):
    return (
        f'<path d="M{cx} {cy} q{-5 * s:.1f} {-4 * s:.1f} 0 {-9 * s:.1f} '
        f'q{3 * s:.1f} {2 * s:.1f} {2 * s:.1f} {-1 * s:.1f} '
        f'q{4 * s:.1f} {3 * s:.1f} {1 * s:.1f} {7 * s:.1f} '
        f'q{1 * s:.1f} {3 * s:.1f} {-3 * s:.1f} {3 * s:.1f} Z" fill="#e8722a"/>'
        f'<path d="M{cx} {cy} q{-2 * s:.1f} {-2 * s:.1f} 0 {-4.5 * s:.1f} '
        f'q{2 * s:.1f} {1 * s:.1f} {1 * s:.1f} {3 * s:.1f} Z" fill="#f5c542"/>'
    )


def _drone(cx, cy, s=1.0, col=NAVY):
    return (
        f'<rect x="{cx - 4 * s:.1f}" y="{cy - 2 * s:.1f}" width="{8 * s:.1f}" '
        f'height="{4 * s:.1f}" fill="{col}"/>'
        f'<line x1="{cx - 7 * s:.1f}" y1="{cy - 3 * s:.1f}" x2="{cx + 7 * s:.1f}" '
        f'y2="{cy + 3 * s:.1f}" stroke="{col}" stroke-width="0.8"/>'
        f'<circle cx="{cx - 8 * s:.1f}" cy="{cy - 3.5 * s:.1f}" r="{1.6 * s:.1f}" fill="{col}"/>'
        f'<circle cx="{cx + 8 * s:.1f}" cy="{cy + 3.5 * s:.1f}" r="{1.6 * s:.1f}" fill="{col}"/>'
    )


# ---------------------------------------------------------------------------
# LEAD 1 — Tariffs: dusk Washington skyline, Capitol dome left, stacked
# cargo containers right, a big tariff stamp slamming down centre,
# tiny "20%" price tag on one container.
# ---------------------------------------------------------------------------
def art_tariffs():
    parts = []
    parts.append('<rect width="320" height="33" fill="#e8d9b8"/>')
    parts.append(_sun(288, 8, 5))
    parts.append(_cloud(120, 6, 0.9))
    parts.append(_bird(200, 8, 0.8))
    # skyline silhouettes, far
    parts.append('<rect x="0" y="18" width="320" height="15" fill="#8a7a5c"/>')
    for x, h in ((8, 8), (96, 6), (150, 9), (230, 7)):
        parts.append(f'<rect x="{x}" y="{26 - h}" width="10" height="{h}" fill="#8a7a5c"/>')
    # Capitol dome, left — big and white so it reads at lead size
    parts.append('<rect x="20" y="13" width="52" height="20" fill="#f7f1de" stroke="#14264d" stroke-width="0.8"/>')
    parts.append('<path d="M20 13 Q46 -1 72 13 Z" fill="#f7f1de" stroke="#14264d" stroke-width="0.8"/>')
    parts.append('<rect x="44" y="-1" width="4" height="5" fill="#f7f1de" stroke="#14264d" stroke-width="0.6"/>')
    parts.append('<rect x="20" y="13" width="52" height="2" fill="#14264d"/>')
    for x in (26, 35, 44, 53, 62):
        parts.append(f'<rect x="{x}" y="18" width="2.5" height="10" fill="#14264d"/>')
    # containers, right — stacked, two colours
    for x, y, c in ((238, 20, "#c96a1e"), (262, 20, "#1f5fa8"), (250, 12, "#1e8a4c"),
                    (274, 12, "#c0392b"), (238, 12, "#6a4fa3")):
        parts.append(f'<rect x="{x}" y="{y}" width="22" height="8" fill="{c}"/>')
        parts.append(f'<line x1="{x + 5}" y1="{y}" x2="{x + 5}" y2="{y + 8}" stroke="#fffdf4" stroke-width="0.7" opacity="0.7"/>')
        parts.append(f'<line x1="{x + 11}" y1="{y}" x2="{x + 11}" y2="{y + 8}" stroke="#fffdf4" stroke-width="0.7" opacity="0.7"/>')
        parts.append(f'<line x1="{x + 17}" y1="{y}" x2="{x + 17}" y2="{y + 8}" stroke="#fffdf4" stroke-width="0.7" opacity="0.7"/>')
    # tiny price tag "20%" on the blue container
    parts.append('<rect x="264" y="21" width="12" height="6" fill="#fffdf4"/>')
    parts.append('<text x="270" y="25.5" font-family="Libre Franklin,sans-serif" font-size="4.5" font-weight="bold" fill="#a31621" text-anchor="middle">20%</text>')
    # tariff stamp, centre — tilted, red border, slamming down
    parts.append('<g transform="rotate(-8 160 17)">')
    parts.append('<rect x="128" y="7" width="64" height="20" fill="none" stroke="#a31621" stroke-width="2.2"/>')
    parts.append('<text x="160" y="21" font-family="Oswald,sans-serif" font-size="12" font-weight="600" fill="#a31621" text-anchor="middle" letter-spacing="1">TARIFF</text>')
    parts.append('</g>')
    parts.append('<line x1="128" y1="30" x2="192" y2="30" stroke="#a31621" stroke-width="1.4"/>')
    return "".join(parts)


# ---------------------------------------------------------------------------
# LEAD 2 — Hormuz: blue strait between two ochre cliffs, two tankers
# with small orange flames and grey smoke, a spiked mine bobbing
# between them, tiny radar dish on the nearer cliff.
# ---------------------------------------------------------------------------
def art_hormuz():
    parts = []
    parts.append('<rect width="320" height="33" fill="#bcd6de"/>')
    parts.append(_sun(160, 7, 5))
    parts.append(_cloud(60, 6, 0.9))
    parts.append(_bird(230, 7, 0.8))
    # far cliff, left; near cliff, right
    parts.append('<polygon points="0,33 0,14 52,10 78,33" fill="#c9a25e"/>')
    parts.append('<polygon points="320,33 320,8 268,12 244,33" fill="#b08a45"/>')
    # radar dish on the near cliff (small detail)
    parts.append('<line x1="292" y1="12" x2="292" y2="6" stroke="#14264d" stroke-width="1.2"/>')
    parts.append('<path d="M286 6 A7 7 0 0 1 298 6 Z" fill="#14264d"/>')
    # strait water
    parts.append('<rect x="70" y="20" width="182" height="13" fill="#2a6f97"/>')
    parts.append(_wave_row(24, 320, "#fffdf4", 0, 0.5))
    parts.append(_wave_row(30, 320, "#fffdf4", -6, 0.4))
    # tanker 1 (far, smaller), tanker 2 (near, bigger)
    parts.append('<rect x="96" y="14" width="52" height="8" fill="#14264d"/>')
    parts.append('<rect x="104" y="9" width="8" height="5" fill="#c0392b"/>')
    parts.append('<rect x="118" y="10" width="20" height="4" fill="#fffdf4"/>')
    parts.append(_flame(140, 14, 0.9))
    parts.append(_smoke(140, 8, 0.8))
    parts.append('<rect x="188" y="18" width="62" height="10" fill="#14264d"/>')
    parts.append('<rect x="198" y="12" width="9" height="6" fill="#c96a1e"/>')
    parts.append('<rect x="214" y="13" width="24" height="5" fill="#fffdf4"/>')
    parts.append(_flame(240, 18, 1.1))
    parts.append(_smoke(240, 11, 1.0))
    # spiked mine bobbing between the tankers
    parts.append('<circle cx="172" cy="26" r="3.4" fill="#141414"/>')
    for dx, dy in ((-3, -3), (3, -3), (-3, 3), (3, 3), (0, -4.5), (-4.5, 0), (4.5, 0)):
        parts.append(f'<line x1="172" y1="26" x2="{172 + dx}" y2="{26 + dy}" stroke="#141414" stroke-width="1"/>')
    parts.append('<circle cx="170.8" cy="24.8" r="0.8" fill="#fffdf4"/>')
    return "".join(parts)


# ---------------------------------------------------------------------------
# LEAD 3 — Cairo: night highway curving past low city blocks, a tanker
# tipped on its side with tall orange flames, fire crews with a hose
# line, one scorched motorcycle at the kerb.
# ---------------------------------------------------------------------------
def art_cairo():
    parts = []
    parts.append('<rect width="320" height="33" fill="#1d2b4a"/>')
    parts.append('<circle cx="292" cy="7" r="4" fill="#e8e2c8"/>')
    parts.append('<circle cx="60" cy="6" r="1" fill="#fffdf4"/>')
    parts.append('<circle cx="120" cy="4" r="1" fill="#fffdf4"/>')
    parts.append('<circle cx="200" cy="8" r="1" fill="#fffdf4"/>')
    # low city blocks with lit windows, far
    for x, w, h in ((0, 44, 12), (52, 36, 9), (96, 52, 13), (250, 70, 11)):
        parts.append(f'<rect x="{x}" y="{24 - h}" width="{w}" height="{h}" fill="#0f1a30"/>')
        for wx in range(x + 5, x + w - 3, 9):
            parts.append(f'<rect x="{wx}" y="{27 - h}" width="3" height="4" fill="#d8b45a"/>')
    # highway curve
    parts.append('<path d="M0 33 L320 33 L320 26 Q160 22 0 28 Z" fill="#3a3a38"/>')
    parts.append('<path d="M0 30.5 Q160 26 320 29.5" fill="none" stroke="#d8b45a" stroke-width="1" stroke-dasharray="6 5"/>')
    # tipped tanker, centre-left — big, pale, tilted hard
    parts.append('<g transform="rotate(-22 132 21)">')
    parts.append('<rect x="100" y="14" width="62" height="13" rx="6" fill="#c9bd93" stroke="#8a8a86" stroke-width="0.8"/>')
    parts.append('<rect x="100" y="14" width="62" height="4" rx="2" fill="#8a8a86"/>')
    parts.append('<rect x="154" y="16" width="12" height="9" fill="#14264d"/>')
    parts.append('</g>')
    parts.append(_flame(128, 18, 1.6))
    parts.append(_flame(146, 20, 1.2))
    parts.append(_smoke(136, 8, 1.2))
    # fire crew with a hose line, right
    parts.append('<path d="M196 30 Q220 26 246 22" fill="none" stroke="#e8e2c8" stroke-width="1.6"/>')
    parts.append('<path d="M246 22 L238 14" stroke="#7fb3d5" stroke-width="1.6"/>')
    for x in (200, 214):
        parts.append(f'<circle cx="{x}" cy="27" r="3" fill="#c0392b"/>')
        parts.append(f'<rect x="{x - 2}" y="21" width="4" height="5" fill="#c0392b"/>')
        parts.append(f'<circle cx="{x}" cy="19.5" r="2" fill="#d8b45a"/>')
    # scorched motorcycle at the kerb (small detail)
    parts.append('<circle cx="282" cy="30" r="2.4" fill="none" stroke="#141414" stroke-width="1"/>')
    parts.append('<circle cx="292" cy="30" r="2.4" fill="none" stroke="#141414" stroke-width="1"/>')
    parts.append('<line x1="282" y1="30" x2="287" y2="26" stroke="#141414" stroke-width="1"/>')
    parts.append('<line x1="287" y1="26" x2="292" y2="30" stroke="#141414" stroke-width="1"/>')
    return "".join(parts)


# ---------------------------------------------------------------------------
# FEATURE 4 — Ras Tanura: night refinery, round storage tanks and tall
# chimneys, four small drones in the sky, one burst of sparks above a
# tank, tiny crescent moon over the chimneys.
# ---------------------------------------------------------------------------
def art_ras_tanura():
    p = []
    p.append('<rect width="190" height="23" fill="#16233f"/>')
    p.append('<path d="M168 4 A6 6 0 1 0 168 12 A5 5 0 1 1 168 4 Z" fill="#d8b45a"/>')
    p.append('<rect x="0" y="16" width="190" height="7" fill="#0e1830"/>')
    # storage tanks
    for x in (14, 44, 74):
        p.append(f'<rect x="{x}" y="9" width="24" height="14" rx="3" fill="#c9bd93"/>')
        p.append(f'<rect x="{x}" y="9" width="24" height="3" rx="1.5" fill="#8a8a86"/>')
    # chimneys with lit tops
    for x in (112, 128, 144):
        p.append(f'<rect x="{x}" y="4" width="5" height="19" fill="#3a4a6b"/>')
        p.append(f'<rect x="{x}" y="4" width="5" height="2" fill="#e8722a"/>')
    # sparks burst above a tank
    for dx, dy in ((0, -5), (4, -3), (-4, -3), (3, 2), (-3, 2), (0, 3)):
        p.append(f'<line x1="56" y1="7" x2="{56 + dx}" y2="{7 + dy}" stroke="#f5c542" stroke-width="1.1"/>')
    p.append('<circle cx="56" cy="7" r="1.6" fill="#f5c542"/>')
    # four drones
    for cx, cy, s in ((30, 4, 0.7), (80, 3, 0.6), (120, 6, 0.7), (158, 3, 0.6)):
        p.append(_drone(cx, cy, s, "#e8e2c8"))
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 5 — Cartagena: bright yellow supermarket front, police
# officers escorting shoppers out the door, a helicopter overhead,
# one abandoned shopping trolley by the entrance.
# ---------------------------------------------------------------------------
def art_cartagena():
    p = []
    p.append('<rect width="190" height="23" fill="#f7e3cd"/>')
    p.append(_cloud(150, 4, 0.8))
    p.append(_sun(20, 5, 4))
    # helicopter, top right
    p.append('<ellipse cx="160" cy="6" rx="9" ry="3" fill="#14264d"/>')
    p.append('<line x1="148" y1="5" x2="172" y2="5" stroke="#14264d" stroke-width="1"/>')
    p.append('<line x1="169" y1="6" x2="176" y2="9" stroke="#14264d" stroke-width="1"/>')
    p.append('<line x1="160" y1="9" x2="160" y2="12" stroke="#14264d" stroke-width="1"/>')
    # supermarket front
    p.append('<rect x="28" y="8" width="134" height="15" fill="#f5c542"/>')
    p.append('<rect x="28" y="8" width="134" height="4" fill="#b03a7d"/>')
    p.append('<text x="95" y="11.5" font-family="Libre Franklin,sans-serif" font-size="4" font-weight="bold" fill="#fffdf4" text-anchor="middle" letter-spacing="1">ÉXITO</text>')
    p.append('<rect x="88" y="14" width="14" height="9" fill="#14264d"/>')
    for x in (36, 56, 120, 140):
        p.append(f'<rect x="{x}" y="14" width="14" height="7" fill="#bfe3f0"/>')
    # police officer + shoppers walking out
    for cx, col in ((92, "#14264d"), (106, "#1e8a4c"), (118, "#c96a1e")):
        p.append(f'<circle cx="{cx}" cy="16.5" r="1.8" fill="#d8a077"/>')
        p.append(f'<rect x="{cx - 2}" y="18" width="4" height="5" fill="{col}"/>')
    # abandoned trolley by the entrance
    p.append('<rect x="66" y="19" width="9" height="4" fill="none" stroke="#141414" stroke-width="0.9"/>')
    p.append('<circle cx="68" cy="23.5" r="1" fill="#141414"/>')
    p.append('<circle cx="73" cy="23.5" r="1" fill="#141414"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 6 — SpaceX: Earth curve at the bottom, a grid of small
# satellites with solar panels above it, one rocket rising, a tiny
# server rack drawn inside the largest satellite.
# ---------------------------------------------------------------------------
def art_spacex():
    p = []
    p.append('<rect width="190" height="23" fill="#101c38"/>')
    for cx, cy in ((20, 4), (60, 3), (120, 5), (170, 3), (95, 2)):
        p.append(f'<circle cx="{cx}" cy="{cy}" r="0.8" fill="#fffdf4"/>')
    # Earth curve
    p.append('<path d="M0 23 A140 140 0 0 1 190 23 Z" fill="#2a6f97"/>')
    p.append('<path d="M20 23 Q60 12 110 18 T180 16 L190 23 Z" fill="#1e8a4c"/>')
    # satellite grid
    for cx, cy, s in ((30, 8, 0.8), (70, 6, 0.7), (110, 9, 0.8), (150, 7, 0.7), (50, 13, 0.6), (130, 13, 0.6)):
        p.append(f'<rect x="{cx - 5 * s:.1f}" y="{cy - 1.5 * s:.1f}" width="{10 * s:.1f}" height="{3 * s:.1f}" fill="#d8b45a"/>')
        p.append(f'<rect x="{cx - 1.5 * s:.1f}" y="{cy - 2.5 * s:.1f}" width="{3 * s:.1f}" height="{5 * s:.1f}" fill="#fffdf4"/>')
    # largest satellite with a server rack inside
    p.append('<rect x="84" y="4" width="22" height="10" fill="#fffdf4" stroke="#14264d" stroke-width="0.8"/>')
    for y in (6.5, 9, 11.5):
        p.append(f'<line x1="87" y1="{y}" x2="103" y2="{y}" stroke="#14264d" stroke-width="0.8"/>')
    p.append('<rect x="76" y="7" width="8" height="4" fill="#d8b45a"/>')
    p.append('<rect x="106" y="7" width="8" height="4" fill="#d8b45a"/>')
    # rocket rising, right
    p.append('<path d="M168 20 L172 10 L176 20 Z" fill="#fffdf4"/>')
    p.append('<rect x="168" y="18" width="8" height="3" fill="#c0392b"/>')
    p.append('<path d="M172 21 L170 23 L174 23 Z" fill="#e8722a"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 7 — Solomon: small green Pacific island with palm trees, two
# flags on poles (Australia and Solomon Islands), a patrol boat in
# turquoise water, a tiny turtle near the boat.
# ---------------------------------------------------------------------------
def art_solomon():
    p = []
    p.append('<rect width="190" height="23" fill="#bfe3f0"/>')
    p.append(_sun(168, 5, 4))
    p.append(_cloud(30, 4, 0.8))
    # sea
    p.append('<rect x="0" y="14" width="190" height="9" fill="#2a9db5"/>')
    p.append(_wave_row(17, 190, "#fffdf4", 0, 0.5))
    p.append(_wave_row(21, 190, "#fffdf4", -6, 0.4))
    # island
    p.append('<path d="M55 16 Q70 6 95 7 Q120 8 132 16 Z" fill="#5da24a"/>')
    p.append('<path d="M60 16 Q95 12 130 16 L132 16 L55 16 Z" fill="#e8d9b8"/>')
    # two palm trees
    for cx in (78, 104):
        p.append(f'<line x1="{cx}" y1="13" x2="{cx + 2}" y2="5" stroke="#6b4a2a" stroke-width="1.4"/>')
        for dx, dy in ((-5, -2), (5, -2), (-3, -4), (4, -3)):
            p.append(f'<path d="M{cx + 2} 5 q{dx} {dy} {dx * 1.6:.1f} {dy + 2}" fill="none" stroke="#1e8a4c" stroke-width="1.2"/>')
    # two flags: Australia (blue, stars) and Solomon Islands (blue/green)
    p.append('<line x1="88" y1="12" x2="88" y2="2" stroke="#141414" stroke-width="0.9"/>')
    p.append('<rect x="88" y="2" width="9" height="5" fill="#1f5fa8"/>')
    p.append('<circle cx="92" cy="4.5" r="0.8" fill="#fffdf4"/>')
    p.append('<line x1="112" y1="12" x2="112" y2="2" stroke="#141414" stroke-width="0.9"/>')
    p.append('<rect x="112" y="2" width="9" height="5" fill="#1e8a4c"/>')
    p.append('<polygon points="112,2 121,2 112,7" fill="#1f5fa8"/>')
    p.append('<circle cx="114" cy="3.5" r="0.7" fill="#f5c542"/>')
    # patrol boat
    p.append('<path d="M140 17 L142 13 L168 13 L170 17 Z" fill="#fffdf4"/>')
    p.append('<rect x="150" y="9" width="8" height="4" fill="#14264d"/>')
    p.append('<line x1="138" y1="17.5" x2="172" y2="17.5" stroke="#fffdf4" stroke-width="0.8" opacity="0.7"/>')
    # tiny turtle near the boat
    p.append('<ellipse cx="128" cy="20" rx="3" ry="1.8" fill="#1e8a4c"/>')
    p.append('<circle cx="131.5" cy="19.5" r="1" fill="#1e8a4c"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 8 — Canary: deep-blue Atlantic, a crowded wooden cayuco boat,
# an orange rescue vessel alongside, the small volcanic island behind,
# a red emergency blanket on the rescue deck.
# ---------------------------------------------------------------------------
def art_canary():
    p = []
    p.append('<rect width="190" height="23" fill="#1d4e7a"/>')
    p.append(_cloud(150, 4, 0.8))
    # volcanic island behind, left
    p.append('<polygon points="0,14 18,4 34,14" fill="#5c5540"/>')
    p.append('<polygon points="14,7 22,7 18,4" fill="#fffdf4"/>')
    p.append(_wave_row(12, 190, "#fffdf4", 0, 0.35))
    p.append(_wave_row(19, 190, "#fffdf4", -8, 0.45))
    # crowded wooden cayuco boat
    p.append('<path d="M52 16 L56 12 L118 12 L124 16 L120 19 L58 19 Z" fill="#8a6a3a"/>')
    p.append('<rect x="56" y="12" width="62" height="1.6" fill="#6b4a2a"/>')
    for cx in (62, 72, 82, 92, 102, 112):
        p.append(f'<circle cx="{cx}" cy="10.5" r="1.7" fill="#d8a077"/>')
        p.append(f'<rect x="{cx - 2}" y="11.5" width="4" height="2" fill="#c0392b"/>')
    # orange rescue vessel alongside
    p.append('<path d="M132 15 L135 10 L176 10 L180 15 L176 18 L136 18 Z" fill="#e8722a"/>')
    p.append('<rect x="146" y="5" width="14" height="5" fill="#fffdf4"/>')
    p.append('<rect x="146" y="5" width="14" height="1.4" fill="#14264d"/>')
    p.append('<circle cx="150" cy="3.5" r="1.4" fill="#fffdf4"/>')
    # red emergency blanket on the rescue deck
    p.append('<rect x="162" y="11" width="10" height="3" fill="#c0392b"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 9 — Poland: border landscape, a line of pine trees, a fighter
# jet above a dashed red boundary line, a radar station with a turning
# dish, a tiny AWACS plane with a dome on its back.
# ---------------------------------------------------------------------------
def art_poland():
    p = []
    p.append('<rect width="190" height="23" fill="#d9e7f6"/>')
    p.append(_sun(170, 5, 4))
    p.append(_cloud(40, 4, 0.9))
    # ground + pine trees
    p.append('<rect x="0" y="17" width="190" height="6" fill="#7a9a5c"/>')
    for cx in (14, 26, 38, 52, 66):
        p.append(f'<polygon points="{cx},8 {cx - 4},17 {cx + 4},17" fill="#1e8a4c"/>')
        p.append(f'<rect x="{cx - 1}" y="17" width="2" height="2" fill="#6b4a2a"/>')
    # dashed red boundary line
    p.append('<line x1="86" y1="19" x2="190" y2="19" stroke="#a31621" stroke-width="1.4" stroke-dasharray="5 3"/>')
    # radar station, right
    p.append('<rect x="150" y="13" width="16" height="10" fill="#8a8a86"/>')
    p.append('<line x1="158" y1="13" x2="158" y2="8" stroke="#14264d" stroke-width="1.2"/>')
    p.append('<path d="M152 8 A7 7 0 0 1 164 8 Z" fill="#14264d"/>')
    p.append('<circle cx="158" cy="9" r="1" fill="#d8b45a"/>')
    # fighter jet above the line
    p.append('<polygon points="92,6 118,8 92,10" fill="#14264d"/>')
    p.append('<polygon points="100,6 106,3 108,6" fill="#14264d"/>')
    p.append('<polygon points="100,10 106,13 108,10" fill="#14264d"/>')
    p.append('<line x1="92" y1="8" x2="84" y2="8" stroke="#e8722a" stroke-width="1.2"/>')
    # tiny AWACS with a dome, far left sky
    p.append('<ellipse cx="120" cy="4" rx="7" ry="1.8" fill="#fffdf4"/>')
    p.append('<path d="M116 3 A4 4 0 0 1 124 3 Z" fill="#14264d"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 10 — Netanyahu: Jerusalem court building with tall columns, a
# gavel resting on a stack of papers, the Knesset dome behind, a tiny
# scale of justice on the top step.
# ---------------------------------------------------------------------------
def art_netanyahu():
    p = []
    p.append('<rect width="190" height="23" fill="#e9e2c8"/>')
    p.append(_sun(18, 5, 4))
    p.append(_cloud(140, 4, 0.8))
    # Knesset dome behind, right
    p.append('<rect x="140" y="10" width="34" height="13" fill="#c9bd93"/>')
    p.append('<path d="M140 10 Q157 0 174 10 Z" fill="#c9bd93"/>')
    # court building, centre-left
    p.append('<rect x="30" y="8" width="96" height="15" fill="#fffdf4" stroke="#14264d" stroke-width="0.8"/>')
    p.append('<polygon points="28,8 78,2 128,8" fill="#14264d"/>')
    for x in (38, 56, 74, 92, 110):
        p.append(f'<rect x="{x}" y="10" width="4" height="11" fill="#14264d"/>')
    p.append('<rect x="72" y="16" width="12" height="7" fill="#14264d"/>')
    # steps
    p.append('<rect x="24" y="23" width="108" height="0" fill="#14264d"/>')
    # tiny scale of justice on the top step
    p.append('<line x1="52" y1="8" x2="52" y2="4" stroke="#a31621" stroke-width="0.8"/>')
    p.append('<line x1="48" y1="5" x2="56" y2="5" stroke="#a31621" stroke-width="0.8"/>')
    p.append('<path d="M46.5 5 L48 7.5 L49.5 5 Z" fill="#a31621"/>')
    p.append('<path d="M54.5 5 L56 7.5 L57.5 5 Z" fill="#a31621"/>')
    # gavel on a stack of papers, foreground right
    p.append('<rect x="132" y="20" width="18" height="3" fill="#fffdf4" stroke="#14264d" stroke-width="0.6"/>')
    p.append('<rect x="134" y="17.5" width="14" height="2.5" fill="#fffdf4" stroke="#14264d" stroke-width="0.6"/>')
    p.append('<rect x="138" y="13" width="12" height="3" rx="1" fill="#6b4a2a" transform="rotate(-18 144 14.5)"/>')
    p.append('<line x1="144" y1="15" x2="152" y2="19" stroke="#6b4a2a" stroke-width="1.6"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 11 — Ramaphosa: Cape Town court with a green roof, a sofa with
# banknotes peeking from a cushion, a judge's bench behind, a tiny farm
# windmill on the horizon.
# ---------------------------------------------------------------------------
def art_ramaphosa():
    p = []
    p.append('<rect width="190" height="23" fill="#d8ecdf"/>')
    p.append(_sun(170, 5, 4))
    p.append(_cloud(30, 4, 0.8))
    # windmill on the horizon (small detail)
    p.append('<line x1="22" y1="16" x2="22" y2="8" stroke="#6b4a2a" stroke-width="1"/>')
    p.append('<line x1="18" y1="8" x2="26" y2="8" stroke="#6b4a2a" stroke-width="0.8"/>')
    p.append('<line x1="22" y1="4" x2="22" y2="12" stroke="#6b4a2a" stroke-width="0.8"/>')
    p.append('<line x1="19" y1="7" x2="25" y2="9" stroke="#6b4a2a" stroke-width="0.8"/>')
    # court with green roof
    p.append('<rect x="60" y="10" width="80" height="13" fill="#fffdf4" stroke="#14264d" stroke-width="0.8"/>')
    p.append('<polygon points="56,10 100,3 144,10" fill="#1e8a4c"/>')
    for x in (68, 86, 104, 122):
        p.append(f'<rect x="{x}" y="13" width="5" height="10" fill="#14264d"/>')
    # judge's bench behind the sofa
    p.append('<rect x="150" y="14" width="28" height="9" fill="#6b4a2a"/>')
    p.append('<rect x="150" y="14" width="28" height="2" fill="#d8b45a"/>')
    # sofa with banknotes peeking from a cushion, foreground
    p.append('<rect x="78" y="17" width="34" height="6" rx="2" fill="#c0392b"/>')
    p.append('<rect x="78" y="13" width="8" height="6" rx="2" fill="#c0392b"/>')
    p.append('<rect x="104" y="13" width="8" height="6" rx="2" fill="#c0392b"/>')
    p.append('<rect x="88" y="14" width="7" height="5" fill="#1e8a4c" transform="rotate(-12 91 16)"/>')
    p.append('<rect x="96" y="15" width="7" height="5" fill="#1e8a4c" transform="rotate(10 99 17)"/>')
    p.append('<circle cx="91" cy="16.5" r="1" fill="#fffdf4"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 12 — Gaza: Gaza City seafront at dusk, apartment blocks along
# the beach, a plume of grey smoke from one building, a fishing boat on
# the water, a tiny laundry line on a rooftop.
# ---------------------------------------------------------------------------
def art_gaza():
    p = []
    p.append('<rect width="190" height="23" fill="#e8c9a8"/>')
    p.append(_sun(24, 6, 4.5, fill="#e8722a"))
    p.append(_cloud(120, 4, 0.8))
    # apartment blocks
    for x, w, h in ((30, 26, 12), (60, 22, 15), (86, 26, 11), (116, 24, 13)):
        p.append(f'<rect x="{x}" y="{18 - h}" width="{w}" height="{h}" fill="#8a7a5c"/>')
        for wx in range(x + 3, x + w - 3, 7):
            for wy in range(18 - h + 2, 17, 5):
                p.append(f'<rect x="{wx}" y="{wy}" width="2.5" height="3" fill="#d8b45a"/>')
    # laundry line on a rooftop (small detail)
    p.append('<line x1="62" y1="3" x2="80" y2="3" stroke="#141414" stroke-width="0.7"/>')
    for cx, c in ((66, "#fffdf4"), (71, "#1f5fa8"), (76, "#c0392b")):
        p.append(f'<rect x="{cx}" y="3" width="3" height="3.5" fill="{c}"/>')
    # smoke plume from one building
    p.append(_smoke(96, 4, 0.9))
    # beach + sea
    p.append('<rect x="0" y="18" width="190" height="5" fill="#e8d9b8"/>')
    p.append(_wave_row(21, 190, "#fffdf4", 0, 0.5))
    # fishing boat
    p.append('<path d="M150 19 L153 15 L172 15 L175 19 Z" fill="#14264d"/>')
    p.append('<line x1="162" y1="15" x2="162" y2="9" stroke="#14264d" stroke-width="1"/>')
    p.append('<polygon points="162,9 162,14 169,14" fill="#fffdf4"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# FEATURE 13 — Sudan: Blue Nile river town, low houses with flat roofs,
# two small drones in a hazy sky, a red-cross tent at the edge, a tiny
# water jug left on a doorstep.
# ---------------------------------------------------------------------------
def art_sudan():
    p = []
    p.append('<rect width="190" height="23" fill="#f2ddc0"/>')
    p.append(_sun(170, 5, 4))
    p.append(_cloud(60, 4, 0.8))
    # river, middle band
    p.append('<rect x="0" y="14" width="190" height="9" fill="#7fa8b8"/>')
    p.append(_wave_row(18, 190, "#fffdf4", 0, 0.5))
    # low flat-roof houses, far bank
    for x, w, h in ((10, 30, 7), (46, 24, 9), (76, 28, 6), (110, 26, 8)):
        p.append(f'<rect x="{x}" y="{14 - h}" width="{w}" height="{h}" fill="#c9a25e"/>')
        p.append(f'<rect x="{x + 4}" y="{16 - h}" width="4" height="5" fill="#14264d"/>')
    # red-cross tent at the edge, foreground
    p.append('<polygon points="150,23 150,13 168,8 186,13 186,23" fill="#fffdf4" stroke="#c0392b" stroke-width="0.8"/>')
    p.append('<rect x="166" y="13" width="4" height="8" fill="#c0392b"/>')
    p.append('<rect x="163" y="15" width="10" height="3.5" fill="#c0392b"/>')
    # two drones in a hazy sky
    p.append(_drone(50, 4, 0.7))
    p.append(_drone(120, 3, 0.6))
    # tiny water jug on a doorstep (small detail)
    p.append('<path d="M44 21 q-2 -3 0 -5 q2 -2 4 0 q2 2 0 5 Z" fill="#1f5fa8"/>')
    p.append('<rect x="43" y="20" width="6" height="2" fill="#1f5fa8"/>')
    return "".join(p)


# ---------------------------------------------------------------------------
# Wrapper: scene SVG with the stat ribbon at the bottom (pandya's device).
# ---------------------------------------------------------------------------
ART = {
    1: art_tariffs, 2: art_hormuz, 3: art_cairo, 4: art_ras_tanura,
    5: art_cartagena, 6: art_spacex, 7: art_solomon, 8: art_canary,
    9: art_poland, 10: art_netanyahu, 11: art_ramaphosa, 12: art_gaza,
    13: art_sudan,
}


def scene_svg(n, reg, stat, label, lead, regions, tints):
    if lead:
        w, h, art_h, rib_h = 320, 56, 33, 23
        stat_fs, lab_fs = 19, 9
    else:
        w, h, art_h, rib_h = 190, 40, 23, 17
        stat_fs, lab_fs = 13, 7
    col = regions[reg][1]
    art = ART[n]()
    ribbon = (
        f'<rect x="0" y="{art_h}" width="{w}" height="{rib_h}" fill="{col}"/>'
        f'<text x="8" y="{art_h + rib_h - 6}" font-family="Oswald,sans-serif" '
        f'font-size="{stat_fs}" font-weight="600" fill="#fffdf4">{_esc(stat)}</text>'
        f'<text x="{w - 8}" y="{art_h + rib_h - 6}" font-family="Libre Franklin,sans-serif" '
        f'font-size="{lab_fs}" font-weight="bold" fill="#fffdf4" text-anchor="end" '
        f'letter-spacing="1">{_esc(label)}</text>'
    )
    return (f'<svg class="scene" viewBox="0 0 {w} {h}" preserveAspectRatio="none">'
            f'<rect width="{w}" height="{art_h}" fill="{tints[reg]}"/>'
            f'{art}{ribbon}</svg>')
