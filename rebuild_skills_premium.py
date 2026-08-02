import re

# ============================================================
# COMPLETE SKILLS SECTION REBUILD - Premium Reference Match
# ============================================================

NEW_HTML = '''    <!-- 3. Skills Dashboard Section -->
    <section class="skills-dashboard" id="skills">
      
      <!-- HERO ROW: 3 columns full width -->
      <div class="skd-hero-row">
        
        <!-- Left: Focus text -->
        <div class="skd-left">
          <h4 class="skd-focus-label">MY FOCUS</h4>
          <h2 class="skd-focus-heading">
            Exploring <br>
            <span class="skd-cyan">Biotechnology</span> &amp; <br>
            <span class="skd-cyan">Bioinformatics</span>
          </h2>
          <p class="skd-focus-desc">
            A biotechnology student passionate about genetics, bioinformatics, and research-driven innovation. Always learning, always growing.
          </p>
          <div class="skd-stat-row">
            <div class="skd-stat-card skd-stat-cyan">
              <div class="skd-stat-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                  <path d="M6 12v5c0 2 2.67 3 6 3s6-1 6-3v-5"/>
                </svg>
              </div>
              <div class="skd-stat-info">
                <span class="skd-stat-num">6+</span>
                <span class="skd-stat-lbl">NPTEL<br>Certifications</span>
              </div>
            </div>
            <div class="skd-stat-card skd-stat-purple">
              <div class="skd-stat-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="16 18 22 12 16 6"/>
                  <polyline points="8 6 2 12 8 18"/>
                </svg>
              </div>
              <div class="skd-stat-info">
                <span class="skd-stat-num">3+</span>
                <span class="skd-stat-lbl">Academic<br>Projects</span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Center: Holographic DNA Helix -->
        <div class="skd-center">
          <div class="skd-dna-scene">
            <!-- Ambient glow rings -->
            <div class="skd-dna-aura skd-aura-1"></div>
            <div class="skd-dna-aura skd-aura-2"></div>
            <!-- DNA Helix -->
            <div class="skd-dna-helix">
              <div class="skd-helix-inner">
                <!-- Left backbone strand -->
                <svg class="skd-backbone skd-backbone-l" viewBox="0 0 40 320" preserveAspectRatio="none">
                  <path class="skd-strand-path skd-strand-cyan" d="M20,0 C40,40 0,80 20,120 C40,160 0,200 20,240 C40,280 0,320 20,320" fill="none" stroke-width="2.5" stroke-linecap="round"/>
                </svg>
                <!-- Right backbone strand -->
                <svg class="skd-backbone skd-backbone-r" viewBox="0 0 40 320" preserveAspectRatio="none">
                  <path class="skd-strand-path skd-strand-blue" d="M20,0 C0,40 40,80 20,120 C0,160 40,200 20,240 C0,280 40,320 20,320" fill="none" stroke-width="2.5" stroke-linecap="round"/>
                </svg>
                <!-- Base pair rungs -->
                <div class="skd-rungs">
                  <div class="skd-rung" style="top:5%; transform: rotateX(75deg) scaleX(0.3)"></div>
                  <div class="skd-rung" style="top:12%; transform: rotateX(75deg) scaleX(0.6)"></div>
                  <div class="skd-rung" style="top:19%; transform: rotateX(75deg) scaleX(0.85)"></div>
                  <div class="skd-rung" style="top:26%; transform: rotateX(75deg) scaleX(0.95)"></div>
                  <div class="skd-rung" style="top:33%; transform: rotateX(75deg) scaleX(0.80)"></div>
                  <div class="skd-rung" style="top:40%; transform: rotateX(75deg) scaleX(0.55)"></div>
                  <div class="skd-rung" style="top:47%; transform: rotateX(75deg) scaleX(0.20)"></div>
                  <div class="skd-rung" style="top:54%; transform: rotateX(75deg) scaleX(0.50)"></div>
                  <div class="skd-rung" style="top:61%; transform: rotateX(75deg) scaleX(0.80)"></div>
                  <div class="skd-rung" style="top:68%; transform: rotateX(75deg) scaleX(0.95)"></div>
                  <div class="skd-rung" style="top:75%; transform: rotateX(75deg) scaleX(0.85)"></div>
                  <div class="skd-rung" style="top:82%; transform: rotateX(75deg) scaleX(0.60)"></div>
                  <div class="skd-rung" style="top:89%; transform: rotateX(75deg) scaleX(0.30)"></div>
                  <div class="skd-rung" style="top:96%; transform: rotateX(75deg) scaleX(0.10)"></div>
                </div>
                <!-- Glowing node dots on strands -->
                <div class="skd-nodes-l">
                  <div class="skd-node skd-node-c" style="top:19%"></div>
                  <div class="skd-node skd-node-c" style="top:33%"></div>
                  <div class="skd-node skd-node-b" style="top:47%"></div>
                  <div class="skd-node skd-node-c" style="top:61%"></div>
                  <div class="skd-node skd-node-c" style="top:75%"></div>
                  <div class="skd-node skd-node-b" style="top:89%"></div>
                </div>
                <div class="skd-nodes-r">
                  <div class="skd-node skd-node-b" style="top:19%"></div>
                  <div class="skd-node skd-node-b" style="top:33%"></div>
                  <div class="skd-node skd-node-c" style="top:47%"></div>
                  <div class="skd-node skd-node-b" style="top:61%"></div>
                  <div class="skd-node skd-node-b" style="top:75%"></div>
                  <div class="skd-node skd-node-c" style="top:89%"></div>
                </div>
                <!-- Floating particle sparks -->
                <div class="skd-particle p1"></div>
                <div class="skd-particle p2"></div>
                <div class="skd-particle p3"></div>
                <div class="skd-particle p4"></div>
                <div class="skd-particle p5"></div>
              </div>
            </div>
            <!-- Circular holographic platform base -->
            <div class="skd-platform">
              <div class="skd-plat-ring skd-pr1"></div>
              <div class="skd-plat-ring skd-pr2"></div>
              <div class="skd-plat-ring skd-pr3"></div>
              <div class="skd-plat-glow"></div>
            </div>
          </div>
        </div>
        
        <!-- Right: Sequence card + Microscope + Test tubes -->
        <div class="skd-right">
          <!-- Sequence Analysis Card -->
          <div class="skd-seq-card">
            <div class="skd-seq-header">
              SEQUENCE ANALYSIS
              <span class="skd-seq-dot"></span>
            </div>
            <div class="skd-seq-body">
              <svg class="skd-seq-graph" viewBox="0 0 220 42" preserveAspectRatio="none">
                <defs>
                  <linearGradient id="sg1" x1="0" y1="0" x2="1" y2="0">
                    <stop offset="0%" stop-color="#00d2c4"/>
                    <stop offset="100%" stop-color="#3b82f6"/>
                  </linearGradient>
                </defs>
                <polyline points="0,25 15,12 28,30 42,8 55,22 68,14 80,28 94,6 106,20 118,32 130,10 142,24 154,16 168,28 180,10 192,22 205,15 220,25" fill="none" stroke="url(#sg1)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
                <polyline points="0,25 15,30 28,18 42,32 55,22 68,30 80,16 94,28 106,20 118,14 130,28 142,16 154,26 168,14 180,28 192,18 205,25 220,20" fill="none" stroke="rgba(0,210,196,0.35)" stroke-width="1.5" stroke-dasharray="4 3" stroke-linejoin="round"/>
              </svg>
              <div class="skd-seq-text">
                ATGCCGTAGCTAACGTTAGCCTAGC<br>
                CGTTAACGTTAGCTAACGTTAGCTA
              </div>
            </div>
          </div>
          <!-- Microscope + Test Tubes -->
          <div class="skd-lab-art">
            <!-- Microscope SVG -->
            <div class="skd-microscope">
              <svg viewBox="0 0 130 200" class="skd-scope-svg">
                <!-- Base -->
                <ellipse cx="65" cy="185" rx="50" ry="10" fill="#0a1628" stroke="#1e3a5f" stroke-width="2"/>
                <rect x="35" y="175" width="60" height="12" rx="6" fill="#0d1f3c" stroke="#1e3a5f" stroke-width="2"/>
                <!-- Pillar arm -->
                <rect x="58" y="110" width="12" height="68" rx="4" fill="#0d1f3c" stroke="#1a3050" stroke-width="2"/>
                <!-- Horizontal arm -->
                <rect x="38" y="105" width="55" height="12" rx="4" fill="#0d1f3c" stroke="#1e3a5f" stroke-width="2"/>
                <!-- Tube -->
                <rect x="45" y="40" width="14" height="68" rx="4" fill="#091525" stroke="#00d2c4" stroke-width="1.5"/>
                <!-- Objective lenses -->
                <rect x="38" y="108" width="16" height="8" rx="2" fill="#091525" stroke="#00d2c4" stroke-width="1.5"/>
                <rect x="52" y="106" width="10" height="5" rx="2" fill="#091525" stroke="#3b82f6" stroke-width="1"/>
                <!-- Eyepiece -->
                <rect x="42" y="26" width="18" height="16" rx="4" fill="#0a1826" stroke="#00d2c4" stroke-width="2"/>
                <rect x="47" y="20" width="8" height="10" rx="3" fill="#091525" stroke="#00d2c4" stroke-width="1.5"/>
                <!-- Stage -->
                <rect x="28" y="134" width="60" height="6" rx="3" fill="#0d1f3c" stroke="#00d2c4" stroke-width="1.5"/>
                <!-- Stage glow -->
                <ellipse cx="58" cy="142" rx="18" ry="6" fill="none" stroke="rgba(0,210,196,0.4)" stroke-width="2"/>
                <!-- Focus knob -->
                <circle cx="94" cy="128" r="9" fill="#0d1f3c" stroke="#1e3a5f" stroke-width="2"/>
                <circle cx="94" cy="128" r="5" fill="#091525" stroke="#00d2c4" stroke-width="1"/>
                <!-- Arm glow -->
                <line x1="52" y1="42" x2="52" y2="106" stroke="rgba(0,210,196,0.15)" stroke-width="8"/>
                <!-- Base glow -->
                <ellipse cx="65" cy="183" rx="42" ry="6" fill="rgba(0,210,196,0.08)"/>
              </svg>
            </div>
            <!-- Test Tubes -->
            <div class="skd-tubes">
              <div class="skd-tube-wrap">
                <svg viewBox="0 0 28 100" class="skd-tube-svg">
                  <rect x="4" y="5" width="20" height="70" rx="10" fill="rgba(255,255,255,0.04)" stroke="#3b82f6" stroke-width="1.5"/>
                  <rect x="5" y="48" width="18" height="26" rx="9" fill="rgba(59,130,246,0.55)"/>
                  <ellipse cx="14" cy="48" rx="9" ry="4" fill="rgba(59,130,246,0.3)"/>
                  <circle cx="10" cy="42" r="2" fill="rgba(255,255,255,0.5)"/>
                  <rect x="0" y="2" width="28" height="8" rx="3" fill="#0d1f3c" stroke="#1e3a5f" stroke-width="1"/>
                </svg>
                <div class="skd-tube-glow tube-g-blue"></div>
              </div>
              <div class="skd-tube-wrap">
                <svg viewBox="0 0 28 100" class="skd-tube-svg">
                  <rect x="4" y="5" width="20" height="70" rx="10" fill="rgba(255,255,255,0.04)" stroke="#a855f7" stroke-width="1.5"/>
                  <rect x="5" y="40" width="18" height="34" rx="9" fill="rgba(168,85,247,0.6)"/>
                  <ellipse cx="14" cy="40" rx="9" ry="4" fill="rgba(168,85,247,0.3)"/>
                  <circle cx="18" cy="36" r="2" fill="rgba(255,255,255,0.5)"/>
                  <rect x="0" y="2" width="28" height="8" rx="3" fill="#0d1f3c" stroke="#1e3a5f" stroke-width="1"/>
                </svg>
                <div class="skd-tube-glow tube-g-purple"></div>
              </div>
              <div class="skd-tube-wrap">
                <svg viewBox="0 0 28 100" class="skd-tube-svg">
                  <rect x="4" y="5" width="20" height="70" rx="10" fill="rgba(255,255,255,0.04)" stroke="#00d2c4" stroke-width="1.5"/>
                  <rect x="5" y="55" width="18" height="19" rx="9" fill="rgba(0,210,196,0.55)"/>
                  <ellipse cx="14" cy="55" rx="9" ry="4" fill="rgba(0,210,196,0.3)"/>
                  <circle cx="10" cy="50" r="2" fill="rgba(255,255,255,0.5)"/>
                  <rect x="0" y="2" width="28" height="8" rx="3" fill="#0d1f3c" stroke="#1e3a5f" stroke-width="1"/>
                </svg>
                <div class="skd-tube-glow tube-g-cyan"></div>
              </div>
              <div class="skd-tube-wrap">
                <svg viewBox="0 0 28 100" class="skd-tube-svg">
                  <rect x="4" y="5" width="20" height="70" rx="10" fill="rgba(255,255,255,0.04)" stroke="#3b82f6" stroke-width="1.5"/>
                  <rect x="5" y="30" width="18" height="44" rx="9" fill="rgba(59,130,246,0.5)"/>
                  <ellipse cx="14" cy="30" rx="9" ry="4" fill="rgba(59,130,246,0.25)"/>
                  <circle cx="18" cy="26" r="1.5" fill="rgba(255,255,255,0.4)"/>
                  <rect x="0" y="2" width="28" height="8" rx="3" fill="#0d1f3c" stroke="#1e3a5f" stroke-width="1"/>
                </svg>
                <div class="skd-tube-glow tube-g-blue"></div>
              </div>
            </div>
          </div>
        </div>
        
      </div>
      <!-- END HERO ROW -->
      
      <!-- SKILLS CARDS ROW -->
      <div class="skd-cards-row">
        
        <!-- Card 1: Biotechnology Foundations -->
        <div class="skd-card skd-card-cyan">
          <div class="skd-card-head">
            <div class="skd-card-icon-wrap skd-ci-cyan">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 12a2.5 2.5 0 0 0 2-2.5V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v6.5A2.5 2.5 0 0 0 10 12"/>
                <path d="M6 18h8"/><path d="M3 22h18"/>
                <path d="M14 22a7 7 0 1 0-14 0"/>
              </svg>
            </div>
            <div class="skd-card-titles">
              <h3><span class="skd-card-num skd-cyan">01</span> Biotechnology Foundations</h3>
              <p class="skd-cyan">Building my lab knowledge</p>
            </div>
          </div>
          <div class="skd-card-body">
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4.5 10.5C4.5 10.5 6 7.5 12 7.5C18 7.5 19.5 10.5 19.5 10.5M4.5 13.5C4.5 13.5 6 16.5 12 16.5C18 16.5 19.5 13.5 19.5 13.5"/><path d="M8 8.5V15.5M12 7.5V16.5M16 8.5V15.5" stroke-dasharray="1.5 1.5"/></svg>
              <span class="skd-sk-name">PCR &amp; qPCR</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:80%"></div></div>
              <span class="skd-sk-pct">80%</span>
              <span class="skd-sk-lvl skd-cyan">Learning</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="3" width="16" height="18" rx="2"/><line x1="8" y1="3" x2="8" y2="21"/><line x1="12" y1="3" x2="12" y2="21"/><line x1="16" y1="3" x2="16" y2="21"/></svg>
              <span class="skd-sk-name">Gel Electrophoresis</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:70%"></div></div>
              <span class="skd-sk-pct">70%</span>
              <span class="skd-sk-lvl skd-cyan">Learning</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6" stroke-dasharray="2 2" opacity="0.6"/><circle cx="9" cy="9" r="1.5" fill="currentColor" stroke="none"/><circle cx="15" cy="10" r="2" fill="currentColor" stroke="none"/></svg>
              <span class="skd-sk-name">Cell Culture</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:50%"></div></div>
              <span class="skd-sk-pct">50%</span>
              <span class="skd-sk-lvl skd-cyan">Beginner</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="6"/><path d="M12 3v3M12 18v3M3 12h3"/></svg>
              <span class="skd-sk-name">Molecular Cloning</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:45%"></div></div>
              <span class="skd-sk-pct">45%</span>
              <span class="skd-sk-lvl skd-cyan">Beginner</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none"/></svg>
              <span class="skd-sk-name">Cell Biology</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:65%"></div></div>
              <span class="skd-sk-pct">65%</span>
              <span class="skd-sk-lvl skd-cyan">Learning</span>
            </div>
          </div>
        </div>
        
        <!-- Card 2: Bioinformatics -->
        <div class="skd-card skd-card-blue">
          <div class="skd-card-head">
            <div class="skd-card-icon-wrap skd-ci-blue">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="3" width="20" height="14" rx="2"/>
                <line x1="8" y1="21" x2="16" y2="21"/>
                <line x1="12" y1="17" x2="12" y2="21"/>
                <polyline points="10 7 8 9 10 11"/>
                <polyline points="14 11 16 9 14 7"/>
              </svg>
            </div>
            <div class="skd-card-titles">
              <h3><span class="skd-card-num skd-blue">02</span> Bioinformatics<br>&amp; Computational Skills</h3>
              <p class="skd-blue">Using tools to understand biology</p>
            </div>
          </div>
          <div class="skd-card-body">
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="6"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="8" y1="9" x2="14" y2="9" stroke-width="1.5"/><line x1="8" y1="13" x2="12" y2="13" stroke-width="1.5"/></svg>
              <span class="skd-sk-name">BLAST &amp; Sequence Analysis</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:75%"></div></div>
              <span class="skd-sk-pct">75%</span>
              <span class="skd-sk-lvl skd-cyan">Intermediate</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2c-5.52 0-6 1.48-6 4v2h6v1H6c-3.1 0-4 1.76-4 4.5 0 3 1.9 4.5 5 4.5h2v-2.5c0-1.93 1.57-3.5 3.5-3.5h5.5v-3c0-2.52-.48-4-6-4zm-2.5 2.5a.75.75 0 1 1 0 1.5.75.75 0 0 1 0-1.5z"/><path d="M12 22c5.52 0 6-1.48 6-4v-2h-6v-1h6c3.1 0 4-1.76 4-4.5 0-3-1.9-4.5-5-4.5h-2v2.5c0 1.93-1.57 3.5-3.5 3.5H6v3c0 2.52.48 4 6 4zm2.5-4.5a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5z"/></svg>
              <span class="skd-sk-name">Python for Biology</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:70%"></div></div>
              <span class="skd-sk-pct">70%</span>
              <span class="skd-sk-lvl skd-cyan">Intermediate</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M8 6h5a3.5 3.5 0 0 1 0 7H8v5M13 13l4 5"/></svg>
              <span class="skd-sk-name">R / Bioconductor</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:40%"></div></div>
              <span class="skd-sk-pct">40%</span>
              <span class="skd-sk-lvl skd-cyan">Beginner</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="18" rx="2"/><line x1="2" y1="8" x2="22" y2="8"/><rect x="5" y="11" width="14" height="2" rx="1" fill="currentColor" stroke="none" opacity="0.6"/><rect x="8" y="15" width="8" height="2" rx="1" fill="currentColor" stroke="none" opacity="0.6"/></svg>
              <span class="skd-sk-name">Genome Browsers</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:60%"></div></div>
              <span class="skd-sk-pct">60%</span>
              <span class="skd-sk-lvl skd-cyan">Intermediate</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><path d="M3 20h18"/></svg>
              <span class="skd-sk-name">Data Visualization</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-cyan" style="width:55%"></div></div>
              <span class="skd-sk-pct">55%</span>
              <span class="skd-sk-lvl skd-cyan">Learning</span>
            </div>
          </div>
        </div>
        
        <!-- Card 3: Research Interests -->
        <div class="skd-card skd-card-purple">
          <div class="skd-card-head">
            <div class="skd-card-icon-wrap skd-ci-purple">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <path d="M9.5 8.5c0 1.5 2.5 1.5 2.5 3.5s-2.5 2-2.5 3.5M14.5 8.5c0 1.5-2.5 1.5-2.5 3.5s2.5 2 2.5 3.5"/>
                <line x1="10" y1="10" x2="14" y2="10" stroke-width="1.5"/>
                <line x1="10" y1="14" x2="14" y2="14" stroke-width="1.5"/>
              </svg>
            </div>
            <div class="skd-card-titles">
              <h3><span class="skd-card-num skd-purple">03</span> Research Interests<br>&amp; Concepts</h3>
              <p class="skd-purple">Areas I\'m passionate about</p>
            </div>
          </div>
          <div class="skd-card-body">
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4.5 10.5C4.5 10.5 6 7.5 12 7.5C18 7.5 19.5 10.5 19.5 10.5M4.5 13.5C4.5 13.5 6 16.5 12 16.5C18 16.5 19.5 13.5 19.5 13.5"/><line x1="8" y1="8.5" x2="8" y2="15.5" stroke-width="1.5"/><line x1="12" y1="7.5" x2="12" y2="16.5" stroke-width="1.5"/><line x1="16" y1="8.5" x2="16" y2="15.5" stroke-width="1.5"/></svg>
              <span class="skd-sk-name">Molecular Genetics</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-purple" style="width:70%"></div></div>
              <span class="skd-sk-pct">70%</span>
              <span class="skd-sk-lvl skd-purple">Intermediate</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="6" r="2"/><circle cx="9" cy="18" r="2"/><line x1="10.5" y1="7.5" x2="16" y2="15"/><line x1="10.5" y1="16.5" x2="16" y2="9"/></svg>
              <span class="skd-sk-name">CRISPR / Cas Systems</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-purple" style="width:60%"></div></div>
              <span class="skd-sk-pct">60%</span>
              <span class="skd-sk-lvl skd-purple">Learning</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h5M8 6v12M8 6h11M8 18h6M14 14v8M14 14h5M14 22h5"/></svg>
              <span class="skd-sk-name">Evolutionary Biology</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-purple" style="width:75%"></div></div>
              <span class="skd-sk-pct">75%</span>
              <span class="skd-sk-lvl skd-purple">Intermediate</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>
              <span class="skd-sk-name">Genomics</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-purple" style="width:50%"></div></div>
              <span class="skd-sk-pct">50%</span>
              <span class="skd-sk-lvl skd-purple">Exploring</span>
            </div>
            <div class="skd-skill">
              <svg class="skd-sk-icon skd-purple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 2h4M12 2v8M6 22h12M6 22L10 10V4h4v6l4 12"/></svg>
              <span class="skd-sk-name">Biochemistry</span>
              <div class="skd-bar-wrap"><div class="skd-bar skd-bar-purple" style="width:40%"></div></div>
              <span class="skd-sk-pct">40%</span>
              <span class="skd-sk-lvl skd-purple">Beginner</span>
            </div>
          </div>
        </div>
        
      </div>
      <!-- END CARDS ROW -->
      
      <!-- CERTIFICATIONS ROW -->
      <div class="skd-cert-row">
        <h4 class="skd-cert-title">MY NPTEL CERTIFICATIONS</h4>
        <div class="skd-cert-items">
          <div class="skd-cert-item">
            <div class="skd-laurel">
              <svg viewBox="0 0 64 64" fill="none" stroke="#00d2c4" stroke-width="2">
                <path d="M32 58C18 58 10 46 10 32C10 20 16 12 24 8" stroke-linecap="round"/>
                <path d="M32 58C46 58 54 46 54 32C54 20 48 12 40 8" stroke-linecap="round"/>
                <path d="M10 32l-4 4m6-12l-5 3m8-12l-4 2m10-10l-3 1" stroke-linecap="round"/>
                <path d="M54 32l4 4m-6-12l5 3m-8-12l4 2m-10-10l3 1" stroke-linecap="round"/>
                <circle cx="32" cy="28" r="12" fill="rgba(0,210,196,0.08)" stroke="#00d2c4" stroke-width="2"/>
                <path d="M28 26l4-3 4 3v6h-8z" stroke="#00d2c4" stroke-width="1.5" stroke-linejoin="round"/>
                <circle cx="32" cy="28" r="2" fill="#00d2c4"/>
              </svg>
            </div>
            <div class="skd-cert-text">
              <span class="skd-cert-name">Evolutionary Biology</span>
              <span class="skd-cert-org">NPTEL</span>
            </div>
          </div>
          <div class="skd-cert-item">
            <div class="skd-laurel">
              <svg viewBox="0 0 64 64" fill="none" stroke="#00d2c4" stroke-width="2">
                <path d="M32 58C18 58 10 46 10 32C10 20 16 12 24 8" stroke-linecap="round"/>
                <path d="M32 58C46 58 54 46 54 32C54 20 48 12 40 8" stroke-linecap="round"/>
                <path d="M10 32l-4 4m6-12l-5 3m8-12l-4 2m10-10l-3 1" stroke-linecap="round"/>
                <path d="M54 32l4 4m-6-12l5 3m-8-12l4 2m-10-10l3 1" stroke-linecap="round"/>
                <circle cx="32" cy="28" r="12" fill="rgba(0,210,196,0.08)" stroke="#00d2c4" stroke-width="2"/>
                <path d="M28 26l4-3 4 3v6h-8z" stroke="#00d2c4" stroke-width="1.5" stroke-linejoin="round"/>
                <circle cx="32" cy="28" r="2" fill="#00d2c4"/>
              </svg>
            </div>
            <div class="skd-cert-text">
              <span class="skd-cert-name">The Joy of Computing using Python</span>
              <span class="skd-cert-org">NPTEL</span>
            </div>
          </div>
        </div>
      </div>
      <!-- END CERT ROW -->
      
    </section>'''

