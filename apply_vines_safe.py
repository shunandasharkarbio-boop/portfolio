import re
import sys

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject Leaf Defs and Animations
defs_start = content.find('<defs>')
if defs_start == -1:
    print("Defs not found")
    sys.exit(1)

new_defs = """
            <style>
              @keyframes sway {
                0% { transform: rotate(-5deg); }
                100% { transform: rotate(5deg); }
              }
            </style>
            <defs>
              <linearGradient id="vineGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="#6FAF45" />
                <stop offset="100%" stop-color="#A8E063" />
              </linearGradient>
              <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#A8E063" />
                <stop offset="100%" stop-color="#6FAF45" />
              </linearGradient>
              <linearGradient id="leafGradDark" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#93CA51" />
                <stop offset="100%" stop-color="#5A9631" />
              </linearGradient>
              <g id="botanical-leaf-1">
                <path d="M15,30 Q15,25 15,20" stroke="#4A752C" stroke-width="1.5" fill="none" />
                <path d="M15,20 C5,20 0,5 15,0 C30,5 25,20 15,20 Z" fill="url(#leafGrad)" />
                <path d="M15,20 Q15,10 15,2" stroke="#4A752C" stroke-width="0.75" fill="none" />
              </g>
              <g id="botanical-leaf-2">
                <path d="M15,30 Q15,25 15,20" stroke="#4A752C" stroke-width="1.2" fill="none" />
                <path d="M15,20 C8,22 2,10 15,2 C28,10 22,22 15,20 Z" fill="url(#leafGradDark)" />
                <path d="M15,20 Q15,12 15,3" stroke="#4A752C" stroke-width="0.5" fill="none" />
              </g>
              <g id="botanical-leaf-3">
                <path d="M15,30 Q15,27 15,25" stroke="#4A752C" stroke-width="1" fill="none" />
                <path d="M15,25 C0,25 -5,12 15,5 C35,12 30,25 15,25 Z" fill="url(#leafGrad)" />
                <path d="M15,25 Q15,15 15,6" stroke="#4A752C" stroke-width="0.5" fill="none" />
              </g>
"""
content = content.replace('<defs>', new_defs)

# 2. Replace Branches
# branch-2024 (Right card)
branch_2024_new = """<g class="tree-branch-group" id="branch-2024">
              <path class="tree-branch-path" d="M400,1050 Q480,1035 560,1050" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,1050 Q480,1065 560,1050" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 4s ease-in-out infinite alternate; transform-origin: 480px 1030px;"><use href="#botanical-leaf-2" x="465" y="1000" transform="rotate(30, 480, 1030)" /></g>
              <g style="animation: sway 3.5s ease-in-out infinite alternate-reverse; transform-origin: 520px 1060px;"><use href="#botanical-leaf-1" x="505" y="1030" transform="scale(0.8) rotate(130, 520, 1060)" /></g>
            </g>"""
content = re.sub(r'<g class="tree-branch-group" id="branch-2024">.*?</g>', branch_2024_new, content, flags=re.DOTALL)

# branch-2025 (Left card)
branch_2025_new = """<g class="tree-branch-group" id="branch-2025">
              <path class="tree-branch-path" d="M400,770 Q320,755 240,770" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,770 Q320,785 240,770" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 3s ease-in-out infinite alternate; transform-origin: 320px 750px;"><use href="#botanical-leaf-1" x="305" y="720" transform="rotate(-30, 320, 750)" /></g>
              <g style="animation: sway 4.5s ease-in-out infinite alternate-reverse; transform-origin: 280px 780px;"><use href="#botanical-leaf-3" x="265" y="750" transform="scale(0.8) rotate(-130, 280, 780)" /></g>
            </g>"""
content = re.sub(r'<g class="tree-branch-group" id="branch-2025">.*?</g>', branch_2025_new, content, flags=re.DOTALL)

# branch-2026 (Right card)
branch_2026_new = """<g class="tree-branch-group" id="branch-2026">
              <path class="tree-branch-path" d="M400,490 Q480,475 560,490" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,490 Q480,505 560,490" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 4s ease-in-out infinite alternate; transform-origin: 480px 470px;"><use href="#botanical-leaf-3" x="465" y="440" transform="rotate(20, 480, 470)" /></g>
              <g style="animation: sway 3.2s ease-in-out infinite alternate-reverse; transform-origin: 520px 500px;"><use href="#botanical-leaf-2" x="505" y="470" transform="scale(0.8) rotate(140, 520, 500)" /></g>
            </g>"""
