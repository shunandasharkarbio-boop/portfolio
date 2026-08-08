import random
import re

def get_leaves_html(is_left_card):
    html = []
    for i in range(45):
        leaf_num = random.randint(1, 3)
        size = random.randint(25, 45)
        sway_dur = round(random.uniform(3.0, 5.0), 1)
        anim_dir = "alternate" if random.random() < 0.5 else "alternate-reverse"
        base_rotation = 0
        
        progress = i / 45.0
        
        if progress < 0.2:
            p = progress / 0.2
            top = 50 + (40 * p)
            if is_left_card:
                side = f'left: {random.randint(-20, -5)}px;'
                base_rotation = -45 + random.randint(-40, 40)
            else:
                side = f'right: {random.randint(-20, -5)}px;'
                base_rotation = 45 + random.randint(-40, 40)
        elif progress < 0.5:
            p = (progress - 0.2) / 0.3
            top = random.randint(95, 102)
            pos_pct = p * 100
            if is_left_card:
                side = f'left: {pos_pct}%;'
                base_rotation = random.randint(-40, 40)
            else:
                side = f'right: {pos_pct}%;'
                base_rotation = random.randint(-40, 40)
        elif progress < 0.85:
            p = (progress - 0.5) / 0.35
            top = 95 - (90 * p)
            if is_left_card:
                side = f'right: {random.randint(-20, 0)}px;'
                base_rotation = 90 + random.randint(-40, 40)
            else:
                side = f'left: {random.randint(-20, 0)}px;'
                base_rotation = -90 + random.randint(-40, 40)
        else:
            p = (progress - 0.85) / 0.15
            top = random.randint(-15, -5)
            pos_pct = p * 50
            if is_left_card:
                side = f'right: {pos_pct}%;'
                base_rotation = 180 + random.randint(-40, 40)
            else:
                side = f'left: {pos_pct}%;'
                base_rotation = 180 + random.randint(-40, 40)
                
        top += random.randint(-3, 3)
        if isinstance(top, float): top = round(top, 1)
        
        top_str = f"{top}%" if isinstance(top, (int, float)) and 0 < top < 90 else f"{top}px" if top <= 0 else f"{top}%"
        
        leaf_html = f'<div style="position: absolute; top: {top_str}; {side} transform: rotate({base_rotation}deg); animation: sway {sway_dur}s infinite {anim_dir};"><img src="./image/leaf_{leaf_num}.png" style="width: {size}px; height: auto; object-fit: contain; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));" alt="leaf" /></div>'
        html.append(leaf_html)
        
    return "\n".join(html)

with open(r"d:\shunanda( natto don't delete)\shunanda portfolio\index.html", "r", encoding="utf-8") as f:
    content = f.read()

def replace_left_leaves(match):
    prefix = match.group(1)
    leaves = get_leaves_html(True)
    return prefix + "\n" + leaves + "\n                </div>"

content = re.sub(r'(<div class="card-botanical-vines left-card-long-vine".*?</svg>).*?</div>\s*</div>', replace_left_leaves, content, flags=re.DOTALL)

def replace_right_leaves(match):
    prefix = match.group(1)
    leaves = get_leaves_html(False)
    return prefix + "\n" + leaves + "\n                </div>"

content = re.sub(r'(<div class="card-botanical-vines right-card-long-vine".*?</svg>).*?</div>\s*</div>', replace_right_leaves, content, flags=re.DOTALL)

with open(r"d:\shunanda( natto don't delete)\shunanda portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Injected lots of leaves!")
