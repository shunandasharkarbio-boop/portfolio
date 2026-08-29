import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

out_dir = r"d:\shunanda( natto don't delete)\shunanda portfolio\image"
head_base = Image.open(os.path.join(out_dir, "avatar_head.png")).convert("RGBA")
w, h = head_base.size

# Coordinates of the eyes in avatar_head.png (1024x1024):
# Left Eye (character's right): x: 375 to 455, y: 265 to 335, center = (415, 300)
# Right Eye (character's left): x: 550 to 630, y: 265 to 335, center = (590, 300)
# Skin tone = (240, 188, 155, 255)
# Sclera / eye white = (248, 250, 255, 255)
# Iris dark brown = (48, 28, 20, 255)
# Iris warm amber = (115, 68, 42, 255)
# Pupil = (20, 12, 10, 255)
# Eye highlight = (255, 255, 255, 255)
# Eyelash line = (35, 22, 18, 255)

skin_tone = (240, 188, 155, 255)

def draw_anime_eye(d, cx, cy, pupil_dx, pupil_dy, eye_h=32, is_happy=False, is_closed=False):
    if is_closed:
        # Closed eyelid arc
        d.arc([cx - 40, cy - 25, cx + 40, cy + 25], start=15, end=165, fill=(35, 22, 18, 255), width=6)
        return
    if is_happy:
        # Happy curved arc ( ^ _ ^ )
        d.arc([cx - 38, cy - 20, cx + 38, cy + 30], start=195, end=345, fill=(35, 22, 18, 255), width=7)
        return
    
    # 1. Eye socket / White sclera
    d.ellipse([cx - 38, cy - eye_h, cx + 38, cy + eye_h], fill=(250, 252, 255, 255))
    
    # 2. Large anime Iris
    ix = cx + pupil_dx
    iy = cy + pupil_dy
    iw = 25
    ih = eye_h - 4
    # Dark outer iris
    d.ellipse([ix - iw, iy - ih, ix + iw, iy + ih], fill=(55, 32, 24, 255))
    # Amber lower gradient
    d.ellipse([ix - iw + 3, iy - 2, ix + iw - 3, iy + ih - 2], fill=(135, 78, 45, 255))
    # Pupil
    d.ellipse([ix - 12, iy - 10, ix + 12, iy + 14], fill=(22, 12, 10, 255))
    
    # Highlights
    # Big top-left light
    d.ellipse([ix - 14, iy - 18, ix - 2, iy - 6], fill=(255, 255, 255, 255))
    # Small bottom-right light
    d.ellipse([ix + 6, iy + 4, ix + 13, iy + 11], fill=(255, 255, 255, 220))
    
    # Upper eyelash line
    d.arc([cx - 42, cy - eye_h - 8, cx + 42, cy + eye_h - 10], start=190, end=350, fill=(35, 22, 18, 255), width=7)
    # Upper lash flick
    d.line([(cx + 34, cy - eye_h + 2), (cx + 46, cy - eye_h - 4)], fill=(35, 22, 18, 255), width=5)

def create_head_variant(name, left_dx, left_dy, right_dx, right_dy, eye_h=32, is_happy=False, is_closed=False):
    img = head_base.copy()
    d = ImageDraw.Draw(img)
    
    # 1. Clear existing eye areas with skin tone
    d.ellipse([365, 255, 465, 345], fill=skin_tone)
    d.ellipse([540, 255, 640, 345], fill=skin_tone)
    
    # 2. Draw left eye and right eye
    draw_anime_eye(d, 415, 300, left_dx, left_dy, eye_h, is_happy, is_closed)
    draw_anime_eye(d, 590, 300, right_dx, right_dy, eye_h, is_happy, is_closed)
    
    # Subtle cute blush for friendly states
    d.ellipse([355, 335, 405, 360], fill=(255, 175, 175, 100))
    d.ellipse([600, 335, 650, 360], fill=(255, 175, 175, 100))
    
    path = os.path.join(out_dir, f"avatar_head_{name}.png")
    img.save(path, "PNG")
    print(f"Saved {path}")

# 1. Head Front (Default)
create_head_variant("front", 0, 0, 0, 0)

# 2. Look Right (About Me / Internship)
create_head_variant("look_right", 14, 1, 14, 1)

# 3. Look Left (Skills / DNA)
create_head_variant("look_left", -14, 1, -14, 1)

# 4. Look Down (Laptop / Journey)
create_head_variant("look_down", 0, 10, 0, 10, eye_h=25)

# 5. Look Microscope (Projects - Focused down-left into eyepiece)
create_head_variant("look_microscope", -12, 12, -10, 10, eye_h=24)

# 6. Look Up (Academic Evolution)
create_head_variant("look_up", 4, -12, 4, -12)

# 7. Happy Smile (Achievements / Milestone celebration)
create_head_variant("happy", 0, 0, 0, 0, is_happy=True)
