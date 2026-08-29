import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

out_dir = r"d:\shunanda( natto don't delete)\shunanda portfolio\image"
head_base = Image.open(os.path.join(out_dir, "avatar_head.png")).convert("RGBA")
w, h = head_base.size

# 1. BLINK OVERLAY (ONLY covers the eye sockets with natural skin + closed lash lines)
blink_overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
d = ImageDraw.Draw(blink_overlay)

# Left eye area center (415, 300), Right eye area center (590, 300)
# Skin tone sampled from face
skin_c = (242, 192, 160, 255)
lash_c = (38, 22, 16, 255)

# Left eye closed
d.ellipse([372, 262, 458, 338], fill=skin_c)
d.arc([374, 275, 456, 328], start=15, end=165, fill=lash_c, width=6)
d.line([(448, 298), (460, 292)], fill=lash_c, width=5) # lash tip

# Right eye closed
d.ellipse([547, 262, 633, 338], fill=skin_c)
d.arc([549, 275, 631, 328], start=15, end=165, fill=lash_c, width=6)
d.line([(623, 298), (635, 292)], fill=lash_c, width=5)

blink_overlay = blink_overlay.filter(ImageFilter.GaussianBlur(0.5))
blink_overlay.save(os.path.join(out_dir, "avatar_head_blink.png"), "PNG")
print("Saved clean avatar_head_blink.png")

# 2. HAPPY EYES OVERLAY (Achievements / ^ _ ^)
happy_overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
dh = ImageDraw.Draw(happy_overlay)

dh.ellipse([372, 262, 458, 338], fill=skin_c)
dh.arc([376, 275, 454, 325], start=195, end=345, fill=lash_c, width=7)
dh.line([(446, 290), (458, 284)], fill=lash_c, width=5)

dh.ellipse([547, 262, 633, 338], fill=skin_c)
dh.arc([551, 275, 629, 325], start=195, end=345, fill=lash_c, width=7)
dh.line([(621, 290), (633, 284)], fill=lash_c, width=5)

# Cute blush
dh.ellipse([350, 332, 405, 360], fill=(255, 175, 175, 120))
dh.ellipse([600, 332, 655, 360], fill=(255, 175, 175, 120))

happy_overlay = happy_overlay.filter(ImageFilter.GaussianBlur(0.5))
happy_overlay.save(os.path.join(out_dir, "avatar_head_happy.png"), "PNG")
print("Saved clean avatar_head_happy.png")
