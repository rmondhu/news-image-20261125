#!/usr/bin/env python3
"""Build render.html for news-image-20261125 — THE WORLD TODAY,
Wednesday 25 November 2026.

Design: the winner system from the 24 Nov edition (DESIGN.md) — navy
header band with gold kicker, red headline strip, region colour system
(8 colours used in chips, stat ribbons, kickers, map badges, legend),
every story in a neat 1px frame, a flat vector scene drawn in code with
a stat ribbon inside it on each of the 13 top cards, a real world map
(tools/land.svg, built by tools/gen_map.py from Natural Earth data),
19 numbered briefs in 3 columns, red DATE CHECK footer + navy sources
strip. Three Google Fonts (SIL OFL 1.1) as local woff2 in fonts/.

Content: the 32 stories in news.md (3 leads + 10 features + 19 briefs),
all events of Wednesday 25 November 2026. Verification pills are set
honestly from sourcing: OFFICIAL = on the record (court, government,
institution); CONFIRMED = 2+ outlets; REPORTED = one outlet's report;
CLAIM = one side's word only.

Run from the entry directory:  python3 tools/gen_entry.py
Writes: render.html
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / "tools"))
from scenes import scene_svg as _scene_svg  # noqa: E402

REGIONS = {
    "ME": ("MIDDLE EAST", "#c96a1e"),
    "EUR": ("EUROPE", "#1f5fa8"),
    "AFR": ("AFRICA", "#c0392b"),
    "ASIA": ("ASIA", "#1e8a4c"),
    "NAM": ("N. AMERICA", "#6a4fa3"),
    "SAM": ("S. AMERICA", "#b03a7d"),
    "OCE": ("OCEANIA", "#0e7d8c"),
    "WLD": ("WORLD & SPACE", "#14264d"),
}

STATUS = {
    "OFFICIAL": "#1e7a46",
    "CONFIRMED": "#1f5fa8",
    "REPORTED": "#a31621",
    "CLAIM": "#b7791f",
}

TINTS = {
    "ME": "#f7e3cd", "EUR": "#d9e7f6", "AFR": "#f6dbd5", "ASIA": "#d8ecdf",
    "NAM": "#e5ddf2", "SAM": "#f3dbe9", "OCE": "#d3e9ec", "WLD": "#dde3f0",
}

# (n, region, kicker, headline, body, lat, lon, badge_x, badge_y,
#  stat, stat_label, status, source)
LEADS = [
    (1, "NAM", "TARIFFS — LEAD",
     "Trump proposes tariffs on 14 economies — China up to ~45%",
     "Trump proposes duties on 14 economies after a Section 301 probe; "
     "China faces up to ~45% combined.",
     38.9, -77.0, 262, 26, "14", "ECONOMIES · CHINA ~45%", "OFFICIAL", "Reuters"),
    (2, "ME", "HORMUZ — LEAD",
     "Two tankers hit by mines in the Strait of Hormuz",
     "Tehran says two tankers hit mines; the maritime centre says the "
     "mine claims are unconfirmed.",
     26.5, 56.3, 668, 40, "2", "TANKERS HIT BY MINES", "CLAIM", "IRGC · JMIC"),
    (3, "AFR", "CAIRO — LEAD",
     "Cairo tanker fire kills 31 after crash on ring road",
     "A tanker overturns and ignites on Cairo's ring road, killing 31 "
     "and injuring 21 in Al-Warraq.",
     30.0, 31.2, 556, 66, "31", "KILLED · 21 INJURED", "CONFIRMED", "AP"),
]

GRID = [
    (4, "ME", "RAS TANURA", "Houthis say they hit Ras Tanura refinery",
     "Coalition says four drones were intercepted over Ras Tanura.",
     26.6, 50.2, 640, 78, "4", "DRONES INTERCEPTED", "CLAIM", "Reuters"),
    (5, "SAM", "CARTAGENA", "Cartagena siege ends: all 76 hostages freed",
     "Forces storm the supermarket after 17 hours; one captor is killed.",
     10.4, -75.5, 262, 84, "76", "HOSTAGES FREED", "REPORTED", "One Turn"),
    (6, "WLD", "SPACEX", "FCC lets SpaceX deploy a million satellites",
     "First such authorisation in US history; first launch due by 2033.",
     28.4, -80.6, 250, 62, "1M", "SATELLITES AUTHORISED", "OFFICIAL", "FCC"),
    (7, "OCE", "SOLOMON", "Australia signs Solomons security treaty",
     "Treaty would bar a foreign military base; the 2022 China pact will "
     "not be renewed.",
     -9.6, 160.2, 916, 116, "1 TREATY", "NO FOREIGN BASE", "CONFIRMED", "NYT"),
    (8, "EUR", "CANARY", "Record 2,100 migrants reach Canary Islands",
     "Highest single-day total on record; most land on El Hierro.",
     27.7, -18.0, 420, 70, "2,100", "ARRIVALS IN 24 HOURS", "CONFIRMED", "Reuters"),
    (9, "EUR", "POLAND", "Poland plans no-fly zone on eastern border",
     "Strip of 12–50 km to ease shooting down Russian missiles and drones.",
     52.2, 23.0, 580, 10, "12–50 KM", "NO-FLY STRIP PLANNED", "OFFICIAL", "Reuters"),
    (10, "ME", "NETANYAHU", "Judges urge dropping Netanyahu bribery case",
     "Knesset votes 65–50 for an independent inquiry into 7 October.",
     31.8, 35.2, 600, 28, "65–50", "VOTE FOR OCT 7 INQUIRY", "CONFIRMED", "CNN"),
    (11, "AFR", "RAMAPHOSA", "Court throws out Ramaphosa farm-cash report",
     "Panel exceeded its mandate, judges rule; the impeachment inquiry "
     "falls away.",
     -33.9, 18.4, 520, 116, "$580,000", "CASH IN THE CASE", "OFFICIAL", "Sowetan"),
    (12, "ME", "GAZA", "Israel kills Hamas security chief in Gaza",
     "Abuelouf dies with his wife and two children in a strike on Gaza City.",
     31.5, 34.45, 566, 30, "4", "KILLED IN THE STRIKE", "REPORTED", "Reuters"),
    (13, "AFR", "SUDAN", "RSF drone strikes kill 19 civilians in Sudan",
     "Rights group counts 19 dead in Damazin and five wounded in Roseires.",
     11.8, 34.35, 610, 88, "19", "KILLED · 20 WOUNDED", "REPORTED", "Reuters"),
    (14, "EUR", "KYIV", "Missiles hit Kyiv shopping centre",
     "Strikes hit a shopping centre and two other buildings, the mayor says.",
     50.45, 30.5, 548, 14, "", "", "REPORTED", "Reuters"),
    (15, "EUR", "UKRAINE", "Drones 'hit two Rosneft refineries'",
     "Syzran and Kuibyshev ablaze; one killed, 145 drones downed, Russia says.",
     53.2, 50.2, 660, 14, "", "", "REPORTED", "One Turn"),
    (16, "AFR", "LIBYA", "Army vows revenge after Ukraine drone hit",
     "A Ukrainian drone hit a Russian warship; two Libyan officers died.",
     32.1, 20.1, 528, 66, "", "", "REPORTED", "AP"),
    (17, "EUR", "MERZ", "Russia 'wants more than Ukraine', Merz warns",
     "Merz defends higher defence spending and continued aid to Kyiv.",
     52.5, 13.4, 500, 12, "", "", "OFFICIAL", "Reuters"),
    (18, "ASIA", "N. KOREA", "Pyongyang expels Swiss envoy in 48 hours",
     "Swiss envoy ordered out after sanctions over a children's camp.",
     39.0, 125.75, 856, 26, "", "", "OFFICIAL", "Reuters"),
    (19, "ASIA", "CHINA", "Shanghai party chief Chen Jining probed",
     "Fourth sitting Politburo member probed in just over a year.",
     31.2, 121.5, 836, 66, "", "", "OFFICIAL", "Reuters"),
    (20, "EUR", "SPAIN", "Snap election called for Sunday 29 Nov",
     "Final polls put the PP on 31.5% and the Socialists on 29%.",
     40.4, -3.7, 452, 52, "", "", "REPORTED", "One Turn"),
    (21, "ASIA", "BOGOR", "Mine toll rises to nine; 17 still trapped",
     "Rescuers pump water from a flooded gold mine shaft 100 m deep.",
     -6.6, 106.8, 800, 110, "", "", "CONFIRMED", "AP"),
    (22, "AFR", "NIGERIA", "Militants kill at least 30 in Niger state",
     "Residents describe the assault as retaliation for US strikes.",
     9.5, 6.5, 488, 88, "", "", "REPORTED", "Reuters"),
    (23, "ASIA", "BANGLADESH", "Garment wage up 36% to 17,000 taka",
     "Workers demanded up to 30,000 taka after weeks of protests.",
     23.8, 90.4, 716, 74, "", "", "OFFICIAL", "Reuters"),
    (24, "SAM", "ARGENTINA", "Argentina enters technical recession",
     "Activity fell 1.8% in Q3, the second straight contraction.",
     -34.6, -58.4, 360, 130, "", "", "OFFICIAL", "AFP"),
    (25, "EUR", "POUNDLAND", "Poundland collapses; 11,000 jobs at risk",
     "Chain fails to find a buyer before the deadline; ~600 stores.",
     51.5, -0.1, 452, 14, "", "", "REPORTED", "PA"),
    (26, "AFR", "DR CONGO", "10 Ebola workers evacuated amid fighting",
     "Staff sheltered three days in a hospital maternity ward in Akwe.",
     1.8, 30.0, 556, 92, "", "", "CONFIRMED", "Reuters"),
    (27, "ME", "SYRIA", "IS attack kills two security staff in Hasaka",
     "Five others wounded in the north-eastern city, state TV reports.",
     36.5, 40.75, 626, 30, "", "", "REPORTED", "Reuters"),
    (28, "WLD", "SPACE", "Shenzhou-24 docks; Pakistan's first astronaut",
     "Zeeshan Ali is the first foreign astronaut aboard Tiangong.",
     39.9, 116.4, 786, 24, "", "", "OFFICIAL", "Reuters"),
    (29, "NAM", "DELL", "Dell revenue $54.9bn, up 103% on AI demand",
     "AI server revenue $22.0bn, up 291% in the third quarter.",
     30.3, -97.7, 205, 62, "", "", "REPORTED", "One Turn"),
    (30, "NAM", "USA", "US inflation at 3.8% in October",
     "Consumer confidence jumps to its highest in nearly two years.",
     38.9, -77.0, 300, 28, "", "", "REPORTED", "AP"),
    (31, "NAM", "MACY'S", "Macy's parade postponed by storm winds",
     "First postponement ever; New Jersey declares a state of emergency.",
     40.7, -74.0, 312, 48, "", "", "CONFIRMED", "AP"),
    (32, "EUR", "SPORT", "Lille stun Bayern 2-1; Liverpool win 3-0",
     "Barcelona beat Sabah 4-1; PSG draw 2-2 with Roma.",
     50.6, 3.06, 470, 38, "", "", "CONFIRMED", "UEFA"),
]

FEATURES = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# ALSO TODAY items (checked, from the same day's reporting in news.md).
ALSO = [
    ("S&P 500 slips 0.25%; Brent $90.82", "One Turn"),
    ("Boehly group clinches Lukoil assets", "Dow Jones"),
]


def project(lat, lon):
    """Equirectangular: lon -180..180 -> x 0..984; lat 75..-52 -> y 0..144."""
    return (round((lon + 180.0) / 360.0 * 984.0, 1),
            round((75.0 - lat) / 127.0 * 144.0, 1))


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def scene(n, reg, stat, label, lead):
    return _scene_svg(n, reg, stat, label, lead, REGIONS, TINTS)


def card_html(row, lead):
    n, reg, kick, head, body = row[0], row[1], row[2], row[3], row[4]
    stat, label, status, src = row[9], row[10], row[11], row[12]
    col = REGIONS[reg][1]
    scol = STATUS[status]
    cls = "lead-card" if lead else "feat-card"
    tag = "h2" if lead else "h4"
    return (
        f'<article class="card {cls}">{scene(n, reg, stat, label, lead)}'
        f'<div class="kickrow"><span class="num" style="background:{col}">{n}</span>'
        f'<span class="loc" style="color:{col}">{esc(kick)}</span>'
        f'<span class="pill" style="border-color:{scol};color:{scol}">{status}</span></div>'
        f'<{tag}>{esc(head)}</{tag}><p>{esc(body)}</p>'
        f'<div class="src">{esc(src)}</div></article>'
    )


def main():
    land = (HERE / "tools" / "land.svg").read_text()
    stories = {r[0]: r for r in GRID}
    counts = {}
    for r in LEADS + GRID:
        counts[r[1]] = counts.get(r[1], 0) + 1

    # --- map dots + numbered badges, coloured by region ---
    dots, badges = [], []
    for r in LEADS + GRID:
        n, reg = r[0], r[1]
        ax, ay = project(r[5], r[6])
        bx, by = r[7], r[8]
        col = REGIONS[reg][1]
        dots.append(
            f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{col}" stroke-width="1"/>'
            f'<circle cx="{ax}" cy="{ay}" r="2.4" fill="{col}"/>')
        badges.append(
            f'<g font-family="Libre Franklin,DejaVu Sans,sans-serif" font-size="9.5" '
            f'font-weight="bold" text-anchor="middle">'
            f'<circle cx="{bx}" cy="{by}" r="7.5" fill="{col}" stroke="#fff" '
            f'stroke-width="1.4"/><text x="{bx}" y="{by + 3.5}" fill="#fff">{n}</text></g>')

    lead_html = [card_html(r, True) for r in LEADS]
    feat_html = [card_html(stories[n], False) for n in FEATURES]

    # --- also list: remaining grid stories (one line each) + ALSO TODAY ---
    briefs = []
    for r in GRID:
        if r[0] in FEATURES:
            continue
        n, reg, kick, head = r[0], r[1], r[2], r[3]
        col = REGIONS[reg][1]
        briefs.append(
            f'<div class="brief"><span class="num" style="background:{col}">{n}</span>'
            f'<span class="bt"><b>{esc(kick)}:</b> {esc(head)}</span>'
            f'<span class="bs">{esc(r[12])}</span></div>')
    for head, src in ALSO:
        briefs.append(
            f'<div class="brief"><span class="num" style="background:#a31621">\u2605</span>'
            f'<span class="bt"><b>ALSO TODAY:</b> {esc(head)}</span>'
            f'<span class="bs">{esc(src)}</span></div>')
    cols, per = [], 7
    for i in range(0, len(briefs), per):
        cols.append('<div class="bcol">' + "".join(briefs[i:i + per]) + "</div>")

    chips = "".join(
        f'<span class="chip" style="background:{REGIONS[r][1]}">'
        f'{REGIONS[r][0]} {counts[r]}</span>'
        for r in ["ME", "EUR", "AFR", "ASIA", "NAM", "SAM", "OCE", "WLD"])
    legend = "".join(
        f'<span class="lg"><i style="background:{REGIONS[r][1]}"></i>'
        f'{REGIONS[r][0]} {counts[r]}</span>'
        for r in ["ME", "EUR", "AFR", "ASIA", "NAM", "SAM", "OCE", "WLD"])

    css = """/* Design tokens — winner system, see DESIGN.md. */
