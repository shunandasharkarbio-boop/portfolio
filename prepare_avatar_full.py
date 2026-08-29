import os
from PIL import Image, ImageDraw, ImageFilter

base_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(base_dir, "image", "avatar_full.png")
base = Image.open(base_path).convert('RGBA')

# 1. Full blink version
blink = base.copy()
d = ImageDraw.Draw(blink)

skin_c = (242, 192, 160, 255)
lash_c = (38, 22, 16, 255)

# Left eye closed
d.ellipse([372, 262, 458, 338], fill=skin_c)
d.arc([374, 275, 456, 328], start=15, end=165, fill=lash_c, width=6)
d.line([(448, 298), (460, 292)], fill=lash_c, width=5)

# Right eye closed
d.ellipse([547, 262, 633, 338], fill=skin_c)
d.arc([549, 275, 631, 328], start=15, end=165, fill=lash_c, width=6)
d.line([(623, 298), (635, 292)], fill=lash_c, width=5)

blink.save(os.path.join(base_dir, "image", "avatar_full_blink.png"), "PNG")
print("Saved avatar_full_blink.png")

# 2. Full happy version
happy = base.copy()
dh = ImageDraw.Draw(happy)

dh.ellipse([372, 262, 458, 338], fill=skin_c)
dh.arc([376, 275, 454, 325], start=195, end=345, fill=lash_c, width=7)
dh.line([(446, 290), (458, 284)], fill=lash_c, width=5)

dh.ellipse([547, 262, 633, 338], fill=skin_c)
dh.arc([551, 275, 629, 325], start=195, end=345, fill=lash_c, width=7)
dh.line([(621, 290), (633, 284)], fill=lash_c, width=5)

# Gentle blush
dh.ellipse([350, 332, 405, 360], fill=(255, 175, 175, 120))
dh.ellipse([600, 332, 655, 360], fill=(255, 175, 175, 120))

happy.save(os.path.join(base_dir, "image", "avatar_full_happy.png"), "PNG")
print("Saved avatar_full_happy.png")
