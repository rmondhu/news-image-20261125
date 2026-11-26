# Design system — THE WORLD TODAY, 25 November 2026

Carried over from the 24 November edition (v5, judged "Perfect" by Hap),
with new stories and 13 new scenes. Same tokens, same 8px rhythm, same
layout. Nothing in the system changed — only the content did.

## Palet
| Token | Nilai | Pakai untuk |
|---|---|---|
| `--navy` | #14264d | header band, footer strip, World & Space |
| `--gold` | #d8b45a | kicker header, garis bawah masthead |
| `--accent` | #a31621 | strip headline merah, DATE CHECK box, pil REPORTED |
| `--paper` | #f7f1de | latar halaman |
| `--ink` / `--body` | #141414 / #262626 | judul / teks isi |
| `--muted` | #5c5540 | label benua di peta, sumber |
| `--card` | #fffdf4 | latar kartu |
| `--frame` | #d8cfb0 | border kartu & panel peta |
| `--land` | #c9bd93 | daratan peta |
| `--mapbg` | #ece5cb | laut peta |

**Sistem warna per region (chips, stat ribbon, kicker, badge peta, dot
peta, legenda):**
| Region | Warna | Cerita |
|---|---|---|
| Middle East | #c96a1e oranye | 5 |
| Europe | #1f5fa8 biru | 8 |
| Africa | #c0392b merah | 6 |
| Asia | #1e8a4c hijau | 4 |
| N. America | #6a4fa3 ungu | 4 |
| S. America | #b03a7d magenta | 2 |
| Oceania | #0e7d8c teal | 1 |
| World & Space | #14264d navy | 2 |

## Tipografi — tiga font, tiga tugas
| Font | Tugas | Ukuran |
|---|---|---|
| Playfair Display 900 | masthead (48px), headline lead 15.5px, headline kartu | serif hitam klasik |
| Libre Franklin | label, body, kicker, footer | grotesque bersih |
| Oswald 600 | angka & label di stat ribbon | 19px lead / 13px feature, condensed |

Ketiganya Google Fonts (SIL OFL 1.1, gratis komersial), diunduh segar
sebagai woff2 latin ke `fonts/` — `PlayfairDisplay-700.woff2` (38,404
byte), `LibreFranklin-400.woff2` (29,292 byte), `Oswald-600.woff2`
(12,740 byte). Di-load lewat `@font-face` dengan range weight
(`700 900` / `400 700` / `500 700`). Tanpa network saat render.

## Frame & layout
- **Header band navy penuh + kicker emas + garis emas;** masthead
  "THE WORLD TODAY" putih Playfair 900 48px; dateline "WEDNESDAY 25
  NOVEMBER 2026 • 32 STORIES • 6 CONTINENTS".
