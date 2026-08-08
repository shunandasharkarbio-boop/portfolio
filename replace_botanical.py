import sys
import re

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# We need to replace the defs block to inject our leaf defs and keyframes
defs_start = content.find('<defs>')
defs_end = content.find('</defs>') + 7

if defs_start == -1 or defs_end == -1:
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
              <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#81c784" />
                <stop offset="100%" stop-color="#2e7d32" />
              </linearGradient>
              <linearGradient id="leafGradDark" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#66bb6a" />
                <stop offset="100%" stop-color="#1b5e20" />
              </linearGradient>
              <g id="botanical-leaf-1">
                <path d="M15,30 Q15,25 15,20" stroke="#1b5e20" stroke-width="1.5" fill="none" />
                <path d="M15,20 C5,20 0,5 15,0 C30,5 25,20 15,20 Z" fill="url(#leafGrad)" />
                <path d="M15,20 Q15,10 15,2" stroke="#1b5e20" stroke-width="0.75" fill="none" />
              </g>
              <g id="botanical-leaf-2">
                <path d="M15,30 Q15,25 15,20" stroke="#1b5e20" stroke-width="1.2" fill="none" />
                <path d="M15,20 C8,22 2,10 15,2 C28,10 22,22 15,20 Z" fill="url(#leafGradDark)" />
                <path d="M15,20 Q15,12 15,3" stroke="#1b5e20" stroke-width="0.5" fill="none" />
              </g>
              <g id="botanical-leaf-3">
                <path d="M15,30 Q15,27 15,25" stroke="#1b5e20" stroke-width="1" fill="none" />
                <path d="M15,25 C0,25 -5,12 15,5 C35,12 30,25 15,25 Z" fill="url(#leafGrad)" />
                <path d="M15,25 Q15,15 15,6" stroke="#1b5e20" stroke-width="0.5" fill="none" />
              </g>
              <linearGradient id="treeTrunkGrad" x1="0" y1="100%" x2="0" y2="0%">
                <stop offset="0%" stop-color="#12E7B8" stop-opacity="0.4" />
                <stop offset="50%" stop-color="#00F5C3" stop-opacity="0.95" />
                <stop offset="100%" stop-color="#64FFD6" stop-opacity="1" />
              </linearGradient>
              <linearGradient id="branchRightGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#00F5C3" stop-opacity="0.9" />
                <stop offset="100%" stop-color="#12E7B8" stop-opacity="0.3" />
              </linearGradient>
              <linearGradient id="branchLeftGrad" x1="100%" y1="0%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="#00F5C3" stop-opacity="0.9" />
                <stop offset="100%" stop-color="#12E7B8" stop-opacity="0.3" />
              </linearGradient>
              <filter id="treeCyanGlow" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="5" result="blur" />
                <feMerge>
                  <feMergeNode in="blur" />
                  <feMergeNode in="SourceGraphic" />
                </feMerge>
              </filter>
            </defs>"""

content = content[:defs_start] + new_defs + content[defs_end:]

# Replace Branches
b_start = content.find('<!-- Horizontal Branches Connecting to Cards EXACTLY AT CARD BORDER (X=464 and X=336) -->')
b_end = content.find('</svg>', b_start)

if b_start == -1 or b_end == -1:
    print("Branches not found")
    sys.exit(1)

new_branches = """<!-- Natural Botanical Vines Connecting Trunk to Cards (X=464 and X=336) -->
            <g class="tree-branch-group" id="branch-item1">
              <path class="tree-branch-path" d="M400,200 Q432,185 464,200" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,200 Q432,215 464,200" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 4s ease-in-out infinite alternate; transform-origin: 425px 180px;"><use href="#botanical-leaf-2" x="410" y="150" transform="rotate(30, 425, 180)" /></g>
              <g style="animation: sway 3.5s ease-in-out infinite alternate-reverse; transform-origin: 445px 210px;"><use href="#botanical-leaf-1" x="430" y="180" transform="scale(0.8) rotate(130, 445, 210)" /></g>
            </g>
            <g class="tree-branch-group" id="branch-item2">
              <path class="tree-branch-path" d="M400,480 Q368,465 336,480" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,480 Q368,495 336,480" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 3s ease-in-out infinite alternate; transform-origin: 375px 460px;"><use href="#botanical-leaf-1" x="360" y="430" transform="rotate(-30, 375, 460)" /></g>
              <g style="animation: sway 4.5s ease-in-out infinite alternate-reverse; transform-origin: 355px 490px;"><use href="#botanical-leaf-3" x="340" y="460" transform="scale(0.8) rotate(-130, 355, 490)" /></g>
            </g>
            <g class="tree-branch-group" id="branch-item3">
              <path class="tree-branch-path" d="M400,760 Q432,745 464,760" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,760 Q432,775 464,760" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 4s ease-in-out infinite alternate; transform-origin: 425px 740px;"><use href="#botanical-leaf-3" x="410" y="710" transform="rotate(20, 425, 740)" /></g>
              <g style="animation: sway 3.2s ease-in-out infinite alternate-reverse; transform-origin: 445px 770px;"><use href="#botanical-leaf-2" x="430" y="740" transform="scale(0.8) rotate(140, 445, 770)" /></g>
            </g>
            <g class="tree-branch-group" id="branch-item4">
              <path class="tree-branch-path" d="M400,1040 Q368,1025 336,1040" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,1040 Q368,1055 336,1040" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 3.7s ease-in-out infinite alternate; transform-origin: 375px 1020px;"><use href="#botanical-leaf-2" x="360" y="990" transform="rotate(-40, 375, 1020)" /></g>
              <g style="animation: sway 4s ease-in-out infinite alternate-reverse; transform-origin: 355px 1050px;"><use href="#botanical-leaf-1" x="340" y="1020" transform="scale(0.9) rotate(-110, 355, 1050)" /></g>
            </g>
            <g class="tree-branch-group" id="branch-item5">
              <path class="tree-branch-path" d="M400,1320 Q432,1305 464,1320" stroke="#2e7d32" stroke-width="3" fill="none" />
              <path class="tree-branch-path" d="M400,1320 Q432,1335 464,1320" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="8 4" fill="none" />
              <g style="animation: sway 3.5s ease-in-out infinite alternate; transform-origin: 425px 1300px;"><use href="#botanical-leaf-1" x="410" y="1270" transform="rotate(35, 425, 1300)" /></g>
              <g style="animation: sway 4.2s ease-in-out infinite alternate-reverse; transform-origin: 445px 1330px;"><use href="#botanical-leaf-3" x="430" y="1300" transform="scale(0.7) rotate(125, 445, 1330)" /></g>
            </g>
          """

content = content[:b_start] + new_branches + content[b_end:]

# Replace Card Vines
vines_html = """
                <!-- Realistic Botanical Vine Wrap -->
                <div class="card-botanical-vines" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10;">
                  <!-- Main Vine Border -->
                  <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0; overflow: visible;">
                    <rect x="0" y="0" width="100%" height="100%" rx="16" ry="16" fill="none" stroke="#2e7d32" stroke-width="2" opacity="0.9" />
                    <rect x="2" y="2" width="calc(100% - 4px)" height="calc(100% - 4px)" rx="14" ry="14" fill="none" stroke="#4caf50" stroke-width="1.5" stroke-dasharray="12 8" opacity="0.7" />
                  </svg>
                  
                  <!-- Swaying Botanical Leaves hugging corners and edges -->
                  <div style="position: absolute; top: -15px; left: 20px; transform: rotate(-25deg);"><div style="animation: sway 3s ease-in-out infinite alternate; transform-origin: center bottom;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-1" /></svg></div></div>
                  <div style="position: absolute; top: -10px; left: 50px; transform: rotate(15deg);"><div style="animation: sway 3.5s ease-in-out infinite alternate; transform-origin: center bottom;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-2" /></svg></div></div>
                  <div style="position: absolute; top: 15px; right: -15px; transform: rotate(65deg);"><div style="animation: sway 4s ease-in-out infinite alternate; transform-origin: center bottom;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-3" /></svg></div></div>
                  <div style="position: absolute; top: 45px; right: -12px; transform: rotate(105deg);"><div style="animation: sway 2.8s ease-in-out infinite alternate; transform-origin: center bottom;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-1" transform="scale(0.8) origin(15 30)" /></svg></div></div>
                  <div style="position: absolute; bottom: -12px; right: 25px; transform: rotate(155deg);"><div style="animation: sway 4.2s ease-in-out infinite alternate; transform-origin: center bottom;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-2" /></svg></div></div>
                  <div style="position: absolute; bottom: -15px; left: 15px; transform: rotate(-135deg);"><div style="animation: sway 3.1s ease-in-out infinite alternate; transform-origin: center bottom;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-1" /></svg></div></div>
                  <div style="position: absolute; top: 60%; left: -14px; transform: rotate(-75deg);"><div style="animation: sway 3.9s ease-in-out infinite alternate; transform-origin: center bottom;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-3" /></svg></div></div>
                  <div style="position: absolute; bottom: 35%; right: -10px; transform: rotate(85deg);"><div style="animation: sway 3.3s ease-in-out infinite alternate; transform-origin: center bottom;"><svg width="30" height="30" viewBox="0 0 30 30"><use href="#botanical-leaf-2" transform="scale(0.75) origin(15 30)" /></svg></div></div>
                </div>
"""

import re
# The current files have <div class="elegant-vine-corners" ...> ... </div>
# We need to replace that entire div.
content = re.sub(r'<div class="elegant-vine-corners".*?</div>\s*</div>\s*<div class="card-image', vines_html + '                <div class="card-image', content, flags=re.DOTALL)


with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Done replacing.")
