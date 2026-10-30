# Beefed-up FORZA 8x6 uPVC goal locking button (replacement for part 9231)
# Original: ~64 mm OD C-ring, 21 mm tall, ~1.6 mm wall, 13 mm button protruding ~9 mm.
# Goal tube: 70 mm OD, 2 mm wall -> ~66 mm ID.
import FreeCAD, Part, math
from FreeCAD import Vector as V

OD      = 64.0   # ring outer diameter (free state)
WALL    = 2.6    # original ~1.6 -> stiffer spring
H       = 21.0   # band height
GAP_DEG = 90.0   # opening opposite the button
BTN_D   = 11.0   # button diameter (v3: 13 -> 11, v2 snapped forcing a fat button through the hole)
BTN_OUT = 13.0   # how far the button tip sits past the ring OD (v2: 9 -> 13, v1 only just cleared the outer tube)
BTN_CH  = 1.5    # small chamfer on the tip instead of a full dome, so a side knock can't cam it back in
PAD_T   = 2.0    # extra thickness inside the ring at the button root
PAD_DEG = 40.0   # angular width of the root pad

R, Ri = OD/2, OD/2 - WALL
ring = Part.makeCylinder(R, H).cut(Part.makeCylinder(Ri, H))

# root pad: thicken the band behind the button, where originals crack
pad = Part.makeCylinder(Ri+0.1, H, V(0,0,0), V(0,0,1), PAD_DEG).cut(Part.makeCylinder(Ri-PAD_T, H))
pad.rotate(V(0,0,0), V(0,0,1), -PAD_DEG/2)
ring = ring.fuse(pad)

# opening opposite the button (button on +X, gap centred on -X)
wedge = Part.makeCylinder(R+5, H, V(0,0,0), V(0,0,1), GAP_DEG)
wedge.rotate(V(0,0,0), V(0,0,1), 180 - GAP_DEG/2)
ring = ring.cut(wedge)

# round off the tips so they slide into the tube without catching
for ang in (180 - GAP_DEG/2, 180 + GAP_DEG/2):
    a = math.radians(ang)
    c = V((R - WALL/2)*math.cos(a), (R - WALL/2)*math.sin(a), 0)
    ring = ring.fuse(Part.makeCylinder(WALL/2, H, c))

# button: straight-sided cylinder with only a small chamfered tip (v1 had a full dome,
# which let a sideways kick cam the button back into the tube)
zc = H/2
r = BTN_D/2
x0 = Ri - PAD_T + 0.5
tip = R + BTN_OUT
btn = Part.makeCylinder(r, (tip - BTN_CH) - x0, V(x0, 0, zc), V(1,0,0))
btn = btn.fuse(Part.makeCone(r, r - BTN_CH, BTN_CH, V(tip - BTN_CH, 0, zc), V(1,0,0)))
clip = ring.fuse(btn).removeSplitter()

clip.exportStl("forza_locking_button.stl")
bb = clip.BoundBox
print("ok", "vol mm3 %.0f" % clip.Volume, "bbox %.1f x %.1f x %.1f" % (bb.XLength, bb.YLength, bb.ZLength), "valid", clip.isValid())
