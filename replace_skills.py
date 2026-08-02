import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    new_html = """    <!-- 3. Skills Dashboard Section -->
    <section id="skills" class="skills-redesign-v3">
      <div class="hero-grid">
        <div class="left-panel">
          <h4 class="focus-subtitle">MY FOCUS</h4>
          <h2 class="focus-title">Exploring <br><span class="glowing-accent">Biotechnology</span> &amp; <br><span class="glowing-accent">Bioinformatics</span></h2>
          <p class="focus-desc">
            A biotechnology student passionate about genetics, bioinformatics, and research-driven innovation.<br>Always learning, always growing.
          </p>
          <div class="stats-cards-wrapper">
            <div class="focus-stat-card stat-cyan">
              <div class="focus-stat-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                  <path d="M6 12v5c0 2 2.67 3 6 3s6-1 6-3v-5"/>
                </svg>
              </div>
              <div class="focus-stat-text">
                <span class="fs-number">6+</span>
                <span class="fs-label">NPTEL<br>Certifications</span>
              </div>
            </div>
            <div class="focus-stat-card stat-purple">
              <div class="focus-stat-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="16 18 22 12 16 6"></polyline>
                  <polyline points="8 6 2 12 8 18"></polyline>
                </svg>
              </div>
              <div class="focus-stat-text">
                <span class="fs-number">3+</span>
                <span class="fs-label">Academic<br>Projects</span>
              </div>
            </div>
          </div>
        </div>
        
        <div class="center-panel">
          <div class="holographic-dna-container">
            <div class="dna-glow-base"></div>
            <div class="dna-helix-structure">
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
              <div class="dna-strand"></div>
            </div>
            <div class="dna-ring ring-1"></div>
            <div class="dna-ring ring-2"></div>
            <div class="dna-ring ring-3"></div>
          </div>
        </div>
        
        <div class="right-panel">
          <div class="hologram-card sequence-analysis-card">
            <div class="h-card-header">SEQUENCE ANALYSIS <span class="pulse-dot"></span></div>
            <div class="h-card-body">
              <div class="seq-graph-wave">
                <svg viewBox="0 0 200 40" preserveAspectRatio="none" style="width: 100%; height: 100%;">
                  <path d="M0,20 Q10,5 20,20 T40,20 T60,20 T80,20 T100,20 T120,20 T140,20 T160,20 T180,20 T200,20" fill="none" stroke="var(--color-secondary)" stroke-width="1.5"/>
                  <path d="M0,20 Q10,35 20,20 T40,20 T60,20 T80,20 T100,20 T120,20 T140,20 T160,20 T180,20 T200,20" fill="none" stroke="var(--color-primary)" stroke-width="1.5" stroke-dasharray="4 4" style="opacity:0.5"/>
                </svg>
              </div>
              <div class="seq-data-text">
                ATGCCGTAGCTAACGTTAGCCTAGC<br>
                CGTTAACGTTAGCTAACGTTAGCTA
              </div>
            </div>
          </div>
          
          <div class="lab-equipment-visuals">
             <div class="svg-microscope-wrapper glass-panel">
                <svg class="lab-illustration" viewBox="0 0 100 100">
                  <rect x="25" y="80" width="50" height="10" rx="3" fill="#1e293b" stroke="var(--color-secondary)" stroke-width="1.5"/>
                  <rect x="35" y="75" width="30" height="5" fill="#334155"/>
                  <path d="M35 75 Q25 45 40 25 L45 30 Q35 45 45 75 Z" fill="#334155" stroke="var(--color-secondary)" stroke-width="1"/>
                  <rect x="45" y="55" width="25" height="4" rx="1" fill="#1e293b" stroke="var(--color-primary)" stroke-width="1"/>
                  <rect x="40" y="10" width="10" height="25" transform="rotate(15 45 22.5)" fill="#0f172a" stroke="var(--color-primary)" stroke-width="1.5"/>
                  <rect x="45" y="5" width="8" height="6" transform="rotate(15 45 22.5)" fill="#1e293b" stroke="var(--color-primary)" stroke-width="1"/>
                  <polygon points="48,34 44,45 52,45" fill="#334155" stroke="var(--color-secondary)" stroke-width="1"/>
                  <rect x="45" y="45" width="6" height="4" fill="var(--color-primary)"/>
                  <circle cx="58" cy="55" r="3" fill="var(--color-primary)" filter="blur(2px)"/>
                </svg>
             </div>
             <div class="svg-testtubes-wrapper glass-panel">
                <svg class="lab-illustration" viewBox="0 0 100 100">
                  <rect x="15" y="60" width="70" height="8" rx="2" fill="#1e293b" stroke="var(--color-secondary)" stroke-width="1"/>
                  <rect x="15" y="80" width="70" height="8" rx="2" fill="#1e293b" stroke="var(--color-secondary)" stroke-width="1"/>
                  <rect x="25" y="30" width="10" height="55" rx="5" fill="rgba(255,255,255,0.05)" stroke="var(--color-primary)" stroke-width="1.5"/>
                  <rect x="26" y="60" width="8" height="23" rx="3" fill="rgba(168, 85, 247, 0.6)"/>
                  <circle cx="30" cy="55" r="1.5" fill="#fff" opacity="0.8"/>
                  <rect x="45" y="30" width="10" height="55" rx="5" fill="rgba(255,255,255,0.05)" stroke="var(--color-primary)" stroke-width="1.5"/>
                  <rect x="46" y="50" width="8" height="33" rx="3" fill="rgba(0, 245, 155, 0.6)"/>
                  <circle cx="50" cy="45" r="1.5" fill="#fff" opacity="0.8"/>
                  <rect x="65" y="30" width="10" height="55" rx="5" fill="rgba(255,255,255,0.05)" stroke="var(--color-primary)" stroke-width="1.5"/>
                  <rect x="66" y="65" width="8" height="18" rx="3" fill="rgba(59, 130, 246, 0.6)"/>
                  <circle cx="70" cy="60" r="1.5" fill="#fff" opacity="0.8"/>
                </svg>
             </div>
          </div>
        </div>
      </div>
      
      <div class="skills-grid">
        <div class="biotechnology-card s-card">
          <div class="s-card-header">
            <div class="s-icon icon-cyan">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M6 18h8" />
                <path d="M3 22h18" />
                <path d="M14 22a7 7 0 1 0-14 0" />
                <path d="M9 14h2" />
                <path d="M12 12a2.5 2.5 0 0 0 2-2.5V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v6.5A2.5 2.5 0 0 0 10 12" />
                <path d="M12 3h-2" />
              </svg>
            </div>
            <div class="s-title">
              <h3><span class="text-cyan">01</span> Biotechnology Foundations</h3>
              <p class="text-cyan">Building my lab knowledge</p>
            </div>
          </div>
          <div class="s-card-body">
            <div class="s-skill-item">
              <div class="s-skill-info"><span>PCR & qPCR</span><span>80% Learning</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-cyan" style="width: 80%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Gel Electrophoresis</span><span>70% Learning</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-cyan" style="width: 70%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Cell Culture</span><span>50% Beginner</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-cyan" style="width: 50%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Molecular Cloning</span><span>45% Beginner</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-cyan" style="width: 45%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Cell Biology</span><span>65% Learning</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-cyan" style="width: 65%;"></div></div>
            </div>
          </div>
        </div>

        <div class="bioinformatics-card s-card">
          <div class="s-card-header">
            <div class="s-icon icon-blue">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
                <line x1="8" y1="21" x2="16" y2="21" />
                <line x1="12" y1="17" x2="12" y2="21" />
              </svg>
            </div>
            <div class="s-title">
              <h3><span class="text-blue">02</span> Bioinformatics &amp; Computational Skills</h3>
              <p class="text-blue">Using tools to understand biology</p>
            </div>
          </div>
          <div class="s-card-body">
            <div class="s-skill-item">
              <div class="s-skill-info"><span>BLAST & Sequence Analysis</span><span>75% Intermediate</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-blue" style="width: 75%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Python for Biology</span><span>70% Intermediate</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-blue" style="width: 70%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>R / Bioconductor</span><span>40% Beginner</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-blue" style="width: 40%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Genome Browsers</span><span>60% Intermediate</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-blue" style="width: 60%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Data Visualization</span><span>55% Learning</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-blue" style="width: 55%;"></div></div>
            </div>
          </div>
        </div>

        <div class="research-card s-card">
          <div class="s-card-header">
            <div class="s-icon icon-purple">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10" />
                <path d="M9.5 8.5c0 1.5 2.5 1.5 2.5 3.5s-2.5 2-2.5 3.5" />
              </svg>
            </div>
            <div class="s-title">
              <h3><span class="text-purple">03</span> Research Interests &amp; Concepts</h3>
              <p class="text-purple">Areas I'm passionate about</p>
            </div>
          </div>
          <div class="s-card-body">
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Molecular Genetics</span><span>70% Intermediate</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-purple" style="width: 70%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>CRISPR / Cas Systems</span><span>60% Learning</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-purple" style="width: 60%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Evolutionary Biology</span><span>75% Intermediate</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-purple" style="width: 75%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Genomics</span><span>50% Exploring</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-purple" style="width: 50%;"></div></div>
            </div>
            <div class="s-skill-item">
              <div class="s-skill-info"><span>Biochemistry</span><span>40% Beginner</span></div>
              <div class="s-progress-bar"><div class="s-progress-fill bar-purple" style="width: 40%;"></div></div>
            </div>
          </div>
        </div>
      </div>

      <div class="certifications-section">
        <div class="cert-header">
          <h4 class="cert-section-title">MY NPTEL CERTIFICATIONS</h4>
        </div>
        <div class="cert-cards-flex">
          <div class="cert-card premium-glass">
            <svg class="laurel-icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M32 58C18 58 10 46 10 32C10 20 16 12 24 8" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M32 58C46 58 54 46 54 32C54 20 48 12 40 8" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M10 32l-4 4m6-12l-5 3m8-12l-4 2m10-10l-3 1" stroke-linecap="round" />
              <path d="M54 32l4 4m-6-12l5 3m-8-12l4 2m-10-10l3 1" stroke-linecap="round" />
              <circle cx="32" cy="28" r="12" fill="rgba(0, 210, 196, 0.1)" stroke="#00d2c4" stroke-width="2" />
              <path d="M28 26l4-3 4 3v6h-8z" stroke="#00d2c4" stroke-width="1.5" stroke-linejoin="round" />
              <circle cx="32" cy="28" r="2" fill="#00d2c4" />
            </svg>
            <div class="cert-text-wrap">
              <span class="cert-title">Evolutionary Biology</span>
              <span class="cert-issuer">NPTEL</span>
            </div>
          </div>
          <div class="cert-card premium-glass">
            <svg class="laurel-icon" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M32 58C18 58 10 46 10 32C10 20 16 12 24 8" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M32 58C46 58 54 46 54 32C54 20 48 12 40 8" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M10 32l-4 4m6-12l-5 3m8-12l-4 2m10-10l-3 1" stroke-linecap="round" />
              <path d="M54 32l4 4m-6-12l5 3m-8-12l4 2m-10-10l3 1" stroke-linecap="round" />
              <circle cx="32" cy="28" r="12" fill="rgba(0, 210, 196, 0.1)" stroke="#00d2c4" stroke-width="2" />
              <path d="M28 26l4-3 4 3v6h-8z" stroke="#00d2c4" stroke-width="1.5" stroke-linejoin="round" />
              <circle cx="32" cy="28" r="2" fill="#00d2c4" />
            </svg>
            <div class="cert-text-wrap">
              <span class="cert-title">The Joy of Computing using Python</span>
              <span class="cert-issuer">NPTEL</span>
            </div>
          </div>
        </div>
      </div>
    </section>
"""

    pattern = re.compile(r'<!-- 3\. Skills Dashboard Section -->.*?<!-- 4\. Projects & Research Section -->', re.DOTALL)
    if pattern.search(html_content):
        updated_html = pattern.sub(new_html + "    <!-- 4. Projects & Research Section -->", html_content)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(updated_html)
        print("HTML updated successfully.")
    else:
        print("HTML pattern not found.")

