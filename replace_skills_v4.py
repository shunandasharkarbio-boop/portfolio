import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    new_html = """    <!-- 3. Skills Dashboard Section -->
    <section id="skills" class="skills-premium-dashboard py-large">
      <div class="container-fluid skills-dashboard-container">
        
        <!-- Hero Section: 3 Columns -->
        <div class="skills-hero-grid">
          
          <!-- Left Column: Focus -->
          <div class="hero-col hero-left">
            <h4 class="focus-label">MY FOCUS</h4>
            <h2 class="focus-heading">Exploring <br><span class="cyan-text">Biotechnology</span> &amp; <br><span class="cyan-text">Bioinformatics</span></h2>
            <p class="focus-desc">A biotechnology undergraduate passionate about genetics, bioinformatics, and research-driven innovation.<br>Always learning, always growing.</p>
            <div class="focus-stats">
              <div class="stat-card">
                <div class="stat-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 2 2.67 3 6 3s6-1 6-3v-5"/></svg>
                </div>
                <div class="stat-info">
                  <span class="stat-num">2+</span>
                  <span class="stat-text">NPTEL<br>Certifications</span>
                </div>
              </div>
              <div class="stat-card">
                <div class="stat-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                </div>
                <div class="stat-info">
                  <span class="stat-num">3+</span>
                  <span class="stat-text">Academic<br>Projects</span>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Center Column: Holographic DNA -->
          <div class="hero-col hero-center">
            <div class="center-lab-bg"></div>
            <div class="holo-dna-container">
              <div class="holo-dna">
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
                <div class="dna-strand-wrap"><div class="dna-strand"></div></div>
              </div>
              <div class="holo-platform">
                <div class="platform-ring ring-inner"></div>
                <div class="platform-ring ring-middle"></div>
                <div class="platform-ring ring-outer"></div>
                <div class="platform-base"></div>
              </div>
              <div class="holo-particles"></div>
            </div>
          </div>
          
          <!-- Right Column: Sequence Analysis & Microscope -->
          <div class="hero-col hero-right">
            <div class="sequence-card glass-panel">
              <div class="seq-card-header">SEQUENCE ANALYSIS <span class="dot-pulse"></span></div>
              <div class="seq-card-body">
                <svg class="seq-graph" viewBox="0 0 200 40" preserveAspectRatio="none">
                  <path d="M0,20 L10,5 L20,30 L30,10 L40,20 L50,5 L60,35 L70,15 L80,25 L90,10 L100,20 L110,30 L120,5 L130,20 L140,25 L150,10 L160,30 L170,15 L180,25 L190,5 L200,20" fill="none" stroke="rgba(0, 210, 196, 0.8)" stroke-width="1.5"/>
                  <path d="M0,20 L10,15 L20,10 L30,25 L40,20 L50,15 L60,10 L70,25 L80,15 L90,20 L100,10 L110,15 L120,25 L130,20 L140,10 L150,25 L160,15 L170,25 L180,10 L190,15 L200,20" fill="none" stroke="rgba(59, 130, 246, 0.6)" stroke-width="1" stroke-dasharray="3 3"/>
                </svg>
                <div class="seq-text">
                  ATGCCGTAGCTAACGTTAGCCTAGC<br>
                  CGTTAACGTTAGCTAACGTTAGCTA
                </div>
              </div>
            </div>
            
            <div class="microscope-illustration">
              <svg viewBox="0 0 100 120" class="microscope-svg">
                <!-- Base -->
                <rect x="20" y="100" width="60" height="15" rx="4" fill="#0f172a" stroke="#1e293b" stroke-width="2"/>
                <path d="M25 100 L35 70 L65 70 L75 100 Z" fill="#1e293b" stroke="#334155" stroke-width="2"/>
                <!-- Arm -->
                <path d="M65 70 Q85 45 65 20 L55 20 Q70 45 55 70 Z" fill="#1e293b" stroke="#00d2c4" stroke-width="1.5"/>
                <!-- Stage -->
                <rect x="25" y="65" width="40" height="5" rx="2" fill="#0f172a" stroke="#00d2c4" stroke-width="1"/>
                <circle cx="45" cy="65" r="4" fill="#00d2c4" opacity="0.6" filter="blur(2px)"/>
                <!-- Objective Lenses -->
                <polygon points="40,40 50,40 48,55 42,55" fill="#334155" stroke="#00d2c4" stroke-width="1"/>
                <polygon points="45,40 55,40 58,52 52,52" fill="#1e293b" stroke="#3b82f6" stroke-width="1"/>
                <!-- Tube & Eyepiece -->
                <rect x="42" y="20" width="16" height="20" transform="rotate(-30 50 30)" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
                <rect x="35" y="10" width="12" height="6" transform="rotate(-30 50 30)" fill="#0f172a" stroke="#00d2c4" stroke-width="1.5"/>
                <!-- Focus Knobs -->
                <circle cx="62" cy="75" r="6" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                <circle cx="62" cy="75" r="3" fill="#334155"/>
              </svg>
            </div>
          </div>
          
        </div>
        
        <!-- Skills Grid: 3 Cards -->
        <div class="skills-cards-grid">
          
          <!-- Card 1 -->
          <div class="s-card card-cyan">
            <div class="s-card-header">
              <div class="s-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg></div>
              <div class="s-card-title-area">
                <h3><span class="card-num">01</span> Biotechnology Foundations</h3>
                <p>Building my academic foundation</p>
              </div>
            </div>
            <div class="s-card-body">
              <div class="skill-row"><div class="skill-name">PCR & qPCR</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 80%;"></div></div><div class="skill-pct">80%</div><div class="skill-lvl">Learning</div></div>
              <div class="skill-row"><div class="skill-name">Gel Electrophoresis</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 70%;"></div></div><div class="skill-pct">70%</div><div class="skill-lvl">Learning</div></div>
              <div class="skill-row"><div class="skill-name">Cell Culture</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 50%;"></div></div><div class="skill-pct">50%</div><div class="skill-lvl">Beginner</div></div>
              <div class="skill-row"><div class="skill-name">Molecular Cloning</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 45%;"></div></div><div class="skill-pct">45%</div><div class="skill-lvl">Beginner</div></div>
              <div class="skill-row"><div class="skill-name">Cell Biology</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 65%;"></div></div><div class="skill-pct">65%</div><div class="skill-lvl">Learning</div></div>
            </div>
          </div>
          
          <!-- Card 2 -->
          <div class="s-card card-blue">
            <div class="s-card-header">
              <div class="s-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg></div>
              <div class="s-card-title-area">
                <h3><span class="card-num">02</span> Bioinformatics & Comp Skills</h3>
                <p>Learning tools for biological research</p>
              </div>
            </div>
            <div class="s-card-body">
              <div class="skill-row"><div class="skill-name">BLAST & Seq Analysis</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 75%;"></div></div><div class="skill-pct">75%</div><div class="skill-lvl">Intermediate</div></div>
              <div class="skill-row"><div class="skill-name">Python for Biology</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 70%;"></div></div><div class="skill-pct">70%</div><div class="skill-lvl">Intermediate</div></div>
              <div class="skill-row"><div class="skill-name">R / Bioconductor</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 40%;"></div></div><div class="skill-pct">40%</div><div class="skill-lvl">Beginner</div></div>
              <div class="skill-row"><div class="skill-name">Genome Browsers</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 60%;"></div></div><div class="skill-pct">60%</div><div class="skill-lvl">Intermediate</div></div>
              <div class="skill-row"><div class="skill-name">Data Visualization</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 55%;"></div></div><div class="skill-pct">55%</div><div class="skill-lvl">Learning</div></div>
            </div>
          </div>
          
          <!-- Card 3 -->
          <div class="s-card card-purple">
            <div class="s-card-header">
              <div class="s-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg></div>
              <div class="s-card-title-area">
                <h3><span class="card-num">03</span> Research Interests & Concepts</h3>
                <p>Areas I'm passionate about</p>
              </div>
            </div>
            <div class="s-card-body">
              <div class="skill-row"><div class="skill-name">Molecular Genetics</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 70%;"></div></div><div class="skill-pct">70%</div><div class="skill-lvl">Intermediate</div></div>
              <div class="skill-row"><div class="skill-name">CRISPR/Cas Systems</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 60%;"></div></div><div class="skill-pct">60%</div><div class="skill-lvl">Learning</div></div>
              <div class="skill-row"><div class="skill-name">Evolutionary Biology</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 75%;"></div></div><div class="skill-pct">75%</div><div class="skill-lvl">Intermediate</div></div>
              <div class="skill-row"><div class="skill-name">Genomics</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 50%;"></div></div><div class="skill-pct">50%</div><div class="skill-lvl">Exploring</div></div>
              <div class="skill-row"><div class="skill-name">Biochemistry</div><div class="skill-bar-wrap"><div class="skill-bar" style="width: 40%;"></div></div><div class="skill-pct">40%</div><div class="skill-lvl">Beginner</div></div>
            </div>
          </div>
          
        </div>
        
        <!-- Certification Ribbon -->
        <div class="certification-ribbon glass-panel">
          <div class="ribbon-title">MY NPTEL CERTIFICATIONS</div>
          <div class="ribbon-items">
            <div class="r-item">
              <div class="r-laurel"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
              <div class="r-text">
                <span class="r-name">Evolutionary Biology</span>
                <span class="r-issuer">NPTEL</span>
              </div>
            </div>
            <div class="r-item">
              <div class="r-laurel"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
              <div class="r-text">
                <span class="r-name">Genetic Engineering</span>
                <span class="r-issuer">NPTEL</span>
              </div>
            </div>
            <div class="r-item">
              <div class="r-laurel"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
              <div class="r-text">
                <span class="r-name">The Joy of Computing using Python</span>
                <span class="r-issuer">NPTEL</span>
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </section>"""
    
    # Locate the old skills section (from <!-- 3. Skills Dashboard Section --> to just before <!-- 4. Projects & Research Section -->)
    pattern = re.compile(r'<!-- 3\. Skills & Knowledge Section -->.*?<!-- 4\. Projects & Research Section -->', re.DOTALL)
    
    if pattern.search(html_content):
        updated_html = pattern.sub(new_html + '\n\n    <!-- 4. Projects & Research Section -->', html_content)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(updated_html)
        print("HTML updated successfully.")
    else:
        print("Could not find the skills section in HTML.")

