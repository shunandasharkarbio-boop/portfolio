import re

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the gradients
content = re.sub(
    r'<linearGradient id="leafGrad".*?</linearGradient>',
    '''<linearGradient id="vineGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="#6FAF45" />
                <stop offset="100%" stop-color="#A8E063" />
              </linearGradient>
              <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#A8E063" />
                <stop offset="100%" stop-color="#6FAF45" />
              </linearGradient>''',
    content,
    flags=re.DOTALL,
    count=1
)
content = re.sub(
    r'<linearGradient id="leafGradDark".*?</linearGradient>',
    '''<linearGradient id="leafGradDark" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#93CA51" />
                <stop offset="100%" stop-color="#5A9631" />
              </linearGradient>''',
    content,
    flags=re.DOTALL,
    count=1
)

# 2. Update the leaf paths stroke colors to match the new lighter green theme
content = content.replace('stroke="#1b5e20"', 'stroke="#4A752C"')

# 3. Replace the vines per timeline-item
items = re.split(r'(<div class="timeline-item timeline-(right|left)".*?>)', content)
# items[0] is everything before the first timeline-item
# items[1] is the capturing group 1: '<div class="timeline-item timeline-right"...>'
# items[2] is the capturing group 2: 'right'
# items[3] is the content until the next item, etc.

right_edge_vine = """                <!-- Right-Edge Botanical Vine -->
                <div class="card-botanical-vines right-edge-vine" aria-hidden="true" style="position: absolute; top: -15px; right: -25px; bottom: -15px; width: 60px; pointer-events: none; z-index: 0; filter: drop-shadow(0 0 6px rgba(120,255,170,0.18));">
                  <svg width="100%" height="100%" viewBox="0 0 60 100" preserveAspectRatio="none" style="overflow: visible; position: absolute; left: 0; top: 0;">
                    <path d="M 15,100 Q 55,70 30,40 T 10,0" stroke="url(#vineGrad)" stroke-width="2.5" fill="none" vector-effect="non-scaling-stroke" />
                  </svg>
                  <div style="position: absolute; top: 2%; left: 0px; transform: rotate(-60deg); animation: sway 3.5s infinite alternate;"><svg width="24" height="24" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 10%; left: 30px; transform: rotate(45deg); animation: sway 4s infinite alternate-reverse;"><svg width="20" height="20" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 20%; left: 5px; transform: rotate(-30deg); animation: sway 3s infinite alternate;"><svg width="28" height="28" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 32%; left: 40px; transform: rotate(70deg); animation: sway 4.2s infinite alternate-reverse;"><svg width="26" height="26" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 42%; left: 15px; transform: rotate(-45deg); animation: sway 3.2s infinite alternate;"><svg width="22" height="22" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 55%; left: 45px; transform: rotate(90deg); animation: sway 4.5s infinite alternate-reverse;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 68%; left: 10px; transform: rotate(-50deg); animation: sway 3.8s infinite alternate;"><svg width="24" height="24" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 80%; left: 35px; transform: rotate(55deg); animation: sway 4.1s infinite alternate-reverse;"><svg width="20" height="20" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 90%; left: 5px; transform: rotate(-25deg); animation: sway 3.3s infinite alternate;"><svg width="26" height="26" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 97%; left: 30px; transform: rotate(80deg); animation: sway 4.6s infinite alternate-reverse;"><svg width="22" height="22" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                </div>"""

left_edge_vine = """                <!-- Left-Edge Botanical Vine -->
                <div class="card-botanical-vines left-edge-vine" aria-hidden="true" style="position: absolute; top: -15px; left: -25px; bottom: -15px; width: 60px; pointer-events: none; z-index: 0; filter: drop-shadow(0 0 6px rgba(120,255,170,0.18));">
                  <svg width="100%" height="100%" viewBox="0 0 60 100" preserveAspectRatio="none" style="overflow: visible; position: absolute; left: 0; top: 0;">
                    <path d="M 45,100 Q 5,70 30,40 T 50,0" stroke="url(#vineGrad)" stroke-width="2.5" fill="none" vector-effect="non-scaling-stroke" />
                  </svg>
                  <div style="position: absolute; top: 3%; left: 45px; transform: rotate(60deg); animation: sway 3.5s infinite alternate;"><svg width="24" height="24" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 12%; left: 15px; transform: rotate(-45deg); animation: sway 4s infinite alternate-reverse;"><svg width="20" height="20" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 22%; left: 50px; transform: rotate(30deg); animation: sway 3s infinite alternate;"><svg width="28" height="28" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 35%; left: 5px; transform: rotate(-70deg); animation: sway 4.2s infinite alternate-reverse;"><svg width="26" height="26" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 45%; left: 35px; transform: rotate(45deg); animation: sway 3.2s infinite alternate;"><svg width="22" height="22" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 58%; left: 0px; transform: rotate(-90deg); animation: sway 4.5s infinite alternate-reverse;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 70%; left: 40px; transform: rotate(50deg); animation: sway 3.8s infinite alternate;"><svg width="24" height="24" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 82%; left: 10px; transform: rotate(-55deg); animation: sway 4.1s infinite alternate-reverse;"><svg width="20" height="20" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 92%; left: 45px; transform: rotate(25deg); animation: sway 3.3s infinite alternate;"><svg width="26" height="26" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 98%; left: 15px; transform: rotate(-80deg); animation: sway 4.6s infinite alternate-reverse;"><svg width="22" height="22" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                </div>"""

new_content = items[0]
for i in range(1, len(items), 3):
    header = items[i]
    side = items[i+1]
    block = items[i+2]
    
    # We replace <div class="card-botanical-vines"...</div></div> with the correct vine
    # Since we don't know exactly what's inside, we'll use regex to remove the existing vine block
    block = re.sub(r'<div class="card-botanical-vines".*?</div>\s*</div>', '', block, flags=re.DOTALL)
    
    # Insert new vine right after <div class="timeline-card tree-card" style="width: 42%; position: relative;">
    if side == 'right':
        # card is on right, vine is on left
        vine = left_edge_vine
    else:
        # card is on left, vine is on right
        vine = right_edge_vine
        
    block = re.sub(r'(<div class="timeline-card tree-card".*?>)', r'\1\n' + vine, block, count=1)
    
    # Add z-index: 2 to card-image and card-content
    block = block.replace('class="card-image inner-carousel-container"', 'class="card-image inner-carousel-container" style="position: relative; z-index: 2;"')
    block = block.replace('class="card-content"', 'class="card-content" style="position: relative; z-index: 2;"')
    
    new_content += header + block

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done replacing one-sided vines.")
