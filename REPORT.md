# Report — news-image-20261125 (26 Nov 2026)

**Entry:** `~/workspace/makefun/entries/news-image-20261125/entry.png`
**Size:** 303,247 bytes · PNG 1024×1024 RGB · SHA-256
`f718a999096487c1c02f603d4eeca5ac00d29c98d23a7f947cc230503f6e223a`
**Status:** Built, verified, NOT pushed, NOT submitted — awaiting Hap's check.

## The 32 stories — why these

All events happened, or were first reported, on Wednesday 25 November
2026. Sources: One Turn, Just Security Early Edition, Reuters, AP, BBC,
CNN, UEFA, UN News, NPR / AP, The Times, Sowetan / Bloomberg, WSJ, FCC /
TechCrunch. Full notes in `news.md`.

**Leads (the three stories a picture editor would lead with):**
1. **TARIFFS** — the Trump administration proposes new tariffs on 14
   trading partners after an eight-month Section 301 probe; China faces
   up to ~45% combined. The day's biggest trade story, with a countable
   stat (14 economies).
2. **HORMUZ** — the IRGC says two oil tankers struck naval mines in the
   Strait of Hormuz; the Joint Maritime Information Centre says the mine
   claims are unconfirmed. The day's most dangerous escalation — and the
   honest pill is CLAIM, not REPORTED, because the mine claim is one
   side's word.
3. **CAIRO** — a fuel tanker overturns and ignites on Cairo's ring road,
   killing at least 31 and injuring 21. The day's deadliest single event.

**Grid (breadth across 6 continents):**
- Middle East & Gulf (4, 10, 12, 27): Ras Tanura refinery attack claim,
  Netanyahu trial + Knesset inquiry vote, Gaza security-chief killing,
  IS attack in Hasaka.
- Europe (8, 9, 14, 15, 17, 20, 25, 32): Canary Islands record arrivals,
  Poland no-fly zone, Kyiv missiles, Rosneft refinery drone hits, Merz
  warning, Spain snap election, Poundland collapse, Champions League.
- Americas (5, 24, 29, 30, 31): Cartagena hostage rescue, Argentina
  recession, Dell AI results, US inflation 3.8%, Macy's parade postponed.
- Asia (18, 19, 21, 23): North Korea expels Swiss envoy, Shanghai party
  chief probed, Bogor mine rescue, Bangladesh garment wage rise.
- Africa (3, 11, 13, 16, 22, 26): Cairo fire, Ramaphosa report thrown
  out, Sudan drone strikes, Libya retaliation vow, Nigeria attack, DR
  Congo Ebola evacuation.
- Oceania (7): Australia–Solomon Islands security treaty.
- World & Space (6, 28): SpaceX one-million-satellite authorisation,
  Shenzhou-24 docking with Pakistan's first astronaut.
- **Also today:** S&P 500 slips 0.25% / Brent $90.82; Boehly-led group
  clinches Lukoil overseas assets.

**What was left out (alternates in `news.md`):** the single-sourced
report of US strikes on Iranian leaders, the Huawei verdict (already
yesterday's lead), the CIA/ODNI breach (reported Tuesday), and the
Niger kidnapping (happened 21–22 Nov) — all real, but weaker or
wrong-dated for a 25 Nov one-image summary.

## Design decisions
- Same winner system as the 24 Nov v5 edition (Hap: "Perfect"): navy
  header + gold kicker, red headline strip, region colour system,
  framed cards, stat ribbons inside code-drawn scenes, real world map,
  red DATE CHECK footer + navy sources strip, three fonts. See
  `DESIGN.md`.
- All 13 scenes are new, written fresh from the ILLUSTRATION lines in
  `news.md` — nothing copied from yesterday's scenes. Similar scenes
  are kept apart on purpose (Hormuz vs Canary vs Gaza; Netanyahu vs
  Ramaphosa; Poland vs Sudan vs Ras Tanura).
- Verification pills set honestly: Hormuz = CLAIM (IRGC claim, JMIC
  unconfirmed); Ras Tanura = CLAIM (Houthi claim, coalition does not
  confirm the hit); Cairo = CONFIRMED (AP/Reuters/CNN/BBC).
- Map rebuilt from fresh data: Natural Earth countries.geo.json
  (180 countries) downloaded for this edition; `tools/gen_map.py`
  written fresh (251 paths); badge positions chosen fresh for this
  edition's 32 locations (Washington appears twice — stories 1 and 30
  share the same dot, with two badges fanning out).

## Fixes found in the first renders
1. **ALSO TODAY overflow:** the two ALSO TODAY items wrapped to 2 lines
   (28px rows) and pushed the last brief 11px behind the footer.
   Shortened both to one line; after the fix all 21 briefs are
   single-line, max brief bottom exactly at the footer top (y=975).
2. **Feature 4 body clipped** ("…the refinery hit is not…") by the
   2-line clamp → trimmed to "Coalition says four drones were
   intercepted over Ras Tanura."
3. **Lead 1 Capitol dome too small/pale** → enlarged (52px wide, navy
   outline, 5 columns) so it reads at lead size.
4. **Lead 3 tanker hard to read** → enlarged the tipped tanker and
   gave it an outline so the overturned shape reads.

## Verification
- PNG 1024×1024, 303,247 bytes (< 1 MiB). ✔
- `main.ts` run twice (two output dirs) → identical SHA-256
  `f718a999096487c1c02f603d4eeca5ac00d29c98d23a7f947cc230503f6e223a`,
  matching entry.png. Deterministic. ✔
- Re-render via `node render.mjs` → identical SHA-256 again. ✔
- `python3 tools/gen_entry.py` → render.html 107,718 bytes; badge
  check: no badge pair < 15px apart. ✔
- Layout measurement (Playwright, `measure.mjs`): head 79, strip 27,
  chips 28, leads 178, feats 292, map 173, also 158, foot 49; all 21
  ALSO briefs visible, 0 wrapped, max brief bottom y=975 = footer top. ✔
- Visual inspection at full size + 2× leads zoom + 2× features zoom +
  2× map zoom: all 13 scenes legible and relevant; similar scenes read
  as different; stat ribbons readable inside every scene; no clipped
  or colliding text; map is real world outlines with all 32 badges
  legible; ALSO list complete above the footer. ✔

## Files
- `entry.png` — the image for Hap to grade.
- `render.html`, `render.mjs`, `measure.mjs`, `main.ts`, `news.md`,
  `DESIGN.md`, `REPORT.md`, `TESTS.md`, `LICENSE`, `README.md`
- `.makefun/owner.json` — payout wallet
- `tools/gen_entry.py` — builds render.html from story data
- `tools/scenes.py` — the 13 rich vector scenes (one function per scene)
- `tools/gen_map.py` — builds tools/land.svg from Natural Earth data
- `tools/countries.geo.json` — 180-country outlines (source data)
- `tools/land.svg` — 251 country paths embedded in render.html
- `fonts/` — PlayfairDisplay-700.woff2, LibreFranklin-400.woff2,
  Oswald-600.woff2 (Google Fonts, SIL OFL 1.1)

## Not done (by design)
- No GitHub repo created, nothing pushed, nothing submitted to make.fun.
- No transcript bundle built (needed only for a real submission).
