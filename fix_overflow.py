import re

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add overflow: visible to .tree-card
css = css.replace('.tree-card {\n    position: relative !important;', '.tree-card {\n    position: relative !important;\n    overflow: visible !important;')

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\style.css", "w", encoding="utf-8") as f:
    f.write(css)

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add border radius to card-image and card-content inside tree-card just to be safe
html = html.replace('class="card-image inner-carousel-container" style="position: relative; z-index: 2;"', 'class="card-image inner-carousel-container" style="position: relative; z-index: 2; border-top-left-radius: 15px; border-top-right-radius: 15px;"')
html = html.replace('class="card-content" style="position: relative; z-index: 2;"', 'class="card-content" style="position: relative; z-index: 2; border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;"')

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed overflow issue.")
