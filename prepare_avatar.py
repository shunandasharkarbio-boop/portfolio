import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

out_dir = r"d:\shunanda( natto don't delete)\shunanda portfolio\image"
full_img = Image.open(os.path.join(out_dir, "avatar_full.png")).convert("RGBA")
w, h = full_img.size
arr = np.array(full_img)
alpha_arr = arr[:, :, 3]

# Exact anatomical chin curve:
# Vertex at (505, 432)
# Reaches (420, 385) on left and (590, 385) on right
# y_chin = 432 - ((x - 505)/85.0)**2 * 47

y_grid, x_grid = np.ogrid[:h, :w]
chin_limit = 432 - ((x_grid - 505.0) / 85.0)**2 * 47

# Neck center strip (470 <= x <= 540) can go down to y = 460
neck_bool = (x_grid >= 470) & (x_grid <= 540) & (y_grid <= 460)

# Hair curls on outer sides
hair_bool = ((x_grid < 365) | (x_grid > 645)) & (y_grid <= 660)

# Head is inside chin OR in neck strip OR in outer hair curls
head_bool = (alpha_arr > 30) & ((y_grid <= chin_limit) | neck_bool | hair_bool)

head_alpha = np.where(head_bool, alpha_arr, 0).astype(np.uint8)
head_res = full_img.copy()
head_res.putalpha(Image.fromarray(head_alpha, mode='L').filter(ImageFilter.GaussianBlur(0.6)))
head_res.save(os.path.join(out_dir, "avatar_head.png"), "PNG")
print("Saved curved avatar_head.png")

# BODY:
# Body should start from shoulders and have a smooth rounded neck dome
body_bool = (alpha_arr > 30) & (y_grid >= 415)
body_alpha = np.where(body_bool, alpha_arr, 0).astype(np.uint8)

body_res = full_img.copy()
draw_b = ImageDraw.Draw(body_res)
draw_b.ellipse([460, 385, 550, 455], fill=(235, 175, 140, 255))
draw_b.ellipse([475, 400, 535, 435], fill=(210, 150, 120, 255))
draw_b.polygon([(465, 445), (505, 495), (545, 445)], fill=(30, 40, 70, 255))

body_alpha_patch = Image.fromarray(body_alpha, mode='L')
draw_ba = ImageDraw.Draw(body_alpha_patch)
draw_ba.ellipse([460, 385, 550, 455], fill=255)
draw_ba.polygon([(465, 445), (505, 495), (545, 445)], fill=255)

body_res.putalpha(body_alpha_patch.filter(ImageFilter.GaussianBlur(0.6)))
body_res.save(os.path.join(out_dir, "avatar_body.png"), "PNG")
print("Saved curved avatar_body.png")

# BLINK LAYER:
blink_img = head_res.copy()
draw_blink = ImageDraw.Draw(blink_img)
skin_c = (238, 185, 150, 255)
draw_blink.ellipse([358, 260, 465, 345], fill=skin_c)
draw_blink.ellipse([538, 260, 645, 345], fill=skin_c)
lash_c = (35, 22, 18, 255)
draw_blink.arc([365, 275, 460, 335], start=15, end=165, fill=lash_c, width=6)
draw_blink.arc([543, 275, 638, 335], start=15, end=165, fill=lash_c, width=6)
draw_blink.ellipse([355, 340, 410, 368], fill=(255, 175, 175, 110))
draw_blink.ellipse([595, 340, 650, 368], fill=(255, 175, 175, 110))
blink_img.save(os.path.join(out_dir, "avatar_head_blink.png"), "PNG")
print("Saved curved avatar_head_blink.png")
