import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

out_dir = r"d:\shunanda( natto don't delete)\shunanda portfolio\image\props"
os.makedirs(out_dir, exist_ok=True)

# Generate 1024x1024 transparent PNG overlays for each of the 10 props
# Coordinates match the 1024x1024 avatar frame:
# Center = (512, 512)
# Lab coat chest = (512, 530)
# Left hand = (390, 660)
# Right hand = (630, 660)

# Colors matching portfolio theme:
CYAN = (0, 210, 196, 255)
EMERALD = (0, 245, 155, 255)
GOLD = (245, 197, 24, 255)
DARK_BLUE = (15, 28, 48, 255)
WHITE = (245, 250, 255, 255)
SHADOW = (10, 15, 20, 180)

# 1. PROP: BOOK / NOTEBOOK (About Me) - Blue lab journal with bookmark
img_book = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_book)
# Held in left hand/arm: x: 300-440, y: 550-700
# Book spine & cover
d.polygon([(320, 560), (425, 530), (450, 680), (345, 715)], fill=(28, 55, 90, 255))
d.polygon([(325, 565), (420, 538), (442, 675), (347, 705)], fill=(40, 80, 130, 255))
# Pages
d.polygon([(420, 538), (435, 545), (455, 685), (442, 675)], fill=(240, 235, 220, 255))
# Bookmark ribbon
d.line([(380, 545), (395, 640), (405, 660)], fill=(0, 210, 196, 255), width=6)
# Biotech symbol on cover
d.ellipse([365, 600, 395, 630], outline=(0, 245, 155, 255), width=3)
# Hand holding book
d.ellipse([330, 630, 380, 675], fill=(238, 185, 150, 255))
d.ellipse([345, 640, 375, 665], fill=(220, 160, 130, 255))
img_book.save(os.path.join(out_dir, "prop_book.png"), "PNG")
print("1. prop_book.png created")

# 2. PROP: STACK OF BOOKS (Academic Evolution)
img_books = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_books)
# Bottom book (Deep Blue Genomics)
d.polygon([(380, 640), (580, 620), (600, 665), (400, 685)], fill=(20, 45, 85, 255))
d.polygon([(390, 645), (570, 628), (585, 658), (405, 675)], fill=(35, 75, 140, 255))
d.polygon([(570, 628), (595, 635), (615, 670), (585, 658)], fill=(235, 230, 215, 255))
# Middle book (Emerald Bio-Data)
d.polygon([(400, 605), (565, 590), (580, 630), (415, 645)], fill=(12, 70, 55, 255))
d.polygon([(408, 610), (555, 596), (568, 624), (420, 638)], fill=(20, 120, 95, 255))
d.polygon([(555, 596), (575, 602), (590, 634), (568, 624)], fill=(235, 230, 215, 255))
# Top book (Cyan Molecular Biology)
d.polygon([(420, 570), (550, 560), (560, 595), (430, 605)], fill=(10, 85, 95, 255))
d.polygon([(426, 574), (542, 565), (550, 590), (434, 599)], fill=(0, 165, 175, 255))
d.polygon([(542, 565), (558, 570), (568, 598), (550, 590)], fill=(245, 240, 230, 255))
# Hands supporting the books on left and right
d.ellipse([360, 640, 410, 680], fill=(238, 185, 150, 255)) # left hand
d.ellipse([580, 630, 630, 670], fill=(238, 185, 150, 255)) # right hand
img_books.save(os.path.join(out_dir, "prop_books.png"), "PNG")
print("2. prop_books.png created")

# 3. PROP: DNA DOUBLE HELIX (Research Interests)
img_dna = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_dna)
# Floating / held near right hand: x: 640-790, y: 380-600
# Hand gesturing / holding pedestal
d.ellipse([610, 580, 665, 635], fill=(238, 185, 150, 255))

