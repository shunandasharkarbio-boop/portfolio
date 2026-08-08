import sys

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<div class="timeline-wrapper tree-growth-wrapper" style="position: relative; padding: 40px 0;">'
end_marker = '</div><!-- /.timeline-wrapper -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    sys.exit(1)

corner_vines = """
                <div class="elegant-vine-corners" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10;">
                  <svg width="60" height="60" style="position: absolute; top: -5px; left: -5px; overflow: visible;">
                    <path d="M 0,60 Q 5,5 60,0" fill="none" stroke="#00F5C3" stroke-width="2.5" />
                    <path d="M 10,60 Q 15,15 60,10" fill="none" stroke="#12E7B8" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.8" />
                    <path d="M 10,35 Q 0,30 5,20 Q 15,25 10,35 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" />
                    <path d="M 35,10 Q 30,0 20,5 Q 25,15 35,10 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" />
                    <path d="M 25,30 Q 15,25 20,15 Q 30,20 25,30 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: scale(0.7); transform-origin: 20px 20px;" />
                  </svg>
                  <svg width="60" height="60" style="position: absolute; bottom: -5px; right: -5px; overflow: visible;">
                    <path d="M 0,60 Q 55,55 60,0" fill="none" stroke="#00F5C3" stroke-width="2.5" />
                    <path d="M 0,50 Q 45,45 50,0" fill="none" stroke="#12E7B8" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.8" />
                    <path d="M 25,50 Q 35,55 30,65 Q 20,60 25,50 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(15px, -15px);" />
                    <path d="M 50,25 Q 55,35 65,30 Q 60,20 50,25 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(-15px, 15px);" />
                    <path d="M 35,35 Q 45,40 40,50 Q 30,45 35,35 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: scale(0.7) translate(10px, 10px); transform-origin: 40px 40px;" />
                  </svg>
                </div>
"""