/* Fonts: Playfair Display + Libre Franklin + Oswald, Google Fonts, SIL OFL 1.1
   (free for commercial use), downloaded locally into fonts/ — no network. */
@font-face{font-family:"Playfair Display";font-style:normal;font-weight:700 900;font-display:swap;src:url(fonts/PlayfairDisplay-700.woff2) format("woff2")}
@font-face{font-family:"Libre Franklin";font-style:normal;font-weight:400 700;font-display:swap;src:url(fonts/LibreFranklin-400.woff2) format("woff2")}
@font-face{font-family:"Oswald";font-style:normal;font-weight:500 700;font-display:swap;src:url(fonts/Oswald-600.woff2) format("woff2")}
:root{
  --paper:#f7f1de; --ink:#141414; --body:#262626; --muted:#5c5540;
  --accent:#a31621; --navy:#14264d; --gold:#d8b45a; --card:#fffdf4;
  --frame:#d8cfb0; --hairline:#cfc7a4; --land:#c9bd93; --mapbg:#ece5cb;
  --serif:"Playfair Display","Liberation Serif","DejaVu Serif",serif;
  --sans:"Libre Franklin","Liberation Sans","DejaVu Sans",sans-serif;
  --cond:"Oswald","Liberation Sans","DejaVu Sans",sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1024px;height:1024px;background:var(--paper);color:var(--ink);font-family:var(--sans);overflow:hidden}
