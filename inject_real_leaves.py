import re

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

def replace_svg_with_img(match):
    width = match.group(1)
    leaf_num = match.group(2)
    # We map botanical-leaf-X to leaf_X.png
    return f'<img src="./image/leaf_{leaf_num}.png" style="width: {width}px; height: auto; object-fit: contain; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));" alt="leaf" />'

# Replace the inner SVG use statements
# Example: <svg width="40" height="40" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg>
content = re.sub(r'<svg width="(\d+)" height="\d+" viewBox="0 0 30 30"><use href="#botanical-leaf-(\d+)"/></svg>', replace_svg_with_img, content)

# I also need to replace the branch SVG uses which look slightly different:
# <use href="#botanical-leaf-2" x="465" y="1000" transform="rotate(30, 480, 1030)" />
# Wait, for the branch leaves, they are inside an SVG tag!
# You cannot put an <img> tag directly inside an <svg> tag unless it's wrapped in <foreignObject> or using <image>.
# It's much easier to use <image href="./image/leaf_X.png" width="W" height="H" ... />
def replace_branch_leaf(match):
    leaf_num = match.group(1)
    x = match.group(2)
    y = match.group(3)
    transform = match.group(4)
    # Use SVG image tag
    return f'<image href="./image/leaf_{leaf_num}.png" x="{x}" y="{y}" width="35" height="35" transform="{transform}" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.5))" />'

content = re.sub(r'<use href="#botanical-leaf-(\d+)" x="(\d+)" y="(\d+)" transform="(.*?)" />', replace_branch_leaf, content)

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced SVG leaves with real image leaves.")
