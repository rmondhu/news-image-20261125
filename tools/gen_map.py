#!/usr/bin/env python3
"""Build a real world-map fragment from country outline data.

Input: tools/countries.geo.json — Natural Earth country outlines
(johan/world.geo.json, 180 countries), downloaded fresh for this edition.
Output: tools/land.svg — one <g> of filled country paths.

Projection: equirectangular, lon -180..180 -> x 0..984,
lat 75..-52 -> y 0..144 (the vertical is slightly compressed so the
strip fits; continent shapes stay true). Rings are simplified with
Douglas-Peucker at ~0.45 degrees and Antarctica is dropped (it sits
below lat -52 anyway). The finished render.html embeds the fragment,
so the entry program needs no network at run time.

Run from the entry directory:  python3 tools/gen_map.py
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
WIDTH, HEIGHT = 984.0, 144.0
TOP_LAT, BOTTOM_LAT = 75.0, -52.0


def project(lon, lat):
    x = (lon + 180.0) / 360.0 * WIDTH
    y = (TOP_LAT - lat) / (TOP_LAT - BOTTOM_LAT) * HEIGHT
    return x, y


def _perp_distance(px, py, ax, ay, bx, by):
    """Perpendicular distance from point P to segment AB (degrees)."""
    dx, dy = bx - ax, by - ay
    seg = math.hypot(dx, dy)
    if seg == 0:
        return math.hypot(px - ax, py - ay)
    return abs(dy * px - dx * py + bx * ay - by * ax) / seg


def simplify(points, tolerance):
    """Douglas-Peucker: keep only the points that shape the ring."""
    if len(points) <= 2:
        return list(points)
    ax, ay = points[0]
    bx, by = points[-1]
    farthest, farthest_i = 0.0, -1
    for i in range(1, len(points) - 1):
        d = _perp_distance(points[i][0], points[i][1], ax, ay, bx, by)
        if d > farthest:
            farthest, farthest_i = d, i
    if farthest > tolerance:
        head = simplify(points[:farthest_i + 1], tolerance)[:-1]
        return head + simplify(points[farthest_i:], tolerance)
    return [points[0], points[-1]]


def ring_to_path(ring):
    # Clamp latitude into the strip, drop the closing duplicate point
    # (a zero-length baseline breaks Douglas-Peucker), simplify, project.
    pts = [(lon, min(max(lat, BOTTOM_LAT), TOP_LAT)) for lon, lat in ring]
    if len(pts) > 1 and pts[0] == pts[-1]:
        pts = pts[:-1]
    pts = simplify(pts, 0.45)
    if len(pts) < 3:
        return ""
    xy = [project(lon, lat) for lon, lat in pts]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in xy) + " Z"


def main():
    data = json.loads((HERE / "countries.geo.json").read_text())
    paths = []
    for feature in data["features"]:
        geom = feature["geometry"]
        if geom["type"] == "Polygon":
            rings = geom["coordinates"]
        elif geom["type"] == "MultiPolygon":
            rings = [ring for poly in geom["coordinates"] for ring in poly]
        else:
            continue
        for ring in rings:
            # Skip Antarctica outright (every point below -52).
            if all(lat < -52 for _lon, lat in ring):
                continue
            d = ring_to_path(ring)
            if d:
                paths.append(d)
    group = ('<g fill="#c9bd93" stroke="#f7f1de" stroke-width="0.4">\n'
             + "\n".join(f'<path d="{d}"/>' for d in paths)
             + "\n</g>")
    (HERE / "land.svg").write_text(group)
    print(f"countries: {len(data['features'])}, paths: {len(paths)}, "
          f"land.svg {len(group)} bytes")


if __name__ == "__main__":
    main()