new_content = f"""<div class="timeline-wrapper tree-growth-wrapper" style="position: relative; padding: 40px 0;">

          <!-- Bioluminescent SVG Tree Trunk, Branches & Roots -->
          <svg class="tree-svg-container" viewBox="0 0 800 1600" preserveAspectRatio="none" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0;">
            <defs>
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
            </defs>

            <!-- Spreading Organic Roots at Bottom -->
            <g class="tree-roots-group" filter="url(#treeCyanGlow)">
              <path class="root-strand" d="M400,1470 C350,1490 200,1500 50,1540" stroke="#00F5C3" stroke-width="4" stroke-linecap="round" fill="none" opacity="0.8" />
              <path class="root-strand" d="M395,1470 C320,1500 150,1510 100,1550" stroke="#12E7B8" stroke-width="3" fill="none" opacity="0.6" />
              <path class="root-strand" d="M390,1470 C360,1520 280,1530 200,1560" stroke="#64FFD6" stroke-width="2" fill="none" opacity="0.4" />
              <path class="root-strand" d="M400,1470 C450,1490 600,1500 750,1540" stroke="#00F5C3" stroke-width="4" stroke-linecap="round" fill="none" opacity="0.8" />
              <path class="root-strand" d="M405,1470 C480,1500 650,1510 700,1550" stroke="#12E7B8" stroke-width="3" fill="none" opacity="0.6" />
              <path class="root-strand" d="M410,1470 C440,1520 520,1530 600,1560" stroke="#64FFD6" stroke-width="2" fill="none" opacity="0.4" />
              <path class="root-strand" d="M150,1510 C120,1530 80,1535 60,1560" stroke="#00F5C3" stroke-width="1.5" fill="none" opacity="0.5" />
              <path class="root-strand" d="M650,1510 C680,1530 720,1535 740,1560" stroke="#00F5C3" stroke-width="1.5" fill="none" opacity="0.5" />
            </g>

            <!-- Central Trunk with organic curves and thickness gradient -->
            <path class="tree-trunk-base" d="M398,60 C 395,300 405,600 395,900 C 385,1200 388,1400 388,1470 L 412,1470 C 412,1400 415,1200 405,900 C 395,600 405,300 402,60 Z" fill="url(#treeTrunkGrad)" filter="url(#treeCyanGlow)" />
            
            <!-- Bark texture overlay -->
            <g class="trunk-bark-texture">
              <path d="M 400,60 C 397,300 407,600 397,900 C 387,1200 395,1400 395,1470" stroke="#0a0f14" stroke-width="1.5" fill="none" opacity="0.5" stroke-dasharray="10 15" />
              <path d="M 399,60 C 395,300 403,600 399,900 C 389,1200 392,1400 392,1470" stroke="#0a0f14" stroke-width="1" fill="none" opacity="0.4" stroke-dasharray="25 8" />
              <path d="M 401,60 C 398,300 408,600 398,900 C 390,1200 398,1400 398,1470" stroke="#64FFD6" stroke-width="0.5" fill="none" opacity="0.7" stroke-dasharray="15 20" />
            </g>

            <!-- Embedded DNA Core Animation inside Trunk -->
            <path class="tree-dna-core-1" d="M400,1470 Q415,1270 400,1070 Q385,870 400,670 Q415,470 400,270 Q385,70 400,60" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="3 4" fill="none" opacity="0.45" />
            <path class="tree-dna-core-2" d="M400,1470 Q385,1270 400,1070 Q415,870 400,670 Q385,470 400,270 Q415,70 400,60" stroke="#64FFD6" stroke-width="1.5" stroke-dasharray="3 4" fill="none" opacity="0.6" />

            <!-- Horizontal Branches Connecting to Cards EXACTLY AT CARD BORDER (X=464 and X=336) -->
            <g class="tree-branch-group" id="branch-item1">
              <path class="tree-branch-path" d="M400,200 L464,200" stroke="url(#branchRightGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="200" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="200" r="3" fill="#64FFD6" />
            </g>
            <g class="tree-branch-group" id="branch-item2">
              <path class="tree-branch-path" d="M400,480 L336,480" stroke="url(#branchLeftGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="480" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="480" r="3" fill="#64FFD6" />
            </g>
            <g class="tree-branch-group" id="branch-item3">
              <path class="tree-branch-path" d="M400,760 L464,760" stroke="url(#branchRightGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="760" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="760" r="3" fill="#64FFD6" />
            </g>
            <g class="tree-branch-group" id="branch-item4">
              <path class="tree-branch-path" d="M400,1040 L336,1040" stroke="url(#branchLeftGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="1040" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="1040" r="3" fill="#64FFD6" />
            </g>
            <g class="tree-branch-group" id="branch-item5">
              <path class="tree-branch-path" d="M400,1320 L464,1320" stroke="url(#branchRightGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="1320" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="1320" r="3" fill="#64FFD6" />
            </g>
          </svg>

          <!-- Floating Bioluminescent Particles -->
          <div class="tree-particles-wrap" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;">
            <div class="tree-firefly f1" style="width: 2px; height: 2px; animation-duration: 12s;"></div>
            <div class="tree-firefly f2" style="width: 3px; height: 3px; animation-duration: 15s; left: 52%; top: 30%;"></div>
            <div class="tree-firefly f3" style="width: 2px; height: 2px; animation-duration: 10s; left: 47%; top: 50%;"></div>
            <div class="tree-firefly f4" style="width: 4px; height: 4px; animation-duration: 18s; left: 51%; top: 70%;"></div>
            <div class="tree-firefly f5" style="width: 2px; height: 2px; animation-duration: 11s; left: 49%; top: 90%;"></div>
            <div class="tree-firefly f1" style="width: 3px; height: 3px; animation-duration: 14s; left: 45%; top: 20%;"></div>
            <div class="tree-firefly f2" style="width: 2px; height: 2px; animation-duration: 13s; left: 54%; top: 40%;"></div>
            <div class="tree-firefly f3" style="width: 3px; height: 3px; animation-duration: 16s; left: 46%; top: 60%;"></div>
            <div class="tree-firefly f4" style="width: 2px; height: 2px; animation-duration: 12s; left: 53%; top: 80%;"></div>
            <div class="tree-firefly f5" style="width: 3px; height: 3px; animation-duration: 17s; left: 48%; top: 15%;"></div>
          </div>

          <!-- Top Leaf Badge -->
          <div class="tree-top-node-badge" aria-hidden="true" style="position: absolute; top: 20px; left: 50%; transform: translateX(-50%); z-index: 10;">
            <div class="tree-badge-circle leaf-root-circle" style="width: 44px; height: 44px; border-radius: 50%; background: #0a0f14; border: 2px solid #00F5C3; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px rgba(0,245,195,0.4);">
              <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#64FFD6" stroke-width="2">
                <path d="M12 22s8-4 8-10V5l-8 3-8-3v7c0 6 8 10 8 10z" fill="rgba(100,255,214,0.1)"/>
                <path d="M12 22V12" />
                <path d="M12 12c-2-2-4-2-4-2" />
                <path d="M12 16c-1.5-1.5-3-1.5-3-1.5" />
              </svg>
            </div>
          </div>

          <!-- Timeline Items Wrapper -->
          <div style="padding-top: 80px; padding-bottom: 120px; z-index: 5; position: relative;">
          
            <!-- Item 1: Research Interests (Right) -->
            <div class="timeline-item timeline-right" style="margin-bottom: 40px; margin-top: 40px;">
              <div class="timeline-card tree-card" style="width: 42%; position: relative;">
                {corner_vines}
                <div class="card-image inner-carousel-container" data-images="./image/2027-research.jpg" tabindex="0" role="button" aria-label="Zoom image for Research Interests">
                  <div class="inner-carousel-track"></div><button class="inner-carousel-arrow inner-carousel-prev">❮</button><button class="inner-carousel-arrow inner-carousel-next">❯</button><div class="inner-carousel-dots"></div>
                </div>
                <div class="card-content">
                  <div class="card-header-icon" style="font-size: 1.5rem; margin-bottom: 5px; filter: hue-rotate(-50deg) saturate(1.5);">🧬</div>
                  <h3 class="card-title" style="margin-bottom: 10px;">Research Interests</h3>
                  <ul style="padding-left: 20px; list-style-type: disc; margin: 10px 0; font-size: 0.85rem; color: #b0c0d0; line-height: 1.6;">
                    <li style="margin-bottom: 8px;">Genetics &amp; Genetic Engineering</li>
                    <li style="margin-bottom: 8px;">Evolutionary Dynamics</li>
                    <li style="margin-bottom: 8px;">Gene Drive &amp; CRISPR</li>
                  </ul>
                  <p class="card-description" style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 15px; margin-top: 15px; font-size: 0.85rem;">
                    Exploring how gene drive can alter natural evolutionary processes.
                  </p>
                </div>
              </div>
            </div>

            <!-- Item 2: Academics (Left) -->
            <div class="timeline-item timeline-left" style="margin-bottom: 40px; margin-top: 40px;">
              <div class="timeline-card tree-card" style="width: 42%; position: relative;">
                {corner_vines}
                <div class="card-image inner-carousel-container" data-images="./image/2024-btech.jpg/img_1.png" tabindex="0" role="button" aria-label="Zoom image for Academics">
                  <div class="inner-carousel-track"></div><button class="inner-carousel-arrow inner-carousel-prev">❮</button><button class="inner-carousel-arrow inner-carousel-next">❯</button><div class="inner-carousel-dots"></div>
                </div>
                <div class="card-content">
                  <div class="card-header-icon" style="font-size: 1.5rem; margin-bottom: 5px;">🎓</div>
                  <h3 class="card-title" style="margin-bottom: 10px;">Academics</h3>
                  <ul style="padding-left: 20px; list-style-type: disc; margin: 10px 0; font-size: 0.85rem; color: #b0c0d0; line-height: 1.6;">
                    <li style="margin-bottom: 8px;">B.Tech Biotechnology<br>Andhra University</li>
                    <li style="margin-bottom: 8px;">CGPA: 8.12 (till this semester)</li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Item 3: Bioinformatics (Right) -->
            <div class="timeline-item timeline-right" style="margin-bottom: 40px; margin-top: 40px;">
              <div class="timeline-card tree-card" style="width: 42%; position: relative;">
                {corner_vines}
                <div class="card-image inner-carousel-container" data-images="./image/2026-bioinformatics.jpg/img_1.png" tabindex="0" role="button" aria-label="Zoom image for Bioinformatics">
                  <div class="inner-carousel-track"></div><button class="inner-carousel-arrow inner-carousel-prev">❮</button><button class="inner-carousel-arrow inner-carousel-next">❯</button><div class="inner-carousel-dots"></div>
                </div>
                <div class="card-content">
                  <div class="card-header-icon" style="font-size: 1.5rem; margin-bottom: 5px;">💻</div>
                  <h3 class="card-title" style="margin-bottom: 10px;">Bioinformatics</h3>
                  <ul style="padding-left: 20px; list-style-type: disc; margin: 10px 0; font-size: 0.85rem; color: #b0c0d0; line-height: 1.6;">
                    <li style="margin-bottom: 8px;">Galaxy Workflows</li>
                    <li style="margin-bottom: 8px;">Quality Control &amp; Mapping</li>
                    <li style="margin-bottom: 8px;">SNP Analysis (Chromosome 22)</li>
                    <li style="margin-bottom: 8px;">Tools: FastQC, Cutadapt, MultiQC, Bowtie, Samtools, IGV, JBrowser</li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Item 4: Internships (Left) -->
            <div class="timeline-item timeline-left" style="margin-bottom: 40px; margin-top: 40px;">
              <div class="timeline-card tree-card" style="width: 42%; position: relative;">
                {corner_vines}
                <div class="card-image inner-carousel-container" data-images="./image/2025-foundations.jpg/img_1.png" tabindex="0" role="button" aria-label="Zoom image for Internships & Training">
                  <div class="inner-carousel-track"></div><button class="inner-carousel-arrow inner-carousel-prev">❮</button><button class="inner-carousel-arrow inner-carousel-next">❯</button><div class="inner-carousel-dots"></div>
                </div>
                <div class="card-content">
                  <div class="card-header-icon" style="font-size: 1.5rem; margin-bottom: 5px; filter: hue-rotate(-50deg) saturate(1.5);">👩‍🔬</div>
                  <h3 class="card-title" style="margin-bottom: 10px;">Internships &amp; Training</h3>
                  <ul style="padding-left: 20px; list-style-type: disc; margin: 10px 0; font-size: 0.85rem; color: #b0c0d0; line-height: 1.6;">
                    <li style="margin-bottom: 8px;">Medicover Hospital (28 days observation)</li>
                    <li style="margin-bottom: 8px;">CRISPR Internship (Ongoing)</li>
                    <li style="margin-bottom: 8px;">Galaxy &amp; Bioinformatics Training</li>
                    <li style="margin-bottom: 8px;">Lab Skills: Microbiology, Chromatography, Bioanalysis</li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Item 5: Achievements (Right) -->
            <div class="timeline-item timeline-right" style="margin-bottom: 40px; margin-top: 40px;">
              <div class="timeline-card tree-card" style="width: 42%; position: relative;">
                {corner_vines}
                <div class="card-image inner-carousel-container" data-images="./image/2024-btech.jpg/img_3.png" tabindex="0" role="button" aria-label="Zoom image for Achievements">
                  <div class="inner-carousel-track"></div><button class="inner-carousel-arrow inner-carousel-prev">❮</button><button class="inner-carousel-arrow inner-carousel-next">❯</button><div class="inner-carousel-dots"></div>
                </div>
                <div class="card-content">
                  <div class="card-header-icon" style="font-size: 1.5rem; margin-bottom: 5px; filter: hue-rotate(50deg);">🏆</div>
                  <h3 class="card-title" style="margin-bottom: 10px;">Achievements</h3>
                  <ul style="padding-left: 20px; list-style-type: disc; margin: 10px 0; font-size: 0.85rem; color: #b0c0d0; line-height: 1.6;">
                    <li style="margin-bottom: 8px;">NPTEL &ndash; Genetic Engineering</li>
                    <li style="margin-bottom: 8px;">NPTEL &ndash; Evolutionary Dynamics (Elite)</li>
                    <li style="margin-bottom: 8px;">Selected to Present in Pune (11&ndash;12 September)</li>
                    <li style="margin-bottom: 8px;">Duolingo &ndash; Japanese (Score: 10)</li>
                  </ul>
                </div>
              </div>
            </div>
            
          </div>

          <!-- Bottom Spreading Roots DNA Badge -->
          <div class="tree-bottom-node-badge" aria-hidden="true" style="position: absolute; bottom: -20px; left: 50%; transform: translateX(-50%); z-index: 10;">
            <div class="tree-badge-circle dna-root-circle" style="width: 50px; height: 50px; border-radius: 50%; background: #0a0f14; border: 2px solid #00F5C3; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 20px rgba(0,245,195,0.5);">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#00F5C3" stroke-width="1.5">
                <g transform="translate(12, 12) rotate(90) translate(-12, -12)">
                  <path d="M4.5 10.5C4.5 10.5 6 7.5 12 7.5C18 7.5 19.5 10.5 19.5 10.5M4.5 13.5C4.5 13.5 6 16.5 12 16.5C18 16.5 19.5 13.5 19.5 13.5" />
                  <line x1="8" y1="8.5" x2="8" y2="15.5" stroke="#64FFD6" />
                  <line x1="12" y1="7.5" x2="12" y2="16.5" stroke="#64FFD6" />
                  <line x1="16" y1="8.5" x2="16" y2="15.5" stroke="#64FFD6" />
                </g>
              </svg>
            </div>
          </div>

"""

final_content = content[:start_idx] + new_content + content[end_idx:]

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(final_content)

print("Done replacing.")
