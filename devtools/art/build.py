"""The Iron Horse's game files, from the model as received (devtools/art/reference/motorcycle.bbmodel).

Writes the mesh (the received project, its slate tank, fenders and boxes made dyeable), the profile,
the lang file, the chassis recipe and its unlock, and sounds.json, through the shared bike writer
(minecraft mods/tools/bbgen/bike.py). Everything it writes is committed; this script is the source of
truth for those files. Every number below is read off the model (devtools/art/reference/SOURCES.md
says where): the wheels' axles, the steering head's line, the saddle's and the pillion's tops, the
headlamp, the kickstand's hinge.

Run: uv run --no-project --with pillow python devtools/art/build.py
     uv run --no-project --with pillow --with numpy python devtools/art/build.py sounds   (the engine loop; needs ffmpeg)

Copyright (C) 2026 Chunkworks. SPDX-License-Identifier: AGPL-3.0-or-later.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT.parent / "tools/bbgen"))
import bike  # noqa: E402  (the shared writer: minecraft mods/tools/bbgen)

REFERENCE = "devtools/art/reference/motorcycle.bbmodel"

# The steering head: the head tube is a cube along +Z turned 65.6 degrees about X; the steering axis
# runs along it, raked 24 degrees back from upright, through the tube's own origin.
HEAD = math.radians(65.62353)
STEER_AXIS = [0.0, round(math.sin(HEAD), 5), round(-math.cos(HEAD), 5)]


def _painted() -> frozenset[str]:
    """The slate sheet metal: the tank's shell, both fenders (not their stays), the oil tank, the toolbox, the chain guard."""
    names = {e["name"] for e in json.loads((ROOT / REFERENCE).read_text(encoding="utf-8"))["elements"]}
    fenders = {n for n in names if n.startswith(("ff_", "rf_")) and "stay" not in n}
    return frozenset(fenders | {"tank_core", "tank_crown", "tank_nose", "tank_tail", "oil_tank", "toolbox", "chainguard"})


PAINTED = _painted()

PROFILE = {
    "scale": 0.0625,
    "handedness": "right",
    # 15.6 units across the bars, 43.7 nose to tail, 21.8 to the bar ends.
    "body": {"width": 1.0, "length": 2.75, "height": 1.4,
             "parts": [{"at": [0, 0, 15], "width": 0.8, "height": 1.2}, {"at": [0, 0, -15], "width": 0.8, "height": 1.2}]},
    # The saddle's top is 15.5 up, the pillion pad's 14.7; each attachment 0.4 over it as every truck's is.
    "seats": [{"at": [0, 15.9, -5.4], "driver": True}, {"at": [0, 15.1, -13.0]}],
    # Drawn by the model's own wheel groups (below): these are only where it touches the ground.
    "wheels": {"radius": 6.45, "drawn": False, "positions": [
        {"forward": 13.6, "right": 0, "up": 6.45, "steers": True},
        {"forward": -12.7, "right": 0, "up": 6.45}]},
    # A heavier, steadier machine than the Scrambler: faster flat out, slower off the mark, wider turns.
    "engine": {"max_speed": 0.85, "acceleration": 0.022, "reverse_speed": 0.2, "brake": 0.06, "drag": 0.01},
    "handling": {"grip": 0.85, "steer_degrees": 30, "drift_grip": 0.2, "drift_boost": 0.2, "drift_charge_ticks": 40},
    "climb": 1.0,
    "mass": 0.5,
    "durability": 4.0,
    "fuel": {"capacity": 18000},
    # The lens is the front face of the four headlamp shells, inside the rim.
    "headlights": {"at": [[0, 16.8, 12.3]],
                   "part": {"group": ["headlamp_shell_0", "headlamp_shell_1", "headlamp_shell_2", "headlamp_shell_3"], "z_min": 11.85},
                   "range": 10},
    "paint": {"part": {"group": sorted(PAINTED)}, "default": "gray"},
    "sounds": {"engine": "ironhorse:engine", "pitch": [0.75, 1.5], "volume": [0.35, 0.85]},
    "repair": {"ingredient": {"tag": "c:ingots/steel"}, "full_cost": 8},
    # An average horse's jump (D-0001): a full bar three blocks up.
    "jump": {"strength": 0.7},
    # Parked, it leans onto its kickstand, which is on its left.
    "lean": {"degrees": 35, "parked": -8},
    "moving": [
        {"part": {"group": "steering"}, "pivot": [0, 16.3, 9.95], "axis": STEER_AXIS, "by": "steer"},
        {"part": {"group": "wheel_front"}, "pivot": [0, 6.45, 13.6], "axis": [1, 0, 0], "by": "roll", "radius": 6.45, "within": 0},
        {"part": {"group": "wheel_rear"}, "pivot": [0, 6.45, -12.7], "axis": [1, 0, 0], "by": "roll", "radius": 6.45},
        # Modelled down; ridden, it folds back about its hinge until it lies along the frame.
        {"part": {"group": "kickstand"}, "pivot": [2.8, 7.4, -4.3], "axis": [1, 0, 0], "by": "ridden", "degrees": 70},
    ],
}

IRON_HORSE = bike.Bike(
    ns="ironhorse",
    name="iron_horse",
    display="Iron Horse",
    reference=REFERENCE,
    painted=PAINTED,
    profile=PROFILE,
    # Five steel ingots in a frame's shape and a leather saddle.
    recipe={"pattern": [" LS", "SSS", "S S"], "key": {"S": {"tag": "c:ingots/steel"}, "L": {"item": "minecraft:leather"}}},
    unlock="#c:ingots/steel",
    distance=32,
)

if __name__ == "__main__":
    if sys.argv[1:] == ["sounds"]:
        # A single cylinder ticking over, steady from 8 to 15 s: three seconds from 9.5, a quarter-second join.
        bike.engine_loop(ROOT, "ironhorse", "devtools/art/sounds/src/361407-single-cylinder-motorcycle.ogg", 9.5, 3.0, 0.25)
    else:
        print("factory", bike.build(ROOT, IRON_HORSE))