content = re.sub(r'<g class="tree-branch-group" id="branch-2026">.*?</g>', branch_2026_new, content, flags=re.DOTALL)

# branch-future (Left card)
branch_future_new = """<g class="tree-branch-group" id="branch-future">
              <path class="tree-branch-path" d="M400,210 Q320,195 240,210" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,210 Q320,225 240,210" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 3.7s ease-in-out infinite alternate; transform-origin: 320px 190px;"><use href="#botanical-leaf-2" x="305" y="160" transform="rotate(-40, 320, 190)" /></g>
              <g style="animation: sway 4s ease-in-out infinite alternate-reverse; transform-origin: 280px 220px;"><use href="#botanical-leaf-1" x="265" y="190" transform="scale(0.9) rotate(-110, 280, 220)" /></g>
            </g>"""
content = re.sub(r'<g class="tree-branch-group" id="branch-future">.*?</g>', branch_future_new, content, flags=re.DOTALL)

# 3. Clean all old card-vine-corner divs safely
content = re.sub(r'<div class="card-vine-corner.*?</div>', '', content, flags=re.DOTALL)


left_card_long_vine = """
                <!-- Main Long Vine for Left-Side Cards (Wrapping Left, Bottom, Right, Top) -->
                <div class="card-botanical-vines left-card-long-vine" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; filter: drop-shadow(0 0 8px rgba(120,255,170,0.25));">
                  <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none" style="overflow: visible; position: absolute; left: 0; top: 0;">
                    <path d="M -2,50 Q 5,80 10,95 Q 50,102 90,95 Q 102,50 95,5 Q 80,-2 50,-2" stroke="url(#vineGrad)" stroke-width="3.5" fill="none" vector-effect="non-scaling-stroke" stroke-linecap="round" />
                    <path d="M -2,50 Q 5,80 10,95 Q 50,102 90,95 Q 102,50 95,5 Q 80,-2 50,-2" stroke="#A8E063" stroke-width="1.5" stroke-dasharray="8 6" fill="none" vector-effect="non-scaling-stroke" opacity="0.8" />
                  </svg>
                  
                  <div style="position: absolute; top: 50%; left: -15px; transform: rotate(-80deg); animation: sway 4s infinite alternate;"><svg width="40" height="40" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 70%; left: -5px; transform: rotate(-40deg); animation: sway 3.2s infinite alternate-reverse;"><svg width="35" height="35" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 90%; left: -10px; transform: rotate(-10deg); animation: sway 4.5s infinite alternate;"><svg width="45" height="45" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 97%; left: 20%; transform: rotate(20deg); animation: sway 3.8s infinite alternate-reverse;"><svg width="38" height="38" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 98%; left: 50%; transform: rotate(-20deg); animation: sway 4.1s infinite alternate;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 96%; right: 20%; transform: rotate(40deg); animation: sway 3.5s infinite alternate-reverse;"><svg width="42" height="42" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 88%; right: -15px; transform: rotate(-50deg); animation: sway 4.2s infinite alternate;"><svg width="40" height="40" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 65%; right: -5px; transform: rotate(70deg); animation: sway 3.7s infinite alternate-reverse;"><svg width="35" height="35" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 40%; right: -20px; transform: rotate(-30deg); animation: sway 4.6s infinite alternate;"><svg width="45" height="45" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 20%; right: -5px; transform: rotate(50deg); animation: sway 3.4s infinite alternate-reverse;"><svg width="38" height="38" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: -5px; right: -15px; transform: rotate(-20deg); animation: sway 4.1s infinite alternate;"><svg width="40" height="40" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: -12px; right: 20%; transform: rotate(80deg); animation: sway 3.9s infinite alternate-reverse;"><svg width="42" height="42" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: -8px; right: 40%; transform: rotate(-60deg); animation: sway 4.3s infinite alternate;"><svg width="35" height="35" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                </div>"""