# Draw 3D glowing DNA helix
cx = 700
top_y = 380
h_helix = 180
steps = 28
for i in range(steps):
    t = i / steps
    y = top_y + t * h_helix
    angle = t * 3.5 * np.pi
    x1 = cx + np.sin(angle) * 35
    x2 = cx - np.sin(angle) * 35
    depth = np.cos(angle)
    
    # Rung / base pair
    d.line([(x1, y), (x2, y)], fill=(120, 220, 210, 200), width=3)
    
    # Strand 1 node (Cyan)
    r1 = 6 + depth * 2.5
    d.ellipse([x1 - r1, y - r1, x1 + r1, y + r1], fill=(0, 210, 196, 255), outline=(255, 255, 255, 220), width=1)
    
    # Strand 2 node (Emerald)
    r2 = 6 - depth * 2.5
    d.ellipse([x2 - r2, y - r2, x2 + r2, y + r2], fill=(0, 245, 155, 255), outline=(255, 255, 255, 220), width=1)

# Subtle aura
img_dna_glow = img_dna.filter(ImageFilter.GaussianBlur(5))
img_dna = Image.alpha_composite(img_dna_glow, img_dna)
img_dna.save(os.path.join(out_dir, "prop_dna.png"), "PNG")
print("3. prop_dna.png created")

# 4. PROP: BIOINFORMATICS LAPTOP (Journey)
img_laptop = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_laptop)
# Held in front: x: 380-640, y: 550-700
# Laptop base / keyboard
d.polygon([(390, 640), (634, 640), (660, 685), (364, 685)], fill=(30, 42, 58, 255))
d.polygon([(398, 645), (626, 645), (648, 680), (376, 680)], fill=(45, 60, 80, 255))
# Trackpad
d.polygon([(485, 665), (539, 665), (543, 678), (481, 678)], fill=(60, 80, 105, 255))
# Laptop Screen (standing upright angled)
d.polygon([(410, 540), (614, 540), (634, 640), (390, 640)], fill=(18, 28, 42, 255))
# Screen Display (Glowing Dark Cyan with Bioinformatics charts)
d.polygon([(418, 548), (606, 548), (624, 634), (400, 634)], fill=(8, 20, 28, 255))
# DNA / graph on screen
d.line([(430, 590), (460, 575), (490, 605), (530, 565), (570, 595), (595, 580)], fill=(0, 245, 155, 255), width=3)
d.ellipse([502, 568, 522, 588], fill=(0, 210, 196, 255)) # logo
# Hands typing on edges
d.ellipse([345, 645, 395, 685], fill=(238, 185, 150, 255))
d.ellipse([625, 645, 675, 685], fill=(238, 185, 150, 255))
img_laptop.save(os.path.join(out_dir, "prop_laptop.png"), "PNG")
print("4. prop_laptop.png created")

# 5. PROP: OPTICAL LAB MICROSCOPE (Projects) - Major hands-on scientific tool
img_micro = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_micro)
# Microscope positioned at bottom left: x: 230-460, y: 520-800
# Base
d.polygon([(260, 750), (410, 730), (430, 780), (280, 800)], fill=(35, 45, 55, 255))
d.polygon([(270, 755), (400, 738), (418, 774), (288, 790)], fill=(60, 75, 90, 255))
# Stage / Slide holder
d.polygon([(300, 660), (430, 645), (445, 675), (315, 690)], fill=(20, 30, 40, 255))
# Slide (Glowing Cyan)
d.polygon([(340, 662), (400, 655), (408, 670), (348, 677)], fill=(0, 210, 196, 220))
# Objective turret & lenses
d.rectangle([355, 615, 385, 645], fill=(180, 190, 200, 255))
d.polygon([(360, 645), (370, 658), (380, 645)], fill=(0, 245, 155, 255))
# Microscope Arm (curved black metal)
d.polygon([(285, 740), (320, 735), (320, 580), (285, 580)], fill=(40, 50, 60, 255))
# Body Tube angled towards eyepiece
d.polygon([(290, 580), (380, 540), (410, 585), (320, 625)], fill=(50, 65, 80, 255))
# Eyepiece pointing towards avatar's eye/head
d.polygon([(370, 545), (415, 520), (430, 545), (385, 570)], fill=(20, 25, 30, 255))
d.ellipse([405, 515, 435, 545], fill=(0, 210, 196, 255)) # glowing glass lens
# Hand adjusting focus knob
d.ellipse([270, 630, 320, 675], fill=(238, 185, 150, 255))
img_micro.save(os.path.join(out_dir, "prop_microscope.png"), "PNG")
print("5. prop_microscope.png created")

