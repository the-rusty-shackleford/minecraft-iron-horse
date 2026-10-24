# The model as received

`motorcycle.bbmodel`, received 2026-10-23, kept byte for byte. SHA-256 `f4374337df4fd16f7b6106716dcba252facfdd5691a698c3d517a4864218d642`.
A Blockbench project (format 5, free model, 289 cubes, one 512x512 texture embedded). The game's mesh
is made from it by `../build.py`, which changes only the painted parts' texture (made grey, so a dye
colours them; the profile's factory colour keeps an undyed bike the slate received). Copyright 2026
Chunkworks; AGPL-3.0-or-later.

Where the profile's numbers come from, in the model's units (a sixteenth of a block):

- **Wheels**: `wheel_front` turns about its group pivot (0, 6.45, 13.6), `wheel_rear` about
  (0, 6.45, -12.7), both radius 6.45; both tyres touch y 0.
- **Steering**: the `steering` group (`front_end` with the headlamp, `front_fender`, `wheel_front`,
  `front_brake`) turns about the line of `frame/head_tube`, a cube along +Z turned 65.6 degrees about
  X: the axis is (0, sin 65.6, -cos 65.6), raked 24 degrees, through the tube's origin (0, 16.3, 9.95).
- **Seats**: `saddle/saddle` spans z -8.4 to -2.4, its top at 15.5 (the rider at z -5.4);
  `saddle/pillion_pad` z -15.6 to -10.4, its top at 14.7 (the pillion at z -13).
- **Headlamp**: no lens cube; the lens is drawn on the front faces (z 11.88 to 12) of the four
  `headlamp_shell` cubes, inside `headlamp_rim`. The beam starts at (0, 16.8, 12.3).
- **Kickstand**: `frame/kickstand` hangs from its hinge at (2.8, 7.4, -4.3), turned (16, 0, -10): its
  foot is at about (1.7, 1.3, -6.1), on the bike's left. Parked, the bike leans 8 degrees left onto it;
  ridden, it turns 70 degrees about +X at the hinge, the foot coming up level with the hinge, behind it.
- **Slate**: `tank_core`, `tank_crown`, `tank_nose`, `tank_tail`, every `ff_` and `rf_` cube but
  the fender stays, `oil_tank`, `toolbox`, `chainguard`. No texture pixel they use is used by
  anything else (`tools/bbgen/paint.py` refuses one that is).