right_card_long_vine = """
                <!-- Main Long Vine for Right-Side Cards (Wrapping Right, Bottom, Left, Top) -->
                <div class="card-botanical-vines right-card-long-vine" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; filter: drop-shadow(0 0 8px rgba(120,255,170,0.25));">
                  <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none" style="overflow: visible; position: absolute; left: 0; top: 0;">
                    <path d="M 102,50 Q 95,80 90,95 Q 50,102 10,95 Q -2,50 5,5 Q 20,-2 50,-2" stroke="url(#vineGrad)" stroke-width="3.5" fill="none" vector-effect="non-scaling-stroke" stroke-linecap="round" />
                    <path d="M 102,50 Q 95,80 90,95 Q 50,102 10,95 Q -2,50 5,5 Q 20,-2 50,-2" stroke="#A8E063" stroke-width="1.5" stroke-dasharray="8 6" fill="none" vector-effect="non-scaling-stroke" opacity="0.8" />
                  </svg>
                  
                  <div style="position: absolute; top: 50%; right: -15px; transform: rotate(80deg); animation: sway 4s infinite alternate;"><svg width="40" height="40" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 70%; right: -5px; transform: rotate(40deg); animation: sway 3.2s infinite alternate-reverse;"><svg width="35" height="35" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 90%; right: -10px; transform: rotate(10deg); animation: sway 4.5s infinite alternate;"><svg width="45" height="45" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 97%; right: 20%; transform: rotate(-20deg); animation: sway 3.8s infinite alternate-reverse;"><svg width="38" height="38" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 98%; right: 50%; transform: rotate(20deg); animation: sway 4.1s infinite alternate;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 96%; left: 20%; transform: rotate(-40deg); animation: sway 3.5s infinite alternate-reverse;"><svg width="42" height="42" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 88%; left: -15px; transform: rotate(50deg); animation: sway 4.2s infinite alternate;"><svg width="40" height="40" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: 65%; left: -5px; transform: rotate(-70deg); animation: sway 3.7s infinite alternate-reverse;"><svg width="35" height="35" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: 40%; left: -20px; transform: rotate(30deg); animation: sway 4.6s infinite alternate;"><svg width="45" height="45" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: 20%; left: -5px; transform: rotate(-50deg); animation: sway 3.4s infinite alternate-reverse;"><svg width="38" height="38" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                  <div style="position: absolute; top: -5px; left: -15px; transform: rotate(20deg); animation: sway 4.1s infinite alternate;"><svg width="40" height="40" viewBox="0 0 30 30"><use href="#botanical-leaf-2"/></svg></div>
                  <div style="position: absolute; top: -12px; left: 20%; transform: rotate(-80deg); animation: sway 3.9s infinite alternate-reverse;"><svg width="42" height="42" viewBox="0 0 30 30"><use href="#botanical-leaf-3"/></svg></div>
                  <div style="position: absolute; top: -8px; left: 40%; transform: rotate(60deg); animation: sway 4.3s infinite alternate;"><svg width="35" height="35" viewBox="0 0 30 30"><use href="#botanical-leaf-1"/></svg></div>
                </div>"""

# We will inject the correct vine block into the tree-card and modify card-content/card-image to have relative z-index
items = re.split(r'(<div class="timeline-item timeline-(right|left)".*?>)', content)
new_content = items[0]
for i in range(1, len(items), 3):
    header = items[i]
    side = items[i+1]
    block = items[i+2]
    
    if side == 'right':
        # card on right, trunk on left. Uses right_card_long_vine
        vine = right_card_long_vine
    else:
        # card on left, trunk on right. Uses left_card_long_vine
        vine = left_card_long_vine
        
    # Find tree-card div and inject the vine right after its opening
    # The div is <div class="timeline-card tree-card">
    block = re.sub(r'(<div class="timeline-card tree-card">)', r'\1\n' + vine, block, count=1)
    
    # Add z-index: 2
    block = block.replace('class="card-image inner-carousel-container"', 'class="card-image inner-carousel-container" style="position: relative; z-index: 2;"')
    block = block.replace('class="card-content"', 'class="card-content" style="position: relative; z-index: 2;"')
    
    new_content += header + block

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Applied vines perfectly and safely.")
