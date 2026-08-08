import os
from PIL import Image
import math

image_path = r"C:\Users\User\.gemini\antigravity-ide\brain\61f1f6f0-e8ce-4edc-b9d9-c3ff5be70663\realistic_green_leaves_1786118132853.png"
out_dir = r"d:\shunanda( natto don't delete)\shunanda portfolio\image"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

img = Image.open(image_path).convert("RGBA")
width, height = img.size
pixels = img.load()

# Threshold for white background
visited = set()
components = []

def is_bg(r, g, b):
    # Pure white or very close
    return r > 240 and g > 240 and b > 240

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if is_bg(r, g, b):
            pixels[x, y] = (0, 0, 0, 0)
        else:
            pass # Keep it, but we also want to extract components

# Now extract components
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a > 0 and (x, y) not in visited:
            # BFS to find component
            q = [(x, y)]
            visited.add((x, y))
            comp_pixels = []
            min_x, max_x = x, x
            min_y, max_y = y, y
            
            while q:
                cx, cy = q.pop(0)
                comp_pixels.append((cx, cy))
                
                min_x = min(min_x, cx)
                max_x = max(max_x, cx)
                min_y = min(min_y, cy)
                max_y = max(max_y, cy)
                
                for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                    if 0 <= nx < width and 0 <= ny < height:
                        if (nx, ny) not in visited:
                            nr, ng, nb, na = pixels[nx, ny]
                            if na > 0:
                                visited.add((nx, ny))
                                q.append((nx, ny))
            
            # If component is large enough, save it
            if len(comp_pixels) > 1000:
                components.append((min_x, min_y, max_x, max_y))

print(f"Found {len(components)} leaf components")

# Sort by size (largest first)
components.sort(key=lambda c: (c[2]-c[0])*(c[3]-c[1]), reverse=True)

# Save top 3
for i, (min_x, min_y, max_x, max_y) in enumerate(components[:3]):
    # Add padding
    pad = 5
    min_x = max(0, min_x - pad)
    min_y = max(0, min_y - pad)
    max_x = min(width, max_x + pad)
    max_y = min(height, max_y + pad)
    
    leaf_img = img.crop((min_x, min_y, max_x, max_y))
    leaf_img.save(os.path.join(out_dir, f"leaf_{i+1}.png"))
    print(f"Saved leaf_{i+1}.png")