.page{width:1024px;height:1024px;padding:0 20px;display:flex;flex-direction:column}
.head{margin:0 -20px;background:var(--navy);color:#fff;padding:6px 20px 7px;border-bottom:3px solid var(--gold);text-align:center}
.head .top{display:flex;justify-content:space-between;font-size:10px;letter-spacing:2.5px;font-weight:bold}
.head .top .l{color:var(--gold)}
.head h1{font-family:var(--serif);font-size:48px;line-height:1;font-weight:900;letter-spacing:2px;margin-top:3px}
.strip{padding:5px 0 4px;text-align:center;border-bottom:1px solid var(--hairline);
  font-family:var(--serif);font-size:13px;font-weight:bold;color:var(--accent)}
.strip i{font-style:normal;color:var(--ink);padding:0 6px}
.chips{display:flex;gap:6px;padding:5px 0 6px}
.chip{flex:1;text-align:center;color:#fff;font-size:9px;font-weight:bold;letter-spacing:1px;padding:3px 0}
.leads{display:flex;gap:10px;margin-bottom:8px}
.feats{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:8px}
.card{background:var(--card);border:1px solid var(--frame);display:flex;flex-direction:column;overflow:hidden}
.lead-card{flex:1}
.scene{display:block;width:100%;height:auto}
.kickrow{display:flex;align-items:center;gap:6px;padding:7px 9px 0}
.num{width:16px;height:16px;border-radius:50%;color:#fff;font-size:9.5px;font-weight:bold;text-align:center;line-height:16px;flex:none}
.feat-card .num{width:14px;height:14px;font-size:8.5px;line-height:14px}
.loc{font-size:9px;font-weight:bold;letter-spacing:1.5px}
.feat-card .loc{font-size:8px}
.pill{margin-left:auto;font-size:7.5px;font-weight:bold;letter-spacing:1px;padding:2px 5px;border:1.5px solid}
.lead-card h2{font-family:var(--serif);font-size:15.5px;line-height:1.18;font-weight:bold;padding:5px 9px 0;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.lead-card p{font-size:10.5px;line-height:1.35;color:var(--body);padding:4px 9px 0;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.feat-card h4{font-family:var(--serif);font-size:11px;line-height:1.2;font-weight:bold;padding:5px 8px 0;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.feat-card p{font-size:9px;line-height:1.3;color:var(--body);padding:3px 8px 0;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.src{font-size:8px;color:var(--muted);letter-spacing:.5px;padding:5px 9px 8px;margin-top:auto}
.feat-card .src{font-size:7.5px;padding:4px 8px 7px}
.seclab{display:flex;align-items:center;gap:10px;font-size:10.5px;font-weight:bold;letter-spacing:3px;margin:0 0 5px}
.seclab::before,.seclab::after{content:"";flex:1;border-top:2px solid var(--ink)}
.map{border:1px solid var(--frame);background:var(--card);padding:5px 10px 5px;margin-bottom:6px}
.map h3{font-size:10.5px;letter-spacing:2.5px;text-align:center;margin-bottom:4px;font-weight:bold}
.map h3 span{color:var(--accent)}
.map .legend{display:flex;justify-content:center;gap:12px;margin-top:4px;font-size:8.5px;font-weight:bold;letter-spacing:1px;color:var(--body)}
.map .legend .lg i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px}
.also{flex:1;min-height:0;display:flex;flex-direction:column}
.briefs{display:flex;gap:16px;flex:1}
.bcol{flex:1;min-width:0;display:flex;flex-direction:column;justify-content:space-between}
.brief{display:flex;align-items:baseline;gap:6px;padding:1.5px 0;border-bottom:1px solid #e2dcc0}
.brief .num{width:15px;height:15px;font-size:8.5px;line-height:15px}
.brief .bt{font-size:9.3px;line-height:1.25;color:var(--body);min-width:0}
.brief .bt b{color:var(--ink)}
.brief .bs{margin-left:auto;font-size:8px;color:var(--muted);white-space:nowrap}
.foot{margin:0 -20px}
.datecheck{background:var(--accent);color:#fff;display:flex;gap:10px;align-items:flex-start;
  padding:6px 20px;font-size:9.5px;line-height:1.35}
.datecheck b{font-family:var(--cond);font-size:11px;letter-spacing:2px;white-space:nowrap;padding-top:1px}
.datecheck .how{margin-left:auto;text-align:right;font-size:8.5px;white-space:nowrap}
.datecheck .how i{font-style:normal;border:1.5px solid #fff;padding:1px 4px;margin-left:3px;font-size:7.5px;font-weight:bold}
.srcs{background:var(--navy);color:#fff;text-align:center;font-size:9px;letter-spacing:1px;padding:5px 20px}"""

    map_svg = (
        '<svg width="964" height="126" viewBox="0 0 984 144" preserveAspectRatio="xMidYMid meet">\n'
        '<rect width="984" height="144" fill="#e9e2c8"/>\n' + land + "\n"
        '<line x1="0" y1="85.0" x2="984" y2="85.0" stroke="#b7ab7d" stroke-width="0.5" stroke-dasharray="3 4"/>\n'
        '<line x1="0" y1="58.5" x2="984" y2="58.5" stroke="#b7ab7d" stroke-width="0.5" stroke-dasharray="3 4"/>\n'
        '<line x1="0" y1="111.6" x2="984" y2="111.6" stroke="#b7ab7d" stroke-width="0.5" stroke-dasharray="3 4"/>\n'
        '<text x="180" y="14" font-family="Libre Franklin,DejaVu Sans,sans-serif" font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">N. AMERICA</text>\n'
        '<text x="330" y="105" font-family="Libre Franklin,DejaVu Sans,sans-serif" font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">S. AMERICA</text>\n'
        '<text x="440" y="95" font-family="Libre Franklin,DejaVu Sans,sans-serif" font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">EUROPE</text>\n'
        '<text x="605" y="110" font-family="Libre Franklin,DejaVu Sans,sans-serif" font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">AFRICA</text>\n'
        '<text x="730" y="20" font-family="Libre Franklin,DejaVu Sans,sans-serif" font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">ASIA</text>\n'
        '<text x="860" y="130" font-family="Libre Franklin,DejaVu Sans,sans-serif" font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">AUSTRALIA</text>\n'
        + "\n".join(dots) + "\n" + "\n".join(badges) + "\n</svg>")

    html = (
        "<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\"><style>\n" + css
        + "\n</style></head><body><div class=\"page\">\n"
        + '<div class="head"><div class="top"><span class="l">THE WORLD IN ONE DAY</span>'
        + '<span class="r">WEDNESDAY 25 NOVEMBER 2026 &nbsp;\u2022&nbsp; 32 STORIES '
        + '&nbsp;\u2022&nbsp; 6 CONTINENTS</span></div>'
        + "<h1>THE WORLD TODAY</h1></div>\n"
        + '<div class="strip">Trump proposes tariffs on 14 economies'
        + "<i>\u2022</i>Two tankers hit by mines in the Strait of Hormuz"
        + "<i>\u2022</i>Cairo tanker fire kills 31</div>\n"
        + '<div class="chips">' + chips + "</div>\n"
        + '<div class="leads">\n' + "\n".join(lead_html) + "\n</div>\n"
        + '<div class="seclab">THE DAY IN 10 MORE</div>\n'
        + '<div class="feats">\n' + "\n".join(feat_html) + "\n</div>\n"
        + '<div class="map"><h3>WHERE IT HAPPENED <span>\u2014 SCENES 1\u201313</span> '
        + "&nbsp;\u2022&nbsp; NUMBERS MATCH THE STORIES ABOVE</h3>\n" + map_svg
        + '\n<div class="legend">' + legend + "</div></div>\n"
        + '<div class="also"><div class="seclab">ALSO ON WEDNESDAY 25 NOVEMBER \u2014 19 MORE STORIES</div>'
        + '<div class="briefs">\n' + "\n".join(cols) + "\n</div></div>\n"
        + '<div class="foot"><div class="datecheck"><b>DATE CHECK</b>'
        + "<span>Every story here happened, or was first reported, on "
        + "Wednesday 25 November 2026.</span>"
        + '<span class="how">HOW SURE <i>CONFIRMED</i> 2+ outlets '
        + "<i>OFFICIAL</i> on the record <i>REPORTED</i> one outlet "
        + "<i>CLAIM</i> one side\u2019s word</span></div>"
        + '<div class="srcs">SOURCES: AP \u2022 REUTERS \u2022 BBC \u2022 CNN \u2022 NYT \u2022 WSJ '
        + "\u2022 UEFA \u2022 ONETURN.NEWS \u2022 PICTURES AND MAP "
        + "DRAWN IN CODE, NOT PHOTOS</div></div>\n"
        + "</div></body></html>\n")

    (HERE / "render.html").write_text(html)
    print("wrote", HERE / "render.html", len(html), "bytes")
    pts = [(r[0], r[7], r[8]) for r in LEADS + GRID]
    bad = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = ((pts[i][1] - pts[j][1]) ** 2 + (pts[i][2] - pts[j][2]) ** 2) ** 0.5
            if d < 15:
                bad.append((pts[i][0], pts[j][0], round(d, 1)))
    print("badge collisions <15px:", bad if bad else "none")
    print("region counts:", counts)


if __name__ == "__main__":
    main()