def update_css():
    with open('style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()

    # Remove old skills block 1
    pattern1 = re.compile(r'/\*\s*9\.\s*Skills\s*&\s*Knowledge.*?(?=(/\*\s*10\.))', re.DOTALL | re.IGNORECASE)
    css_content = pattern1.sub("/* OLD SKILLS SECTION DELETED */\n\n", css_content)
    
    # Remove old skills block 2 (NEW SKILLS DASHBOARD CSS)
    pattern2 = re.compile(r'/\*\s*NEW SKILLS DASHBOARD CSS\s*\*/.*', re.DOTALL)
    css_content = pattern2.sub("", css_content)

    new_css = """
/* ==========================================================================
   NEW SKILLS DASHBOARD CSS (GRID REBUILD)
   ========================================================================== */

.skills-redesign-v3 {
  padding: 8rem 0;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 3.5rem;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  background-color: transparent; /* No background image as requested */
}

/* 1. HERO GRID */
.skills-redesign-v3 .hero-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr 1.2fr;
  gap: 2rem;
  align-items: center;
}

/* Left Panel */
.skills-redesign-v3 .left-panel {
  display: flex;
  flex-direction: column;
}
.skills-redesign-v3 .focus-subtitle {
  font-family: var(--font-family-mono, monospace);
  font-size: 0.8rem;
  color: var(--color-primary, #00f59b);
  letter-spacing: 0.15em;
  margin-bottom: 0.5rem;
}
.skills-redesign-v3 .focus-title {
  font-family: var(--font-family-title, sans-serif);
  font-size: 2.8rem;
  line-height: 1.2;
  margin-bottom: 1rem;
  color: #fff;
}
.skills-redesign-v3 .focus-desc {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 2rem;
  line-height: 1.6;
}
.skills-redesign-v3 .stats-cards-wrapper {
  display: flex;
  gap: 1.5rem;
}
.skills-redesign-v3 .focus-stat-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.8rem 1.2rem;
  border-radius: 12px;
  background: rgba(10, 15, 20, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}
.skills-redesign-v3 .stat-cyan {
  border-color: rgba(0, 245, 155, 0.2);
}
.skills-redesign-v3 .stat-purple {
  border-color: rgba(168, 85, 247, 0.2);
}
.skills-redesign-v3 .focus-stat-icon {
  width: 2.5rem;
  height: 2.5rem;
  color: #fff;
}
.stat-cyan .focus-stat-icon { color: #00f59b; }
.stat-purple .focus-stat-icon { color: #a855f7; }

.skills-redesign-v3 .focus-stat-text {
  display: flex;
  flex-direction: column;
}
.skills-redesign-v3 .fs-number {
  font-size: 1.4rem;
  font-weight: bold;
  color: #fff;
  line-height: 1;
}
.skills-redesign-v3 .fs-label {
  font-size: 0.7rem;
  color: rgba(255, 255, 255, 0.6);
  line-height: 1.2;
  margin-top: 0.2rem;
}

/* Center Panel (Holographic DNA) */
.skills-redesign-v3 .center-panel {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  height: 400px;
}
.holographic-dna-container {
  position: relative;
  width: 200px;
  height: 350px;
  display: flex;
  justify-content: center;
  align-items: center;
  perspective: 1000px;
}
.dna-glow-base {
  position: absolute;
  bottom: -20px;
  width: 150px;
  height: 40px;
  background: radial-gradient(ellipse at center, rgba(0, 136, 255, 0.6) 0%, transparent 70%);
  border-radius: 50%;
  filter: blur(10px);
}
.dna-ring {
  position: absolute;
  bottom: -10px;
  border-radius: 50%;
  border: 1px solid rgba(0, 136, 255, 0.5);
  box-shadow: 0 0 15px rgba(0, 136, 255, 0.4);
  transform: rotateX(70deg);
}
.ring-1 { width: 140px; height: 140px; animation: spin-ring 4s linear infinite; }
.ring-2 { width: 100px; height: 100px; animation: spin-ring 3s linear infinite reverse; }
.ring-3 { width: 60px; height: 60px; animation: spin-ring 2s linear infinite; border-width: 2px; }

@keyframes spin-ring {
  to { transform: rotateX(70deg) rotateZ(360deg); }
}

.dna-helix-structure {
  position: relative;
  width: 60px;
  height: 280px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transform-style: preserve-3d;
  animation: rotate-dna 10s linear infinite;
}
.dna-strand {
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, #00f59b, #00d2c4);
  position: relative;
  box-shadow: 0 0 10px #00f59b;
}
.dna-strand::before, .dna-strand::after {
  content: '';
  position: absolute;
  top: -4px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 0 10px #fff;
}
.dna-strand::before { left: -5px; }
.dna-strand::after { right: -5px; }

/* Rotate each strand for double helix effect */
.dna-strand:nth-child(1) { transform: rotateY(0deg); }
.dna-strand:nth-child(2) { transform: rotateY(25deg); }
.dna-strand:nth-child(3) { transform: rotateY(50deg); }
.dna-strand:nth-child(4) { transform: rotateY(75deg); }
.dna-strand:nth-child(5) { transform: rotateY(100deg); }
.dna-strand:nth-child(6) { transform: rotateY(125deg); }
.dna-strand:nth-child(7) { transform: rotateY(150deg); }
.dna-strand:nth-child(8) { transform: rotateY(175deg); }
.dna-strand:nth-child(9) { transform: rotateY(200deg); }
.dna-strand:nth-child(10) { transform: rotateY(225deg); }
.dna-strand:nth-child(11) { transform: rotateY(250deg); }
.dna-strand:nth-child(12) { transform: rotateY(275deg); }
.dna-strand:nth-child(13) { transform: rotateY(300deg); }
.dna-strand:nth-child(14) { transform: rotateY(325deg); }

@keyframes rotate-dna {
  to { transform: rotateY(360deg); }
}

/* Right Panel */
.skills-redesign-v3 .right-panel {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.hologram-card {
  background: rgba(10, 15, 20, 0.6);
  border: 1px solid rgba(0, 210, 196, 0.3);
  border-radius: 12px;
  padding: 1.2rem;
  box-shadow: 0 0 20px rgba(0, 210, 196, 0.1);
  backdrop-filter: blur(10px);
}
.h-card-header {
  font-family: var(--font-family-mono, monospace);
  color: #00d2c4;
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  margin-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.pulse-dot {
  width: 6px;
  height: 6px;
  background-color: #00f59b;
  border-radius: 50%;
  box-shadow: 0 0 8px #00f59b;
  animation: blink 1s infinite alternate;
}
@keyframes blink {
  to { opacity: 0.3; transform: scale(0.8); }
}
.seq-graph-wave {
  height: 40px;
  margin-bottom: 0.5rem;
}
.seq-data-text {
  font-family: var(--font-family-mono, monospace);
  font-size: 0.75rem;
  color: #00f59b;
  letter-spacing: 0.05em;
  opacity: 0.9;
}
.lab-equipment-visuals {
  display: flex;
  gap: 1rem;
}
.glass-panel {
  flex: 1;
  background: rgba(10, 15, 20, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1rem;
  backdrop-filter: blur(10px);
  display: flex;
  justify-content: center;
  align-items: center;
}
.lab-illustration {
  width: 100%;
  max-width: 80px;
  height: auto;
}

/* 2. SKILLS GRID */
.skills-redesign-v3 .skills-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}
.skills-redesign-v3 .s-card {
  background: rgba(10, 15, 20, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 1.5rem;
  backdrop-filter: blur(10px);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.skills-redesign-v3 .s-card:hover {
  transform: translateY(-5px);
}
.biotechnology-card { border-top: 3px solid #00d2c4; }
.biotechnology-card:hover { box-shadow: 0 10px 30px rgba(0, 210, 196, 0.1); }
.bioinformatics-card { border-top: 3px solid #3b82f6; }
.bioinformatics-card:hover { box-shadow: 0 10px 30px rgba(59, 130, 246, 0.1); }
.research-card { border-top: 3px solid #a855f7; }
.research-card:hover { box-shadow: 0 10px 30px rgba(168, 85, 247, 0.1); }

.s-card-header {
  display: flex;
  gap: 1rem;
  align-items: center;
  margin-bottom: 2rem;
}
.s-icon {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px;
}
.s-title h3 {
  font-size: 1.1rem;
  color: #fff;
  margin-bottom: 0.2rem;
}
.s-title p {
  font-size: 0.75rem;
  opacity: 0.7;
}
.text-cyan { color: #00d2c4 !important; }
.text-blue { color: #3b82f6 !important; }
.text-purple { color: #a855f7 !important; }

.s-skill-item {
  margin-bottom: 1.2rem;
}
.s-skill-item:last-child {
  margin-bottom: 0;
}
.s-skill-info {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 0.4rem;
}
.s-progress-bar {
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
  overflow: hidden;
}
.s-progress-fill {
  height: 100%;
  border-radius: 3px;
}
.bar-cyan { background: linear-gradient(90deg, #00f59b, #00d2c4); box-shadow: 0 0 10px rgba(0, 210, 196, 0.5); }
.bar-blue { background: linear-gradient(90deg, #3b82f6, #60a5fa); box-shadow: 0 0 10px rgba(59, 130, 246, 0.5); }
.bar-purple { background: linear-gradient(90deg, #a855f7, #c084fc); box-shadow: 0 0 10px rgba(168, 85, 247, 0.5); }

/* 3. CERTIFICATIONS SECTION */
.skills-redesign-v3 .certifications-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}
.skills-redesign-v3 .cert-header {
  margin-bottom: 2rem;
}
.skills-redesign-v3 .cert-section-title {
  font-family: var(--font-family-mono, monospace);
  font-size: 0.8rem;
  color: #00d2c4;
  letter-spacing: 0.2em;
  text-align: center;
}
.skills-redesign-v3 .cert-cards-flex {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}
.skills-redesign-v3 .cert-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: rgba(10, 15, 20, 0.6);
  border: 1px solid rgba(0, 210, 196, 0.2);
  padding: 1.2rem 2rem;
  border-radius: 12px;
  box-shadow: 0 0 20px rgba(0, 210, 196, 0.05);
  backdrop-filter: blur(10px);
}
.skills-redesign-v3 .laurel-icon {
  width: 40px;
  height: 40px;
  color: #00d2c4;
}
.skills-redesign-v3 .cert-text-wrap {
  display: flex;
  flex-direction: column;
}
.skills-redesign-v3 .cert-title {
  font-weight: bold;
  color: #fff;
  font-size: 1rem;
}
.skills-redesign-v3 .cert-issuer {
  font-size: 0.75rem;
  color: #00d2c4;
  letter-spacing: 0.05em;
  margin-top: 0.2rem;
}

/* RESPONSIVE DESIGN */
@media (max-width: 1024px) {
  .skills-redesign-v3 .hero-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  .skills-redesign-v3 .skills-grid {
    grid-template-columns: 1fr;
  }
  .skills-redesign-v3 .center-panel {
    order: -1;
  }
}
"""
    
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content + new_css)
    print("CSS updated successfully.")

if __name__ == '__main__':
    update_html()
    update_css()
