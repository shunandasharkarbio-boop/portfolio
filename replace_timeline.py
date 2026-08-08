import sys

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<div class="timeline-wrapper tree-growth-wrapper">'
end_marker = '</div><!-- /.timeline-wrapper -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    sys.exit(1)

new_content = """<div class="timeline-wrapper tree-growth-wrapper" style="position: relative; padding: 40px 0;">

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
              <path class="root-strand" d="M400,1470 C350,1490 280,1510 180,1535" stroke="#00F5C3" stroke-width="3" fill="none" opacity="0.6" />
              <path class="root-strand" d="M400,1470 C330,1505 240,1525 120,1540" stroke="#12E7B8" stroke-width="2.5" fill="none" opacity="0.5" />
              <path class="root-strand" d="M400,1470 C450,1490 520,1510 620,1535" stroke="#00F5C3" stroke-width="3" fill="none" opacity="0.6" />
              <path class="root-strand" d="M400,1470 C470,1505 560,1525 680,1540" stroke="#12E7B8" stroke-width="2.5" fill="none" opacity="0.5" />
            </g>

            <!-- Central Trunk -->
            <path class="tree-trunk-path" d="M400,1470 L400,60" stroke="url(#treeTrunkGrad)" stroke-width="4" stroke-linecap="round" fill="none" filter="url(#treeCyanGlow)" />

            <!-- Embedded DNA Core Animation inside Trunk -->
            <path class="tree-dna-core-1" d="M400,1470 Q415,1270 400,1070 Q385,870 400,670 Q415,470 400,270 Q385,70 400,60" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="3 4" fill="none" opacity="0.45" />
            <path class="tree-dna-core-2" d="M400,1470 Q385,1270 400,1070 Q415,870 400,670 Q385,470 400,270 Q415,70 400,60" stroke="#64FFD6" stroke-width="1.5" stroke-dasharray="3 4" fill="none" opacity="0.6" />

            <!-- Horizontal Branches Connecting to Cards -->
            <g class="tree-branch-group" id="branch-item1">
              <path class="tree-branch-path" d="M400,200 L440,200" stroke="url(#branchRightGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="200" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="200" r="3" fill="#64FFD6" />
            </g>
            <g class="tree-branch-group" id="branch-item2">
              <path class="tree-branch-path" d="M400,480 L360,480" stroke="url(#branchLeftGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="480" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="480" r="3" fill="#64FFD6" />
            </g>
            <g class="tree-branch-group" id="branch-item3">
              <path class="tree-branch-path" d="M400,760 L440,760" stroke="url(#branchRightGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="760" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="760" r="3" fill="#64FFD6" />
            </g>
            <g class="tree-branch-group" id="branch-item4">
              <path class="tree-branch-path" d="M400,1040 L360,1040" stroke="url(#branchLeftGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="1040" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="1040" r="3" fill="#64FFD6" />
            </g>
            <g class="tree-branch-group" id="branch-item5">
              <path class="tree-branch-path" d="M400,1320 L440,1320" stroke="url(#branchRightGrad)" stroke-width="3" fill="none" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="1320" r="6" fill="#0a0f14" stroke="#12E7B8" stroke-width="2" filter="url(#treeCyanGlow)" />
              <circle cx="400" cy="1320" r="3" fill="#64FFD6" />
            </g>
          </svg>

          <!-- Floating Bioluminescent Particles -->
          <div class="tree-particles-wrap" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none;">
            <div class="tree-firefly f1"></div>
            <div class="tree-firefly f2"></div>
            <div class="tree-firefly f3"></div>
            <div class="tree-firefly f4"></div>
            <div class="tree-firefly f5"></div>
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
              <div class="timeline-card tree-card" style="width: 42%;">
                <div class="card-border-vines" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10; border-radius: 16px;">
                  <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0; overflow: visible;">
                    <rect x="0" y="0" width="100%" height="100%" rx="16" ry="16" fill="none" stroke="#00F5C3" stroke-width="2" stroke-dasharray="15 10 5 15" opacity="0.8" />
                    <rect x="2" y="2" width="calc(100% - 4px)" height="calc(100% - 4px)" rx="14" ry="14" fill="none" stroke="#12E7B8" stroke-width="1.5" stroke-dasharray="5 15 20 10" opacity="0.6" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(15%, 0);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(50%, 2px);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(85%, 0);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(20%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(65%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(90%, 100%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(0, 25%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(2px, 75%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(100%, 35%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(100%, 65%);" />
                  </svg>
                </div>
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
              <div class="timeline-card tree-card" style="width: 42%;">
                <div class="card-border-vines" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10; border-radius: 16px;">
                  <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0; overflow: visible;">
                    <rect x="0" y="0" width="100%" height="100%" rx="16" ry="16" fill="none" stroke="#00F5C3" stroke-width="2" stroke-dasharray="15 10 5 15" opacity="0.8" />
                    <rect x="2" y="2" width="calc(100% - 4px)" height="calc(100% - 4px)" rx="14" ry="14" fill="none" stroke="#12E7B8" stroke-width="1.5" stroke-dasharray="5 15 20 10" opacity="0.6" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(15%, 0);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(50%, 2px);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(85%, 0);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(20%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(65%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(90%, 100%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(0, 25%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(2px, 75%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(100%, 35%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(100%, 65%);" />
                  </svg>
                </div>
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
              <div class="timeline-card tree-card" style="width: 42%;">
                <div class="card-border-vines" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10; border-radius: 16px;">
                  <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0; overflow: visible;">
                    <rect x="0" y="0" width="100%" height="100%" rx="16" ry="16" fill="none" stroke="#00F5C3" stroke-width="2" stroke-dasharray="15 10 5 15" opacity="0.8" />
                    <rect x="2" y="2" width="calc(100% - 4px)" height="calc(100% - 4px)" rx="14" ry="14" fill="none" stroke="#12E7B8" stroke-width="1.5" stroke-dasharray="5 15 20 10" opacity="0.6" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(15%, 0);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(50%, 2px);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(85%, 0);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(20%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(65%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(90%, 100%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(0, 25%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(2px, 75%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(100%, 35%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(100%, 65%);" />
                  </svg>
                </div>
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
              <div class="timeline-card tree-card" style="width: 42%;">
                <div class="card-border-vines" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10; border-radius: 16px;">
                  <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0; overflow: visible;">
                    <rect x="0" y="0" width="100%" height="100%" rx="16" ry="16" fill="none" stroke="#00F5C3" stroke-width="2" stroke-dasharray="15 10 5 15" opacity="0.8" />
                    <rect x="2" y="2" width="calc(100% - 4px)" height="calc(100% - 4px)" rx="14" ry="14" fill="none" stroke="#12E7B8" stroke-width="1.5" stroke-dasharray="5 15 20 10" opacity="0.6" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(15%, 0);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(50%, 2px);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(85%, 0);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(20%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(65%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(90%, 100%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(0, 25%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(2px, 75%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(100%, 35%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(100%, 65%);" />
                  </svg>
                </div>
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
              <div class="timeline-card tree-card" style="width: 42%;">
                <div class="card-border-vines" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10; border-radius: 16px;">
                  <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0; overflow: visible;">
                    <rect x="0" y="0" width="100%" height="100%" rx="16" ry="16" fill="none" stroke="#00F5C3" stroke-width="2" stroke-dasharray="15 10 5 15" opacity="0.8" />
                    <rect x="2" y="2" width="calc(100% - 4px)" height="calc(100% - 4px)" rx="14" ry="14" fill="none" stroke="#12E7B8" stroke-width="1.5" stroke-dasharray="5 15 20 10" opacity="0.6" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(15%, 0);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(50%, 2px);" />
                    <path d="M0,0 Q4,-8 0,-14 Q-4,-8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(85%, 0);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(20%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(65%, 100%);" />
                    <path d="M0,0 Q4,8 0,14 Q-4,8 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(90%, 100%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(0, 25%);" />
                    <path d="M0,0 Q-8,4 -14,0 Q-8,-4 0,0 Z" fill="#00F5C3" filter="url(#treeCyanGlow)" style="transform: translate(2px, 75%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#12E7B8" filter="url(#treeCyanGlow)" style="transform: translate(100%, 35%);" />
                    <path d="M0,0 Q8,4 14,0 Q8,-4 0,0 Z" fill="#64FFD6" filter="url(#treeCyanGlow)" style="transform: translate(100%, 65%);" />
                  </svg>
                </div>
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
