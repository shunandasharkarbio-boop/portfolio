import re

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

left_card_long_vine = """<!-- Main Long Vine for Left-Side Cards (Wrapping Left, Bottom, Right, Top) -->
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

right_card_long_vine = """<!-- Main Long Vine for Right-Side Cards (Wrapping Right, Bottom, Left, Top) -->
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

# Replace left-edge-vine with right_card_long_vine (Because left-edge-vine was for right cards!)
content = re.sub(r'<!-- Left-Edge Botanical Vine -->.*?</div>\s*<div class="card-image', right_card_long_vine + '\n                  <div class="card-image', content, flags=re.DOTALL)

# Replace right-edge-vine with left_card_long_vine
content = re.sub(r'<!-- Right-Edge Botanical Vine -->.*?</div>\s*<div class="card-image', left_card_long_vine + '\n                  <div class="card-image', content, flags=re.DOTALL)

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done replacing with large long wrapping vines.")
