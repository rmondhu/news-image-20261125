# Tests — news-image-20261125

Run from `~/workspace/makefun/entries/news-image-20261125/`.

## 1. Rebuild the page
```
python3 tools/gen_map.py     # tools/land.svg: 180 countries, 251 paths
python3 tools/gen_entry.py   # render.html; expect "badge collisions <15px: none"
```
`gen_entry.py` also prints the region counts; they must sum to 32
(ME 5, EUR 8, AFR 6, ASIA 4, NAM 4, SAM 2, OCE 1, WLD 2).

## 2. Measure the layout (nothing behind the footer)
```
node measure.mjs
```
Expect: `maxBriefBottom` 975 (= footer top), `wrappedBriefs` 0,
`briefCount` 21, `scrollHeight` 1024, section heights roughly
head 79, strip 27, chips 28, leads 178, feats 292, map 173,
also 158, foot 49. If `maxBriefBottom` exceeds 975, a brief wrapped
— shorten the wrapping brief (usually an ALSO TODAY item) and
re-measure; do not add height anywhere else.

## 3. Render and check the image
```
node render.mjs
python3 -c "from PIL import Image; im=Image.open('entry.png'); print(im.size, im.format)"
sha256sum entry.png
```
Expect: PNG 1024×1024, under 1,048,576 bytes (this edition: 303,247).
Re-render to a second file and compare SHA-256 — the two must match
(render is deterministic: fixed layout, local fonts, no network).

## 4. Verify main.ts (two runs, two output dirs)
```
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 node main.ts
MAKEFUN_OUTPUT_DIR=out2 node main.ts
sha256sum out1/entry.png out2/entry.png entry.png   # all three identical
```
Expected SHA-256: `f718a999096487c1c02f603d4eeca5ac00d29c98d23a7f947cc230503f6e223a`.
`main.ts` is plain TypeScript, Node 22 stdlib only; it checks the PNG
magic bytes, the IHDR 1024×1024 dimensions and the ≤1 MiB cap, then
copies the file byte-for-byte.

## 5. Visual inspection
Open `entry.png` at full size and at 2× zoom on the leads, the
features, and the map. Check:
- All 13 scenes are legible and match their story; similar scenes
  (Hormuz / Canary / Gaza; Netanyahu / Ramaphosa) read as different.
- Every stat ribbon is readable inside its scene.
- No headline or body is clipped mid-word (2-line clamp); no text
  overlaps another element.
- The map shows real continent outlines; all 32 numbered badges are
  legible with clear leader lines; no badge pair collides.
- All 21 ALSO briefs are visible above the footer; the footer is two
  bands (red DATE CHECK + navy sources) on one line each.
- Header: navy band, gold kicker, white masthead; red headline strip
  below it.

## Not done (practice only — by design)
- No GitHub repo created, nothing pushed, nothing submitted to make.fun.
- No transcript bundle built (would be needed only for a real submission).