NEW_CSS = '''
/* ==========================================================================
   SKILLS DASHBOARD — Complete Premium Redesign
   ========================================================================== */
.skills-dashboard {
  background-color: #00060f;
  padding: 0 0 5rem 0;
  color: #e2e8f0;
  font-family: 'Inter', sans-serif;
  overflow: hidden;
  position: relative;
}

/* Dark ambient glow background */
.skills-dashboard::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: 
    radial-gradient(ellipse 60% 40% at 50% 20%, rgba(0,40,80,0.55) 0%, transparent 70%),
    radial-gradient(ellipse 40% 30% at 80% 30%, rgba(0,10,40,0.4) 0%, transparent 60%),
    radial-gradient(ellipse 30% 25% at 20% 60%, rgba(0,20,40,0.3) 0%, transparent 55%);
  pointer-events: none;
  z-index: 0;
}

/* ── HERO ROW ──────────────────────────────────── */
.skd-hero-row {
  display: grid;
  grid-template-columns: 1fr 1.15fr 1fr;
  min-height: 480px;
  align-items: center;
  position: relative;
  z-index: 1;
  padding: 0 3rem;
  max-width: 1300px;
  margin: 0 auto;
  gap: 1rem;
}

/* ── LEFT ───── */
.skd-left {
  padding: 3.5rem 1rem 3.5rem 0;
  display: flex;
  flex-direction: column;
}
.skd-focus-label {
  color: #00d2c4;
  font-size: 0.78rem;
  letter-spacing: 0.18em;
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 0.85rem;
}
.skd-focus-heading {
  font-family: 'Outfit', sans-serif;
  font-size: clamp(2rem, 3vw, 2.8rem);
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 1.1rem;
  color: #fff;
  letter-spacing: -0.02em;
}
.skd-cyan { color: #00d2c4; text-shadow: 0 0 12px rgba(0,210,196,0.35); }
.skd-blue { color: #3b82f6; }
.skd-purple { color: #a855f7; }
.skd-focus-desc {
  color: rgba(255,255,255,0.6);
  font-size: 0.9rem;
  line-height: 1.65;
  margin-bottom: 2rem;
  max-width: 360px;
}
.skd-stat-row {
  display: flex;
  gap: 1rem;
}
.skd-stat-card {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  border-radius: 12px;
  padding: 0.75rem 1.1rem;
  backdrop-filter: blur(10px);
  flex: 1;
}
.skd-stat-cyan {
  background: rgba(0,6,15,0.6);
  border: 1px solid rgba(0,210,196,0.3);
}
.skd-stat-purple {
  background: rgba(0,6,15,0.6);
  border: 1px solid rgba(168,85,247,0.3);
}
.skd-stat-icon {
  width: 38px; height: 38px;
  border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.skd-stat-cyan .skd-stat-icon { background: rgba(0,210,196,0.1); color: #00d2c4; border: 1px solid rgba(0,210,196,0.2); }
.skd-stat-purple .skd-stat-icon { background: rgba(168,85,247,0.1); color: #a855f7; border: 1px solid rgba(168,85,247,0.2); }
.skd-stat-icon svg { width: 20px; height: 20px; }
.skd-stat-info { display: flex; flex-direction: column; }
.skd-stat-num { font-weight: 700; font-size: 1.3rem; color: #fff; line-height: 1; }
.skd-stat-lbl { font-size: 0.62rem; color: rgba(255,255,255,0.55); text-transform: uppercase; letter-spacing: 0.05em; margin-top: 0.2rem; line-height: 1.3; }

/* ── CENTER — DNA HELIX ─────── */
.skd-center {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  padding: 2rem 0;
}
.skd-dna-scene {
  position: relative;
  width: 240px;
  height: 460px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
}
/* Aura glow rings behind helix */
.skd-dna-aura {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
}
.skd-aura-1 {
  width: 280px; height: 280px;
  background: radial-gradient(ellipse, rgba(0,80,200,0.18) 0%, transparent 70%);
  top: 50px; left: 50%; transform: translateX(-50%);
  animation: aura-pulse 4s ease-in-out infinite alternate;
}
.skd-aura-2 {
  width: 200px; height: 200px;
  background: radial-gradient(ellipse, rgba(0,210,196,0.12) 0%, transparent 70%);
  top: 100px; left: 50%; transform: translateX(-50%);
  animation: aura-pulse 3s ease-in-out infinite alternate-reverse;
}
@keyframes aura-pulse {
  to { transform: translateX(-50%) scale(1.15); opacity: 0.7; }
}

/* Helix wrapper */
.skd-dna-helix {
  position: absolute;
  top: 30px;
  width: 100%;
  height: 380px;
  display: flex;
  justify-content: center;
}
.skd-helix-inner {
  position: relative;
  width: 120px;
  height: 100%;
}

/* SVG Backbone paths */
.skd-backbone {
  position: absolute;
  top: 0;
  width: 100%; height: 100%;
}
.skd-backbone-l { left: 0; }
.skd-backbone-r { left: 0; }
.skd-strand-path {
  animation: strand-glow 3s ease-in-out infinite alternate;
}
.skd-strand-cyan {
  stroke: #00d2c4;
  filter: drop-shadow(0 0 4px rgba(0,210,196,0.8));
}
.skd-strand-blue {
  stroke: #3b82f6;
  filter: drop-shadow(0 0 4px rgba(59,130,246,0.8));
}
@keyframes strand-glow {
  to { filter: drop-shadow(0 0 8px rgba(0,210,196,1)); }
}

/* Base pair rungs */
.skd-rungs {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
}
.skd-rung {
  position: absolute;
  left: 50%;
  transform-origin: center;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, rgba(0,210,196,0.7), rgba(59,130,246,0.7));
  border-radius: 1px;
  box-shadow: 0 0 6px rgba(0,210,196,0.5);
  transform: translateX(-50%) rotateX(75deg) scaleX(0.9);
}

/* Glowing nodes on strands */
.skd-nodes-l, .skd-nodes-r {
  position: absolute;
  top: 0; bottom: 0;
  width: 12px;
}
.skd-nodes-l { left: 0; }
.skd-nodes-r { right: 0; }
.skd-node {
  position: absolute;
  width: 10px; height: 10px;
  border-radius: 50%;
  transform: translateX(-50%) translateY(-50%);
  left: 50%;
}
.skd-node-c {
  background: #00d2c4;
  box-shadow: 0 0 10px #00d2c4, 0 0 20px rgba(0,210,196,0.5);
  animation: node-blink 2.5s ease-in-out infinite alternate;
}
.skd-node-b {
  background: #3b82f6;
  box-shadow: 0 0 10px #3b82f6, 0 0 20px rgba(59,130,246,0.5);
  animation: node-blink 2.5s ease-in-out infinite alternate-reverse;
}
@keyframes node-blink {
  to { opacity: 0.5; transform: translateX(-50%) translateY(-50%) scale(0.7); }
}

/* Floating particles */
.skd-particle {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  animation: particle-float linear infinite;
}
.p1 { width:4px;height:4px;background:#00d2c4;left:20%;top:70%;animation-duration:4s;animation-delay:0s;opacity:0.8; }
.p2 { width:3px;height:3px;background:#3b82f6;left:75%;top:50%;animation-duration:5s;animation-delay:0.7s;opacity:0.7; }
.p3 { width:5px;height:5px;background:#00d2c4;left:40%;top:30%;animation-duration:3.5s;animation-delay:1.2s;opacity:0.6; }
.p4 { width:3px;height:3px;background:#a855f7;left:60%;top:80%;animation-duration:4.5s;animation-delay:0.3s;opacity:0.8; }
.p5 { width:4px;height:4px;background:#3b82f6;left:15%;top:40%;animation-duration:3s;animation-delay:1.8s;opacity:0.7; }
@keyframes particle-float {
  0% { transform: translateY(0) translateX(0); opacity: 0.8; }
  50% { transform: translateY(-40px) translateX(10px); opacity: 1; }
  100% { transform: translateY(-80px) translateX(-5px); opacity: 0; }
}

/* Platform base */
.skd-platform {
  position: absolute;
  bottom: 0;
  width: 230px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.skd-plat-ring {
  position: absolute;
  border-radius: 50%;
  transform: rotateX(72deg);
}
.skd-pr1 { width:80px;height:80px;border:1.5px solid rgba(0,210,196,0.6);box-shadow:0 0 15px rgba(0,210,196,0.3);animation:spin-ring 8s linear infinite; }
.skd-pr2 { width:130px;height:130px;border:1px dashed rgba(0,210,196,0.3);animation:spin-ring 12s linear infinite reverse; }
.skd-pr3 { width:190px;height:190px;border:1px solid rgba(59,130,246,0.2);animation:spin-ring 18s linear infinite; }
@keyframes spin-ring {
  to { transform: rotateX(72deg) rotateZ(360deg); }
}
.skd-plat-glow {
  position: absolute;
  width: 160px; height: 20px;
  background: radial-gradient(ellipse, rgba(0,210,196,0.5) 0%, transparent 70%);
  border-radius: 50%;
  bottom: -5px;
  filter: blur(6px);
  animation: glow-pulse 2s ease-in-out infinite alternate;
}
@keyframes glow-pulse {
  to { opacity: 0.5; transform: scaleX(1.2); }
}

/* ── RIGHT ──────────── */
.skd-right {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 2.5rem 0;
  align-items: flex-start;
}

/* Sequence Analysis Card */
.skd-seq-card {
  background: rgba(5,15,30,0.65);
  border: 1px solid rgba(0,210,196,0.2);
  border-radius: 14px;
  padding: 1.1rem 1.3rem;
  width: 100%;
  backdrop-filter: blur(12px);
  box-shadow: 0 0 20px rgba(0,0,0,0.3), inset 0 0 20px rgba(0,30,60,0.2);
}
.skd-seq-header {
  font-family: 'Fira Code', monospace;
  color: #00d2c4;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.8rem;
}
.skd-seq-dot {
  width: 6px; height: 6px;
  background: #00f59b;
  border-radius: 50%;
  box-shadow: 0 0 8px #00f59b;
  animation: dot-blink 1.5s ease-in-out infinite alternate;
}
@keyframes dot-blink { to { opacity: 0.3; } }
.skd-seq-graph { width: 100%; height: 42px; margin-bottom: 0.7rem; }
.skd-seq-text {
  font-family: 'Fira Code', monospace;
  font-size: 0.68rem;
  color: rgba(255,255,255,0.65);
  letter-spacing: 0.08em;
  word-break: break-all;
  line-height: 1.6;
}

/* Lab art: microscope + test tubes */
.skd-lab-art {
  display: flex;
  align-items: flex-end;
  gap: 1.25rem;
  width: 100%;
}

/* Microscope */
.skd-microscope { flex-shrink: 0; }
.skd-scope-svg {
  width: 110px;
  height: auto;
  filter: drop-shadow(0 8px 20px rgba(0,0,0,0.6)) drop-shadow(0 0 8px rgba(0,210,196,0.15));
}

/* Test tubes */
.skd-tubes {
  display: flex;
  align-items: flex-end;
  gap: 0.4rem;
  flex: 1;
  height: 110px;
  padding-bottom: 4px;
}
.skd-tube-wrap {
  position: relative;
  display: flex;
  align-items: flex-end;
  height: 100%;
}
.skd-tube-svg {
  width: 26px;
  height: auto;
  max-height: 100%;
  filter: drop-shadow(0 6px 14px rgba(0,0,0,0.5));
}
.skd-tube-glow {
  position: absolute;
  bottom: -4px;
  left: 50%;
  transform: translateX(-50%);
  width: 18px; height: 8px;
  border-radius: 50%;
  filter: blur(4px);
  animation: tube-glow-anim 2s ease-in-out infinite alternate;
}
.tube-g-blue { background: rgba(59,130,246,0.7); }
.tube-g-purple { background: rgba(168,85,247,0.7); }
.tube-g-cyan { background: rgba(0,210,196,0.7); }
@keyframes tube-glow-anim { to { opacity: 0.5; transform: translateX(-50%) scale(1.3); } }

/* ── SKILLS CARDS ROW ──────────────────── */
.skd-cards-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1.5rem;
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 3rem 3rem;
  position: relative;
  z-index: 1;
}
.skd-card {
  background: rgba(5,12,25,0.55);
  border-radius: 18px;
  padding: 1.6rem 1.4rem;
  backdrop-filter: blur(12px);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid rgba(255,255,255,0.04);
}
.skd-card:hover { transform: translateY(-6px); }
.skd-card-cyan { border: 1px solid rgba(0,210,196,0.2); }
.skd-card-cyan:hover { box-shadow: 0 12px 35px rgba(0,210,196,0.12); }
.skd-card-blue { border: 1px solid rgba(59,130,246,0.2); }
.skd-card-blue:hover { box-shadow: 0 12px 35px rgba(59,130,246,0.12); }
.skd-card-purple { border: 1px solid rgba(168,85,247,0.2); }
.skd-card-purple:hover { box-shadow: 0 12px 35px rgba(168,85,247,0.12); }

.skd-card-head {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.8rem;
  align-items: flex-start;
}
.skd-card-icon-wrap {
  width: 48px; height: 48px;
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.skd-card-icon-wrap svg { width: 22px; height: 22px; }
.skd-ci-cyan { background: rgba(0,210,196,0.1); color: #00d2c4; border: 1px solid rgba(0,210,196,0.25); }
.skd-ci-blue { background: rgba(59,130,246,0.1); color: #3b82f6; border: 1px solid rgba(59,130,246,0.25); }
.skd-ci-purple { background: rgba(168,85,247,0.1); color: #a855f7; border: 1px solid rgba(168,85,247,0.25); }

.skd-card-titles h3 {
  font-family: 'Outfit', sans-serif;
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.3rem;
  line-height: 1.3;
}
.skd-card-num {
  font-family: 'Fira Code', monospace;
  font-size: 0.85rem;
  margin-right: 0.35rem;
  opacity: 0.8;
}
.skd-card-titles p {
  font-size: 0.75rem;
  margin: 0;
}

/* Skill items inside cards */
.skd-card-body { display: flex; flex-direction: column; gap: 1rem; }
.skd-skill {
  display: grid;
  grid-template-columns: 18px 1fr auto auto auto;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
}
.skd-sk-icon { width: 18px; height: 18px; flex-shrink: 0; }
.skd-sk-name { color: rgba(255,255,255,0.88); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.skd-bar-wrap {
  width: 100%;
  height: 5px;
  background: rgba(255,255,255,0.08);
  border-radius: 3px;
  overflow: hidden;
  min-width: 50px;
}
.skd-bar {
  height: 100%;
  border-radius: 3px;
}
.skd-bar-cyan { background: linear-gradient(90deg, #00f59b, #00d2c4); box-shadow: 0 0 8px rgba(0,210,196,0.6); }
.skd-bar-purple { background: linear-gradient(90deg, #a855f7, #c084fc); box-shadow: 0 0 8px rgba(168,85,247,0.6); }
.skd-sk-pct {
  font-family: 'Fira Code', monospace;
  font-size: 0.72rem;
  color: rgba(255,255,255,0.7);
  white-space: nowrap;
}
.skd-sk-lvl {
  font-size: 0.68rem;
  white-space: nowrap;
  opacity: 0.85;
}

/* ── CERT ROW ──────────────────── */
.skd-cert-row {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 3rem 1rem;
  position: relative;
  z-index: 1;
}
.skd-cert-title {
  font-family: 'Fira Code', monospace;
  color: #00d2c4;
  font-size: 0.8rem;
  letter-spacing: 0.18em;
  text-align: center;
  margin-bottom: 1.8rem;
  font-weight: 600;
}
.skd-cert-items {
  display: flex;
  justify-content: center;
  gap: 3rem;
  flex-wrap: wrap;
}
.skd-cert-item {
  display: flex;
  align-items: center;
  gap: 1.1rem;
  background: rgba(5,12,25,0.5);
  border: 1px solid rgba(0,210,196,0.18);
  border-radius: 14px;
  padding: 1rem 2rem;
  backdrop-filter: blur(10px);
}
.skd-laurel { width: 52px; height: 52px; flex-shrink: 0; }
.skd-laurel svg { width: 100%; height: 100%; }
.skd-cert-text { display: flex; flex-direction: column; }
.skd-cert-name { font-size: 0.95rem; font-weight: 600; color: #fff; }
.skd-cert-org { font-family: 'Fira Code', monospace; font-size: 0.72rem; color: #00d2c4; letter-spacing: 0.05em; margin-top: 0.25rem; }

/* ── RESPONSIVE ──── */
@media (max-width: 1100px) {
  .skd-hero-row { grid-template-columns: 1fr 1fr; gap: 2rem; }
  .skd-right { display: none; }
  .skd-cards-row { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 700px) {
  .skd-hero-row { grid-template-columns: 1fr; }
  .skd-center { order: -1; height: 320px; }
  .skd-dna-scene { height: 320px; transform: scale(0.75); }
  .skd-cards-row { grid-template-columns: 1fr; padding: 0 1rem 2rem; }
  .skd-cert-items { flex-direction: column; align-items: center; }
  .skd-hero-row { padding: 0 1rem; }
}
'''