- **Strip headline merah** di bawah header: 3 headline lead.
- **Chips region** dengan jumlah cerita per region.
- **Tiap cerita dalam frame kotak:** border 1px `--frame`, latar
  `--card` — 3 lead + 10 feature (grid 5×2, label "THE DAY IN 10
  MORE") + 19 brief bernomor (3 kolom) + 2 ALSO TODAY.
- **Stat ribbon berwarna di dalam adegan** (Oswald + label pendek):
  "14", "2", "31", "4", "76", "1M", "1 TREATY", "2,100", "12–50 KM",
  "65–50", "$580,000", "4", "19".
- **Pil verifikasi di tiap kartu:** OFFICIAL hijau `#1e7a46`,
  CONFIRMED biru `#1f5fa8`, REPORTED merah `#a31621`, CLAIM amber
  `#b7791f` — ditetapkan jujur dari sumber tiap cerita (OFFICIAL =
  on the record; CONFIRMED = 2+ outlet; REPORTED = satu outlet;
  CLAIM = kata satu pihak saja). Definisi di footer.
- **Footer dua band kontras:** kotak DATE CHECK merah (teks putih)
  di atas strip sumber navy (teks putih); footer menulis
  "PICTURES AND MAP DRAWN IN CODE, NOT PHOTOS".
- Headline dan body di-clamp 2 baris; lead body ≤ ~110 karakter;
  sumber brief satu token pendek.

## Ilustrasi — 13 adegan kaya, digambar pakai kode
Resep per adegan (gaya v5 edisi kemarin): latar lingkungan utuh +
2–4 elemen berlapis dengan skala kontras + satu detail kecil + stat
ribbon di dalam adegan. Palet datar 2–4 warna, tanpa gradien.
Implementasi: `tools/scenes.py` — satu fungsi per adegan + helper
`_cloud`, `_bird`, `_sun`, `_wave_row`, `_smoke`, `_flame`,
`_drone`. Adegan dibangun sebagai list lalu `"".join` — tidak ada
implicit string concatenation bercampur `+` (bug v5 edisi kemarin).

Daftar adegan (belakang → depan):
- 1 TARIFFS: langit senja + matahari/burung/awan → skyline → kubah
  Capitol besar + kolom → kontainer bertumpuk 5 warna + tag harga
  "20%" → stempel TARIFF merah miring di tengah.
- 2 HORMUZ: langit + matahari/awan/burung → tebing ochre kiri-kanan
  + radar dish di tebing dekat → laut + ombak → tanker jauh + tanker
  dekat (api + asap) → ranjau berduri di antara keduanya.
- 3 CAIRO: langit malam + bulan/bintang → blok kota + jendela menyala
  → jalan melengkung + garis putus-putus → tanker terbalik miring
  + api tinggi + asap → kru pemadam + selang → motor gosong di kerb.
- 4 RAS TANURA: langit malam + bulan sabit → tangki bundar + cerobong
  menyala → percikan di atas tangki → 4 drone kecil.
- 5 CARTAGENA: langit + matahari/awan → helikopter → etalase kuning
  + papan "ÉXITO" + pintu + jendela → polisi + pembeli keluar →
  troli belanja ditinggalkan di pintu.
- 6 SPACEX: langit bintang → lengkung Bumi + daratan hijau → grid
  satelit kecil + satelit terbesar berisi rak server → roket naik.
- 7 SOLOMON: langit + matahari/awan → laut turquoise + ombak → pulau
  hijau + 2 palem → 2 bendera (Australia, Solomon) → kapal patroli →
  kura-kura kecil di dekat kapal.
- 8 CANARY: langit + awan → pulau vulkanik bersalju di belakang →
  laut biru dalam + ombak → perahu kayu cayuco penuh orang → kapal
  penyelamat oranye + selimut darurat merah di dek.
- 9 POLAND: langit + matahari/awan → tanah + deret pinus → garis
  batas merah putus-putus → stasiun radar + dish → jet tempur +
  jejak asap → AWACS kecil berdome.
- 10 NETANYAHU: langit + matahari/awan → kubah Knesset di belakang →
  gedung pengadilan (pedimen navy + 5 kolom + pintu) → timbangan
  kecil di anak tangga → palu di atas tumpukan kertas.
- 11 RAMAPHOSA: langit + matahari/awan → kincir angin di horizon →
  gedung pengadilan atap hijau + kolom → bangku hakim → sofa merah
  + uang kertas menyembul dari bantal.
- 12 GAZA: langit senja + matahari oranye → blok apartemen + jendela
  menyala + jemuran di atap → asap dari satu gedung → pantai + laut
  → perahu nelayan.
- 13 SUDAN: langit + matahari/awan → rumah atap datar di tepi jauh →
  sungai Nil Biru + ombak → tenda palang merah → 2 drone → kendi
  air di ambang pintu.

**Adegan mirip dibedakan dengan sengaja:** Hormuz vs Canary vs Gaza —
Hormuz selat sempit di antara tebing + 2 tanker + ranjau; Canary laut
lepas biru dalam + 1 perahu kayu penuh orang + kapal penyelamat
oranye; Gaza senja + blok apartemen + asap + perahu nelayan.
Netanyahu vs Ramaphosa — Netanyahu gedung pengadilan + palu +
kubah Knesset; Ramaphosa atap hijau + sofa + uang kertas + kincir
angin. Poland vs Sudan vs Ras Tanura — jet + garis batas merah +
radar vs kota sungai + tenda palang merah vs kilang malam + drone.

## Peta — outline negara asli
- Data segar: Natural Earth via
  https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json
  (180 negara), diunduh ke `tools/countries.geo.json`.
- `tools/gen_map.py` (ditulis segar untuk edisi ini): proyeksi
  equirectangular lon −180…180 → x 0…984, lat 75…−52 → y 0…144;
  Douglas–Peucker ~0.45°; buang Antartika; hasil 251 path di
  `tools/land.svg`, di-embed verbatim di `render.html`.
- Dot bernomor di lat/lon asli tiap cerita; badge digeser dengan
  leader line; generator memeriksa tiap pasangan badge ≥ 15px
  (hasil: tidak ada tabrakan). Label benua di laut/daratan kosong.
- Judul peta: "WHERE IT HAPPENED — SCENES 1–13".

## Jarak
- Padding halaman: 0 atas, 8px bawah, 20px kiri/kanan (header/footer
  full-bleed dengan margin −20px).
- Lead: padding 8px vertikal; peta: padding 7px atas, 8px bawah;
  tinggi terukur (Playwright): head 79, strip 27, chips 28, leads
  178, feats 292, map 173, also 158, foot 49; brief terakhir
  berakhir tepat di y=975 = atas footer.

## Pelajaran bug yang dihindari (dari edisi kemarin)
- Sumber brief harus satu token pendek (`.bs` pakai
  `white-space:nowrap` — sumber panjang menekan headline ke lebar
  nol dan meledakkan tinggi kolom).
- Selalu ukur tinggi tiap seksi dengan Playwright sebelum menyerahkan
  (`measure.mjs`); dua item ALSO TODAY pertama membungkus 2 baris dan
  meluber 11px ke balik footer — dipendekkan sampai satu baris.
- Lead body ≤ ~110 karakter agar muat 2 baris tanpa terpotong.
- Jangan campur implicit string concatenation dengan operator `+`
  dalam satu ekspresi return — adegan dibangun sebagai list +
  `"".join`.
- Elemen yang harus tersembunyi di balik sesuatu digambar SEBELUM
  elemen penutupnya.
