# Sounds

Every shipped sound is a cut of a recording kept here, under CC0 (creativecommons.org/publicdomain/zero/1.0),
the licence read on the recording's own page before use.

| File | Source | Licence | Use |
|---|---|---|---|
| `src/361407-single-cylinder-motorcycle.ogg` | freesound.org sound 361407, "Single Cylinder Motorcycle", 192 kbps preview; SHA-256 `3ff9a764f046f457e0fff4230e031f6fc3d045a31227e0663d77a2c91d3f4c25` | CC0 1.0 | `assets/ironhorse/sounds/engine.ogg` |

**The engine loop**: the recording ticks over steadily from 8 to 15 s, its 100 ms loudness within about
2 dB. `build.py sounds` cuts 3.0 s from 9.5 s plus 0.25 s blended into the start
(`tools/sound/cutlib.py`). The profile pitches it from 0.75 at idle to 1.5 flat out; `sounds.json`
hears it 32 blocks off.