# 6. PROP: CLIPBOARD / OBSERVATION SHEET (Internship / Training)
img_clip = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_clip)
# Held on left side: x: 300-450, y: 550-730
# Wooden board
d.polygon([(310, 570), (420, 540), (450, 690), (340, 720)], fill=(120, 75, 45, 255))
# Paper sheet
d.polygon([(320, 580), (410, 555), (438, 680), (348, 705)], fill=(245, 245, 240, 255))
# Metal clip at top
d.rectangle([345, 545, 385, 575], fill=(160, 175, 190, 255))
# Checklist lines & checkmarks (cyan & emerald ticks)
for row in range(5):
    ry = 595 + row * 18
    d.line([(340, ry), (405, ry - 15)], fill=(80, 95, 110, 255), width=2)
    d.ellipse([332, ry - 5, 338, ry + 1], fill=(0, 245, 155, 255))
# Hand holding clipboard
d.ellipse([335, 640, 385, 680], fill=(238, 185, 150, 255))
img_clip.save(os.path.join(out_dir, "prop_clipboard.png"), "PNG")
print("6. prop_clipboard.png created")

# 7. PROP: CERTIFICATE WITH GOLD SEAL (Certifications)
img_cert = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_cert)
# Held in center with both hands: x: 370-650, y: 550-710
# Certificate parchment
d.polygon([(380, 560), (630, 560), (645, 690), (365, 690)], fill=(250, 248, 235, 255))
# Certificate border (Navy & Gold)
d.polygon([(390, 570), (620, 570), (635, 680), (375, 680)], outline=(180, 140, 40, 255), width=3)
# Certificate title line
d.line([(430, 595), (580, 595)], fill=(20, 40, 70, 255), width=4)
d.line([(440, 615), (570, 615)], fill=(90, 105, 120, 255), width=2)
d.line([(450, 630), (560, 630)], fill=(90, 105, 120, 255), width=2)
# Golden Seal with red/cyan ribbons
d.ellipse([490, 640, 530, 680], fill=(245, 197, 24, 255), outline=(200, 150, 10, 255), width=2)
d.polygon([(495, 675), (488, 705), (505, 695)], fill=(0, 210, 196, 255))
d.polygon([(525, 675), (532, 705), (515, 695)], fill=(0, 245, 155, 255))
# Hands holding both sides
d.ellipse([345, 615, 395, 655], fill=(238, 185, 150, 255))
d.ellipse([615, 615, 665, 655], fill=(238, 185, 150, 255))
img_cert.save(os.path.join(out_dir, "prop_cert.png"), "PNG")
print("7. prop_cert.png created")

# 8. PROP: FLOATING SKILLS ICONS (Skills & Tools)
img_skills = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_skills)
# Gesturing left hand: x: 330-420, y: 620-670
d.ellipse([340, 620, 400, 665], fill=(238, 185, 150, 255))
# Floating badges on left side: x: 230-380, y: 380-570
badges = [
    (270, 410, "code", (0, 210, 196)),    # Python / R / Code </>
    (345, 385, "dna", (0, 245, 155)),     # Genomics DNA
    (250, 485, "chart", (190, 120, 255)), # Data / Omics
    (335, 475, "flask", (245, 197, 24))   # Lab / Biotech
]
for bx, by, btype, col in badges:
    # Outer glow
    d.ellipse([bx - 26, by - 26, bx + 26, by + 26], fill=(col[0], col[1], col[2], 50), outline=(col[0], col[1], col[2], 220), width=2)
    d.ellipse([bx - 20, by - 20, bx + 20, by + 20], fill=(12, 22, 35, 230))
    if btype == "code":
        d.line([(bx - 10, by), (bx - 5, by - 7)], fill=col, width=2)
        d.line([(bx - 5, by - 7), (bx - 10, by - 14)], fill=col, width=2)
        d.line([(bx + 10, by), (bx + 5, by - 7)], fill=col, width=2)
        d.line([(bx + 5, by - 7), (bx + 10, by - 14)], fill=col, width=2)
    elif btype == "dna":
        d.line([(bx - 8, by - 8), (bx + 8, by + 8)], fill=col, width=3)
        d.line([(bx + 8, by - 8), (bx - 8, by + 8)], fill=col, width=3)
    elif btype == "chart":
        d.rectangle([bx - 10, by + 2, bx - 6, by + 10], fill=col)
        d.rectangle([bx - 4, by - 4, bx, by + 10], fill=col)
        d.rectangle([bx + 2, by - 10, bx + 6, by + 10], fill=col)
    elif btype == "flask":
        d.polygon([(bx - 4, by - 10), (bx + 4, by - 10), (bx + 10, by + 8), (bx - 10, by + 8)], fill=col)