def update_css():
    css_to_add = """
/* ==========================================================================
   PREMIUM SKILLS DASHBOARD REDESIGN
   ========================================================================== */

.skills-premium-dashboard {
  background: transparent;
  width: 100%;
  padding: 6rem 0;
  position: relative;
}

.skills-dashboard-container {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  flex-direction: column;
  gap: 4rem;
}

/* 1. HERO GRID */
.skills-hero-grid {
  display: grid;
  grid-template-columns: 1fr 1.2fr 1fr;
  gap: 2rem;
  align-items: center;
}

/* Left Column */
.hero-col {
  display: flex;
  flex-direction: column;
}
.focus-label {
  color: var(--color-primary);
  font-family: var(--font-family-mono, monospace);
  font-size: 0.8rem;
  letter-spacing: 0.15em;
  margin-bottom: 1rem;
}
.focus-heading {
  font-size: 2.2rem;
  line-height: 1.2;
  margin-bottom: 1.5rem;
  color: #fff;
  font-weight: 700;
}
.cyan-text {
  color: var(--color-primary);
  text-shadow: 0 0 15px rgba(0, 210, 196, 0.4);
}
.focus-desc {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  margin-bottom: 2rem;
}
.focus-stats {
  display: flex;
  gap: 1.5rem;
}
.stat-card {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 0.75rem 1rem;
}
.stat-icon {
  width: 32px;
  height: 32px;
  color: var(--color-primary);
}
.stat-info {
  display: flex;
  flex-direction: column;
}
.stat-num {
  font-weight: 700;
  font-size: 1.2rem;
  color: #fff;
}
.stat-text {
  font-size: 0.65rem;
  color: rgba(255, 255, 255, 0.6);
  text-transform: uppercase;
}

/* Center Column (DNA) */
.hero-center {
  position: relative;
  height: 450px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.holo-dna-container {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  perspective: 1200px;
}
.holo-dna {
  position: relative;
  width: 80px;
  height: 280px;
  transform-style: preserve-3d;
  animation: rotate-dna 12s linear infinite;
  margin-bottom: 20px;
}
.dna-strand-wrap {
  position: absolute;
  width: 100%;
  height: 2px;
  transform-style: preserve-3d;
}
/* Distribute the 14 strands evenly along height and rotation */
.dna-strand-wrap:nth-child(1) { top: 0%; transform: rotateY(0deg); }
.dna-strand-wrap:nth-child(2) { top: 7.6%; transform: rotateY(25deg); }
.dna-strand-wrap:nth-child(3) { top: 15.3%; transform: rotateY(50deg); }
.dna-strand-wrap:nth-child(4) { top: 23%; transform: rotateY(75deg); }
.dna-strand-wrap:nth-child(5) { top: 30.7%; transform: rotateY(100deg); }
.dna-strand-wrap:nth-child(6) { top: 38.4%; transform: rotateY(125deg); }
.dna-strand-wrap:nth-child(7) { top: 46.1%; transform: rotateY(150deg); }
.dna-strand-wrap:nth-child(8) { top: 53.8%; transform: rotateY(175deg); }
.dna-strand-wrap:nth-child(9) { top: 61.5%; transform: rotateY(200deg); }
.dna-strand-wrap:nth-child(10) { top: 69.2%; transform: rotateY(225deg); }
.dna-strand-wrap:nth-child(11) { top: 76.9%; transform: rotateY(250deg); }
.dna-strand-wrap:nth-child(12) { top: 84.6%; transform: rotateY(275deg); }
.dna-strand-wrap:nth-child(13) { top: 92.3%; transform: rotateY(300deg); }
.dna-strand-wrap:nth-child(14) { top: 100%; transform: rotateY(325deg); }

.dna-strand {
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, #3b82f6, #00d2c4, #3b82f6);
  position: relative;
  box-shadow: 0 0 15px #00d2c4;
}
.dna-strand::before, .dna-strand::after {
  content: '';
  position: absolute;
  top: -4px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 0 12px #00d2c4, 0 0 20px #3b82f6;
}
.dna-strand::before { left: -5px; }
.dna-strand::after { right: -5px; }

@keyframes rotate-dna {
  to { transform: rotateY(360deg); }
}

.holo-platform {
  position: relative;
  width: 250px;
  height: 60px;
  perspective: 800px;
  transform-style: preserve-3d;
}
.platform-ring {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%) rotateX(75deg);
  border-radius: 50%;
  border: 2px solid rgba(0, 210, 196, 0.4);
  box-shadow: 0 0 20px rgba(0, 210, 196, 0.2), inset 0 0 15px rgba(0, 210, 196, 0.2);
}
.ring-inner { width: 120px; height: 120px; animation: pulse-ring 2s infinite alternate; }
.ring-middle { width: 180px; height: 180px; border-style: dashed; animation: spin-plat 10s linear infinite; }
.ring-outer { width: 240px; height: 240px; border-color: rgba(59, 130, 246, 0.3); animation: spin-plat 15s linear infinite reverse; }

@keyframes spin-plat { to { transform: translate(-50%, -50%) rotateX(75deg) rotateZ(360deg); } }
@keyframes pulse-ring { to { transform: translate(-50%, -50%) rotateX(75deg) scale(1.05); box-shadow: 0 0 30px rgba(0, 210, 196, 0.5); } }

/* Right Column */
.hero-right {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: flex-end;
}
.glass-panel {
  background: rgba(15, 23, 42, 0.5);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
.sequence-card {
  width: 100%;
  max-width: 300px;
  padding: 1.5rem;
}
.seq-card-header {
  font-family: var(--font-family-mono, monospace);
  color: var(--color-primary);
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}
.dot-pulse {
  width: 6px;
  height: 6px;
  background-color: var(--color-primary);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--color-primary);
  animation: pulse 1.5s infinite alternate;
}
@keyframes pulse { to { opacity: 0.4; transform: scale(0.8); } }
.seq-graph {
  width: 100%;
  height: 40px;
  margin-bottom: 1rem;
}
.seq-text {
  font-family: var(--font-family-mono, monospace);
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  word-wrap: break-word;
}
.microscope-illustration {
  width: 100%;
  max-width: 250px;
  display: flex;
  justify-content: center;
}
.microscope-svg {
  width: 180px;
  height: auto;
  filter: drop-shadow(0 10px 20px rgba(0,0,0,0.5));
}

/* 2. SKILLS CARDS GRID */
.skills-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}
.s-card {
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 2rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.s-card:hover { transform: translateY(-5px); }
.card-cyan { border-top: 3px solid var(--color-primary); }
.card-cyan:hover { box-shadow: 0 10px 30px rgba(0, 210, 196, 0.1); }
.card-blue { border-top: 3px solid #3b82f6; }
.card-blue:hover { box-shadow: 0 10px 30px rgba(59, 130, 246, 0.1); }
.card-purple { border-top: 3px solid #a855f7; }
.card-purple:hover { box-shadow: 0 10px 30px rgba(168, 85, 247, 0.1); }

.s-card-header {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 2.5rem;
}
.s-card-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.card-cyan .s-card-icon { color: var(--color-primary); }
.card-blue .s-card-icon { color: #3b82f6; }
.card-purple .s-card-icon { color: #a855f7; }
.s-card-title-area h3 {
  font-size: 1.2rem;
  color: #fff;
  margin-bottom: 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.card-num {
  font-family: var(--font-family-mono, monospace);
  font-size: 0.9rem;
  opacity: 0.5;
}
.s-card-title-area p {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.5);
}

.skill-row {
  display: grid;
  grid-template-columns: 2fr 3fr 1fr 1fr;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.25rem;
  font-size: 0.85rem;
}
.skill-row:last-child { margin-bottom: 0; }
.skill-name { color: rgba(255, 255, 255, 0.9); }
.skill-bar-wrap {
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
  overflow: hidden;
}
.skill-bar {
  height: 100%;
  border-radius: 3px;
}
.card-cyan .skill-bar { background: var(--color-primary); box-shadow: 0 0 10px rgba(0, 210, 196, 0.5); }
.card-blue .skill-bar { background: #3b82f6; box-shadow: 0 0 10px rgba(59, 130, 246, 0.5); }
.card-purple .skill-bar { background: #a855f7; box-shadow: 0 0 10px rgba(168, 85, 247, 0.5); }
.skill-pct { color: #fff; font-family: var(--font-family-mono, monospace); text-align: right; }
.skill-lvl { color: rgba(255, 255, 255, 0.5); text-align: right; font-size: 0.75rem; }

/* 3. CERTIFICATION RIBBON */
.certification-ribbon {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 3rem;
  border-radius: 100px;
  margin-top: 2rem;
}
.ribbon-title {
  font-family: var(--font-family-mono, monospace);
  font-size: 0.85rem;
  color: var(--color-primary);
  letter-spacing: 0.15em;
  font-weight: 700;
}
.ribbon-items {
  display: flex;
  gap: 3rem;
}
.r-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.r-laurel {
  color: var(--color-primary);
  width: 24px;
  height: 24px;
}
.r-text {
  display: flex;
  flex-direction: column;
}
.r-name { font-size: 0.9rem; color: #fff; font-weight: 500; }
.r-issuer { font-size: 0.7rem; color: rgba(255, 255, 255, 0.5); font-family: var(--font-family-mono, monospace); }

@media (max-width: 1024px) {
  .skills-hero-grid { grid-template-columns: 1fr; gap: 4rem; }
  .skills-cards-grid { grid-template-columns: 1fr; }
  .hero-center { order: -1; }
  .certification-ribbon { flex-direction: column; gap: 1.5rem; border-radius: 24px; padding: 2rem; text-align: center; }
  .ribbon-items { flex-direction: column; gap: 1.5rem; }
}
"""
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(css_to_add)
    print("CSS updated successfully.")

if __name__ == "__main__":
    update_html()
    update_css()
