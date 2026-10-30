# Stronger locking button for FORZA uPVC football goals

A 3D-printable replacement for the plastic C-spring locking button (FORZA part 9231)
used to join the frame sections of FORZA uPVC garden goals. The originals are thin
and pop out easily, especially on an exposed, windy site.

Made for and tested on a FORZA 8 × 6 ft uPVC goal (70 mm tube).

## What's different from the original

| | Original 9231 | This version |
|---|---|---|
| Ring | ~64 mm OD, 21 mm tall, ~1.6 mm wall | same OD and height, **2.6 mm wall**, plus a thickened pad behind the button |
| Button | ~13 mm domed, ~9 mm proud of the ring | **11 mm straight-sided**, **13 mm proud**, 1.5 mm chamfered tip |

The domed original lets a sideways knock cam the button back into the tube. Straight
sides and a longer reach mean it has to be pressed in deliberately.

## Files

- `stl/forza_locking_button.stl`: ready to print
- `src/make_clip.py`: FreeCAD script that generates the STL. All dimensions are
  parameters at the top. Run it with `freecadcmd src/make_clip.py`.

## Printing

- Material: **PETG** recommended for outdoor use. PLA works for a test fit, but
  it's brittle and creeps under constant spring load.
- Orientation: stand the ring on its edge (ring axis vertical), with the button
  pointing sideways.
- Supports: under the button only (touching the buildplate).
- 4 walls, ~40% infill.

## Fit notes

- If it's too stiff to squeeze into the tube, reduce `WALL`.
- If it's loose in the tube, increase `OD`.

Not affiliated with or endorsed by FORZA / Net World Sports. Use at your own risk.

MIT licensed.