img_skills_glow = img_skills.filter(ImageFilter.GaussianBlur(4))
img_skills = Image.alpha_composite(img_skills_glow, img_skills)
img_skills.save(os.path.join(out_dir, "prop_skills.png"), "PNG")
print("8. prop_skills.png created")

# 9. PROP: GOLDEN TROPHY / CUP (Achievements)
img_trophy = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_trophy)
# Trophy held in center: x: 430-580, y: 520-690
# Cup base & pedestal
d.polygon([(460, 660), (550, 660), (560, 685), (450, 685)], fill=(30, 25, 20, 255))
d.polygon([(485, 620), (525, 620), (525, 660), (485, 660)], fill=(200, 155, 20, 255))
# Cup Body
d.polygon([(450, 530), (560, 530), (540, 620), (470, 620)], fill=(245, 197, 24, 255))
d.polygon([(460, 538), (550, 538), (532, 612), (478, 612)], fill=(255, 220, 70, 255))
# Star emblem on trophy
d.ellipse([493, 560, 517, 584], fill=(255, 255, 255, 255))
# Handles on left & right
d.arc([430, 540, 465, 590], start=90, end=270, fill=(210, 160, 15, 255), width=5)
d.arc([545, 540, 580, 590], start=270, end=90, fill=(210, 160, 15, 255), width=5)
# Hands holding trophy handles
d.ellipse([410, 570, 455, 610], fill=(238, 185, 150, 255))
d.ellipse([555, 570, 600, 610], fill=(238, 185, 150, 255))
img_trophy.save(os.path.join(out_dir, "prop_trophy.png"), "PNG")
print("9. prop_trophy.png created")

# 10. PROP: FRIENDLY WAVING HAND (Contact Me)
img_wave = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
d = ImageDraw.Draw(img_wave)
# Raised right hand waving: x: 670-800, y: 390-540
# Arm / sleeve rising up
d.polygon([(620, 540), (670, 490), (710, 520), (660, 570)], fill=(240, 245, 250, 255)) # white coat sleeve
d.polygon([(665, 495), (695, 465), (715, 485), (685, 515)], fill=(30, 42, 60, 255)) # navy cuff
# Palm and fingers
d.ellipse([690, 410, 765, 475], fill=(238, 185, 150, 255)) # palm
# 4 fingers + thumb
d.rounded_rectangle([695, 375, 715, 430], radius=8, fill=(238, 185, 150, 255))
d.rounded_rectangle([715, 370, 735, 425], radius=8, fill=(238, 185, 150, 255))
d.rounded_rectangle([735, 375, 755, 430], radius=8, fill=(238, 185, 150, 255))
d.rounded_rectangle([755, 390, 772, 440], radius=8, fill=(238, 185, 150, 255))
d.rounded_rectangle([675, 430, 705, 450], radius=6, fill=(238, 185, 150, 255)) # thumb
# Sparkle near hand
d.line([(775, 360), (775, 380)], fill=(0, 245, 155, 255), width=2)
d.line([(765, 370), (785, 370)], fill=(0, 245, 155, 255), width=2)
img_wave.save(os.path.join(out_dir, "prop_wave.png"), "PNG")
print("10. prop_wave.png created")
