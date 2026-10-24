# Iron Horse

A vintage motorcycle for [Vanilla Wheels](https://github.com/the-rusty-shackleford/minecraft-vanilla-wheels)
on NeoForge 1.21.1. A rider and a pillion, a headlamp that lights the road, a kickstand it leans on
when parked and folds up when ridden; it leans into its turns, and it **jumps as a ridden horse
does**: hold the jump key, the jump bar fills where the experience bar was, let go. A full bar puts
it three blocks up, two aboard or one. There is no Java in it: the bike is a vehicle profile and one
Blockbench project, and the protocol does the rest (from Vanilla Wheels 1.19.0, its D-0047), so
driving, fuel, keys, lights, packing and the Mechanic Lift are documented there. By Chunkworks,
AGPL-3.0-or-later.

## Getting one

- **Chassis**: five steel ingots and a leather saddle (` LS` / `SSS` / `S S`), steel from Metals and
  Materials. The chassis item names the Iron Horse.
- **Build**: the chassis, **two wheels** and an engine in a Mechanic Lift, then Build. It fits either
  lift's deck. Paint it there with a dye: the tank, both fenders, the oil tank, the toolbox and the
  chain guard take it; undyed, they are the slate they were modelled in.
- **Fuel**: Vanilla Wheels' gas can, as any vehicle. An eighteen-thousand-tick tank, three quarters
  of a truck's.

## Riding it

- **Movement keys** ride; the fork steers, the front wheel and the headlamp turning with it, and it
  leans into the turn as far as balancing it needs (at most 35 degrees). The second seat is the
  pillion on the pad behind the saddle.
- **Parked** (nobody at the bars, wheels still), it leans 8 degrees left onto its kickstand; ridden,
  the stand folds back along the frame.
- **Jump** (the game's jump key, Space): hold it and the jump bar fills; let go and it jumps with what
  the bar held, exactly as a horse does (an average horse's strength, 0.7: a full bar rises 3.12
  blocks, a tap 0.62). A jump asked for in the air is made as it lands. It never drifts: on a bike the
  key is the jump's.
- **Landing** hurts neither rider, nor the bike, below Vanilla Wheels' seven blocks of suspension: a
  full jump off a three-block ledge lands them all whole.
- **Lights**: Vanilla Wheels' lights key; the headlamp's lens glows and lights the road through
  Luminance, range 10. No horn (Vanilla Wheels' only horn is a truck's), no chest.

| | |
|---|---|
| Top speed | 0.85 blocks a tick (17 m/s); acceleration 0.022, brake 0.06 |
| Steering | 30 degrees of lock; grip 0.85 |
| Climbs | one-block steps; a two-block wall needs a jump |
| Size | 2¾ blocks long, 1 wide, 1.4 high |
| Mass, durability | 0.5; durability 4 (a blow wears it a quarter of what it wears a boat) |
| Repair on the lift | 8 steel ingots for a wreck |
| Engine | a single cylinder ticking over, pitched from 0.75 to 1.5 with speed, heard 32 blocks off |

## How it is made

`devtools/art/reference/motorcycle.bbmodel` is the model as received, byte for byte
(`devtools/art/reference/SOURCES.md`). `devtools/art/build.py` writes every game file from it through
the shared writer `minecraft mods/tools/bbgen/bike.py`:

- the mesh, `assets/ironhorse/vanillawheels/mesh/iron_horse.bbmodel`: the received project with the
  slate sheet metal's texture turned grey (`tools/bbgen/paint.py`), its lightness kept as a share of
  the parts' mean colour, so the profile's `factory` colour (#566167) tints it back to the slate
  received and any dye colours the same shading;
- the profile, `data/ironhorse/vanillawheels/vehicle/iron_horse.json`: its wheels are where it touches
  the ground (`"drawn": false`), drawn by the model's own `wheel_front` and `wheel_rear` groups, which
  roll; the `steering` group (fork, bars, headlamp, front fender, front brake, front wheel) turns
  about the head tube's line, raked 24 degrees; `kickstand` turns 70 degrees about its hinge while
  ridden; the headlamp's lens is the front face of the four `headlamp_shell` cubes; `jump`, `lean`;
- the chassis recipe and its unlock, the lang file, `sounds.json`.

`build.py sounds` cuts the engine loop from a CC0 recording (`devtools/art/sounds/SOURCES.md`) with
`minecraft mods/tools/sound/cutlib.py`. Run both and commit what they write.

## Verification

`./gradlew build` runs five GameTests (`IronHorseGameTests`): the profile is the motorcycle (its fork
raked along the head tube, the kickstand's foot folding up by its hinge); five steel ingots and a
leather saddle craft its chassis; two up, a full bar clears a two-block wall and lands beyond while a
tap is stopped; it leans right into a right turn and left into a left and onto its stand parked; a full
jump off a three-block ledge lands both riders and itself unhurt. Then the booth (`IronHorseBooth`, on
the booth display): side on in stock slate and painted blue, leaning on its stand, the front-left
quarter, the stand down parked and folded once ridden, two up, leaning into a turn, the fork steered,
the jump on the **real** jump key (`devtools/booth/xkey.py`): the jump bar, then the bike at the top of
its arc beside the same view on the ground, the jump key held in a turn never drifting it, and the
headlamp at night. `-PskipBooth` leaves the booth out.
