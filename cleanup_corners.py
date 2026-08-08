import re

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# The elegant-vine-corners block has an opening div and two internal SVGs. We can match up to the end of the second SVG's closing div... wait, the block is:
# <div class="elegant-vine-corners" ...>
#   <svg ...> ... </svg>
#   <svg ...> ... </svg>
# </div>
# We can use regex to remove it completely.
content = re.sub(r'<div class="elegant-vine-corners".*?</svg>\s*</div>', '', content, flags=re.DOTALL)

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Cleaned up old cyber corners.")