def main():
    # Read files
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    with open('style.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # ── Replace HTML ──────────────────────────────────────────────
    # Locate section from <!-- 3. Skills --> to <!-- 4. Projects -->
    pattern = re.compile(
        r'<!-- 3\. Skills.*?-->\s*<section[^>]+id=["\']skills["\'][^>]*>.*?</section>',
        re.DOTALL
    )
    m = pattern.search(html)
    if m:
        html = html[:m.start()] + NEW_HTML + html[m.end():]
        print("HTML replaced successfully.")
    else:
        print("ERROR: Could not locate skills section in HTML.")
        return

    # ── Replace CSS ───────────────────────────────────────────────
    # Remove all existing skills-dashboard CSS block
    css_pattern = re.compile(
        r'/\* [-\-]+\s*NEW SKILLS DASHBOARD CSS\s*[-\-]+ \*/.*',
        re.DOTALL
    )
    if css_pattern.search(css):
        css = css_pattern.sub('', css)
        print("Old skills CSS removed.")
    else:
        print("No old skills CSS block found — appending only.")

    # Also remove the skills-premium-dashboard block if it was added before
    css_pattern2 = re.compile(
        r'/\* =+\s*PREMIUM SKILLS DASHBOARD.*',
        re.DOTALL
    )
    if css_pattern2.search(css):
        css = css_pattern2.sub('', css)
        print("Old premium skills CSS removed.")

    css = css.rstrip() + '\n' + NEW_CSS

    # Write files
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Done! Files updated.")

if __name__ == '__main__':
    main()
