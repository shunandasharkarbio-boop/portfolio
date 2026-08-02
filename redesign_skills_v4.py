import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    new_html = """    <!-- 3. Skills Dashboard Section -->
    <section id="skills" class="skills-dashboard-v4">
      <div class="skills-container-v4">
        
        <!-- Hero Section -->
        <div class="skills-hero-v4">
          
          <!-- Left Column -->
          <div class="sh-left">
            <span class="sh-label">MY FOCUS</span>
            <h2 class="sh-heading">Exploring Biotechnology &amp; Bioinformatics</h2>
            <p class="sh-desc">A biotechnology undergraduate passionate about genetics, bioinformatics, and research-driven innovation. Always learning, always growing.</p>
            <div class="sh-stats">
              <div class="sh-stat-card">
                <span class="sh-stat-num">2+</span>
                <span class="sh-stat-text">NPTEL Certifications</span>
              </div>
              <div class="sh-stat-card">
                <span class="sh-stat-num">3+</span>
                <span class="sh-stat-text">Academic Projects</span>
              </div>
            </div>
          </div>

          <!-- Center Column -->
          <div class="sh-center">
            <div class="blurred-lab-bg"></div>
            <div class="holo-dna-wrapper">
              <div class="holo-dna-platform"></div>
              <div class="holo-dna">
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
                <div class="holo-strand"></div>
              </div>
              <div class="holo-particles">
                <div class="p-dot" style="--dx: 20px; --dy: -40px; --dur: 3s; --delay: 0s;"></div>
                <div class="p-dot" style="--dx: -30px; --dy: -60px; --dur: 4s; --delay: 1s;"></div>
                <div class="p-dot" style="--dx: 15px; --dy: -80px; --dur: 3.5s; --delay: 0.5s;"></div>
                <div class="p-dot" style="--dx: -15px; --dy: -30px; --dur: 2.5s; --delay: 2s;"></div>
                <div class="p-dot" style="--dx: 35px; --dy: -70px; --dur: 4.5s; --delay: 1.5s;"></div>
              </div>
            </div>
          </div>

          <!-- Right Column -->
          <div class="sh-right">
            <div class="floating-seq-card">
              <div class="fsc-header">SEQUENCE ANALYSIS</div>
              <svg viewBox="0 0 100 20" class="fsc-wave" preserveAspectRatio="none">
                <path d="M0,10 Q5,0 10,10 T20,10 T30,10 T40,10 T50,10 T60,10 T70,10 T80,10 T90,10 T100,10" fill="none" stroke="rgba(0, 245, 155, 0.7)" stroke-width="1"/>
              </svg>
              <div class="fsc-data">
                ATGCCGTAGCTAACGTTAGCCTAGC<br>
                CGTTAACGTTAGCTAACGTTAGCTA
              </div>
            </div>
            
            <div class="microscope-art">
              <svg viewBox="0 0 100 100" class="m-svg">
                <path d="M20,85 L80,85 Q85,85 85,90 L15,90 Q15,85 20,85 Z" fill="#0f172a" stroke="rgba(0,245,155,0.3)" stroke-width="0.5"/>
                <path d="M30,85 L35,40 Q40,15 50,15 L60,15 L60,20 L50,20 Q45,20 40,40 L35,85 Z" fill="#1e293b" stroke="rgba(0,245,155,0.2)" stroke-width="0.5"/>
                <path d="M40,55 L75,55 L75,60 L40,60 Z" fill="#0f172a" stroke="rgba(0,245,155,0.4)" stroke-width="0.5"/>
                <path d="M55,10 L70,35 L65,38 L50,13 Z" fill="#020617" stroke="rgba(0,245,155,0.5)" stroke-width="1"/>
                <circle cx="67" cy="40" r="4" fill="#00f59b" filter="drop-shadow(0 0 4px #00f59b)"/>
                <circle cx="58" cy="40" r="3" fill="#00d2c4"/>
                <line x1="55" y1="55" x2="55" y2="50" stroke="#00f59b" stroke-width="1.5" filter="drop-shadow(0 0 2px #00f59b)"/>
                <path d="M48,8 L53,15 L48,18 L43,11 Z" fill="#334155"/>
                <ellipse cx="58" cy="53" rx="8" ry="2" fill="rgba(0,245,155,0.6)" filter="blur(2px)"/>
              </svg>
            </div>
          </div>
          
        </div>

        <!-- 3 Cards Grid -->
        <div class="skills-cards-v4">
          
          <div class="sk-glass-card">
            <div class="sk-card-header">
              <h3>Biotechnology Foundations</h3>
              <span>Building my academic foundation</span>
            </div>
            <div class="sk-card-body">
              <div class="sk-row"><div class="sk-info"><span>PCR &amp; qPCR</span><span class="sk-lvl">Learning</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 80%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Gel Electrophoresis</span><span class="sk-lvl">Learning</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 70%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Cell Culture</span><span class="sk-lvl">Beginner</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 50%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Molecular Cloning</span><span class="sk-lvl">Beginner</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 45%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Cell Biology</span><span class="sk-lvl">Learning</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 65%;"></div></div></div>
            </div>
          </div>

          <div class="sk-glass-card">
            <div class="sk-card-header">
              <h3>Bioinformatics &amp; Computational Skills</h3>
              <span>Learning tools for biological research</span>
            </div>
            <div class="sk-card-body">
              <div class="sk-row"><div class="sk-info"><span>BLAST &amp; Sequence Analysis</span><span class="sk-lvl">Intermediate</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 75%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Python for Biology</span><span class="sk-lvl">Intermediate</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 70%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>R / Bioconductor</span><span class="sk-lvl">Beginner</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 40%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Genome Browsers</span><span class="sk-lvl">Intermediate</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 60%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Data Visualization</span><span class="sk-lvl">Learning</span></div><div class="sk-bar-bg"><div class="sk-bar-fill" style="width: 55%;"></div></div></div>
            </div>
          </div>

          <div class="sk-glass-card">
            <div class="sk-card-header">
              <h3>Research Interests &amp; Concepts</h3>
              <span>Areas I'm passionate about</span>
            </div>
            <div class="sk-card-body">
              <div class="sk-row"><div class="sk-info"><span>Molecular Genetics</span></div><div class="sk-bar-bg concept-bar"><div class="sk-bar-fill" style="width: 70%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>CRISPR/Cas Systems</span></div><div class="sk-bar-bg concept-bar"><div class="sk-bar-fill" style="width: 60%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Evolutionary Biology</span></div><div class="sk-bar-bg concept-bar"><div class="sk-bar-fill" style="width: 75%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Genomics</span></div><div class="sk-bar-bg concept-bar"><div class="sk-bar-fill" style="width: 50%;"></div></div></div>
              <div class="sk-row"><div class="sk-info"><span>Biochemistry</span></div><div class="sk-bar-bg concept-bar"><div class="sk-bar-fill" style="width: 40%;"></div></div></div>
            </div>
          </div>

        </div>

        <!-- Slim Certification Ribbon -->
        <div class="cert-ribbon-v4">
          <div class="cr-title">My NPTEL Certifications</div>
          <div class="cr-divider"></div>
          <div class="cr-item">Evolutionary Biology (NPTEL)</div>
          <div class="cr-dot">&bull;</div>
          <div class="cr-item">Genetic Engineering (NPTEL)</div>
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

    # Remove the V3 CSS
    pattern2 = re.compile(r'/\*\s*==========================================================================\s*NEW SKILLS DASHBOARD CSS \(GRID REBUILD\)\s*==========================================================================\s*\*/.*', re.DOTALL)
    css_content = pattern2.sub("", css_content)

    new_css = """
/* ==========================================================================
   SKILLS DASHBOARD V4 (PREMIUM FUTURISTIC RESEARCH THEME)
   ========================================================================== */

.skills-dashboard-v4 {
  padding: 8rem 0;
  width: 100%;
  background-color: var(--bg-dark-obsidian, #050807);
  position: relative;
  overflow: hidden;
  font-family: var(--font-family-body, 'Inter', sans-serif);
}

.skills-container-v4 {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  flex-direction: column;
  gap: 4rem;
}

/* --- HERO SECTION --- */
.skills-hero-v4 {
  display: grid;
  grid-template-columns: 1.1fr 1fr 1fr;
  gap: 3rem;
  align-items: center;
  position: relative;
}

/* Left Column */
.sh-left {
  display: flex;
  flex-direction: column;
}
.sh-label {
  font-family: var(--font-family-mono, 'Fira Code', monospace);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  color: #00f59b;
  margin-bottom: 1rem;
}
.sh-heading {
  font-family: var(--font-family-title, 'Outfit', sans-serif);
  font-size: 3.2rem;
  line-height: 1.1;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 1.25rem;
}
.sh-desc {
  font-size: 1rem;
  color: #8e9fa0;
  line-height: 1.6;
  margin-bottom: 2.5rem;
}
.sh-stats {
  display: flex;
  gap: 1.5rem;
}
.sh-stat-card {
  background: rgba(12, 18, 15, 0.6);
  border: 1px solid rgba(0, 245, 155, 0.15);
  border-radius: 8px;
  padding: 0.8rem 1.2rem;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  backdrop-filter: blur(8px);
}
.sh-stat-num {
  font-size: 1.4rem;
  font-weight: 700;
  color: #00f59b;
}
.sh-stat-text {
  font-size: 0.7rem;
  color: #caced1;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  line-height: 1.2;
}

/* Center Column */
.sh-center {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 450px;
}
.blurred-lab-bg {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 150%;
  height: 150%;
  background: radial-gradient(circle, rgba(0,245,155,0.05) 0%, transparent 60%);
  filter: blur(20px);
  z-index: 0;
  pointer-events: none;
}
.holo-dna-wrapper {
  position: relative;
  z-index: 1;
  width: 140px;
  height: 380px;
  display: flex;
  justify-content: center;
  align-items: center;
  perspective: 1000px;
}
.holo-dna-platform {
  position: absolute;
  bottom: -20px;
  width: 160px;
  height: 30px;
  border-radius: 50%;
  background: radial-gradient(ellipse at center, rgba(0,245,155,0.4) 0%, transparent 70%);
  box-shadow: 0 0 20px rgba(0,245,155,0.3);
  border: 1px solid rgba(0,245,155,0.2);
  transform: rotateX(75deg);
}
.holo-dna {
  position: relative;
  width: 70px;
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transform-style: preserve-3d;
  animation: rotate-dna-y 8s linear infinite;
}
.holo-strand {
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, #00f59b, #00d2c4);
  position: relative;
  box-shadow: 0 0 8px #00f59b;
}
.holo-strand::before, .holo-strand::after {
  content: '';
  position: absolute;
  top: -3px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 0 10px #00f59b, 0 0 5px #fff;
}
.holo-strand::before { left: -4px; }
.holo-strand::after { right: -4px; }

.holo-strand:nth-child(1) { transform: rotateY(0deg); }
.holo-strand:nth-child(2) { transform: rotateY(30deg); }
.holo-strand:nth-child(3) { transform: rotateY(60deg); }
.holo-strand:nth-child(4) { transform: rotateY(90deg); }
.holo-strand:nth-child(5) { transform: rotateY(120deg); }
.holo-strand:nth-child(6) { transform: rotateY(150deg); }
.holo-strand:nth-child(7) { transform: rotateY(180deg); }
.holo-strand:nth-child(8) { transform: rotateY(210deg); }
.holo-strand:nth-child(9) { transform: rotateY(240deg); }
.holo-strand:nth-child(10) { transform: rotateY(270deg); }
.holo-strand:nth-child(11) { transform: rotateY(300deg); }
.holo-strand:nth-child(12) { transform: rotateY(330deg); }

@keyframes rotate-dna-y {
  to { transform: rotateY(360deg); }
}

/* Subtle Particles */
.holo-particles {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  pointer-events: none;
}
.p-dot {
  position: absolute;
  bottom: 10%;
  left: 50%;
  width: 4px;
  height: 4px;
  background: #00f59b;
  border-radius: 50%;
  box-shadow: 0 0 6px #00f59b;
  opacity: 0;
  animation: float-particle var(--dur) ease-in-out infinite;
  animation-delay: var(--delay);
}
@keyframes float-particle {
  0% { transform: translate(0, 0) scale(0.5); opacity: 0; }
  50% { opacity: 0.8; }
  100% { transform: translate(var(--dx), var(--dy)) scale(1.2); opacity: 0; }
}

/* Right Column */
.sh-right {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: flex-end; /* Push to right, remove black space */
}
.floating-seq-card {
  background: rgba(12, 18, 15, 0.7);
  border: 1px solid rgba(0, 245, 155, 0.2);
  border-radius: 12px;
  padding: 1.25rem;
  width: 100%;
  max-width: 280px;
  backdrop-filter: blur(12px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 15px rgba(0,245,155,0.05);
  animation: float-card 6s ease-in-out infinite;
}
@keyframes float-card {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
.fsc-header {
  font-family: var(--font-family-mono, monospace);
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  color: #00d2c4;
  margin-bottom: 0.8rem;
}
.fsc-wave {
  width: 100%;
  height: 30px;
  margin-bottom: 0.8rem;
}
.fsc-data {
  font-family: var(--font-family-mono, monospace);
  font-size: 0.7rem;
  color: #00f59b;
  letter-spacing: 0.08em;
  line-height: 1.5;
  opacity: 0.9;
}
.microscope-art {
  width: 100%;
  max-width: 280px;
  display: flex;
  justify-content: flex-end;
  padding-right: 1rem;
}
.m-svg {
  width: 140px;
  height: 140px;
  filter: drop-shadow(0 15px 25px rgba(0,0,0,0.6));
}

/* --- 3 CARDS GRID --- */
.skills-cards-v4 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}
.sk-glass-card {
  background: rgba(12, 18, 15, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-top: 1px solid rgba(0, 245, 155, 0.3);
  border-radius: 16px;
  padding: 2rem;
  backdrop-filter: blur(10px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  transition: transform 0.3s ease, border-color 0.3s ease;
}
.sk-glass-card:hover {
  transform: translateY(-5px);
  border-top-color: #00f59b;
  box-shadow: 0 15px 40px rgba(0,245,155,0.1);
}
.sk-card-header {
  margin-bottom: 2rem;
}
.sk-card-header h3 {
  font-family: var(--font-family-title, sans-serif);
  font-size: 1.25rem;
  color: #fff;
  margin-bottom: 0.4rem;
}
.sk-card-header span {
  font-size: 0.8rem;
  color: #8e9fa0;
}
.sk-card-body {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}
.sk-row {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.sk-info {
  display: flex;
  justify-content: space-between;
  font-size: 0.85rem;
  color: #e2e8f0;
}
.sk-lvl {
  font-size: 0.75rem;
  color: #00d2c4;
  opacity: 0.9;
}
.sk-bar-bg {
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 2px;
  overflow: hidden;
}
.sk-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #00f59b, #00d2c4);
  border-radius: 2px;
  box-shadow: 0 0 8px rgba(0, 245, 155, 0.5);
}
.concept-bar .sk-bar-fill {
  background: linear-gradient(90deg, #a855f7, #c084fc);
  box-shadow: 0 0 8px rgba(168, 85, 247, 0.5);
}

/* --- SLIM CERTIFICATION RIBBON --- */
.cert-ribbon-v4 {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  padding: 1.25rem 2rem;
  background: rgba(0, 245, 155, 0.03);
  border: 1px solid rgba(0, 245, 155, 0.15);
  border-radius: 50px;
  margin: 0 auto;
  width: max-content;
  max-width: 100%;
  backdrop-filter: blur(5px);
}
.cr-title {
  font-family: var(--font-family-mono, monospace);
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  color: #00f59b;
  text-transform: uppercase;
}
.cr-divider {
  width: 1px;
  height: 20px;
  background: rgba(255, 255, 255, 0.2);
}
.cr-item {
  font-size: 0.9rem;
  color: #e2e8f0;
  font-weight: 500;
}
.cr-dot {
  color: #00d2c4;
  font-size: 0.8rem;
}

/* --- RESPONSIVE --- */
@media (max-width: 1024px) {
  .skills-hero-v4 {
    grid-template-columns: 1fr;
    gap: 4rem;
  }
  .sh-right {
    align-items: center;
  }
  .skills-cards-v4 {
    grid-template-columns: 1fr;
  }
  .cert-ribbon-v4 {
    flex-direction: column;
    border-radius: 16px;
    gap: 0.8rem;
    text-align: center;
  }
  .cr-divider, .cr-dot {
    display: none;
  }
}
"""
    
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content + new_css)
    print("CSS updated successfully.")

if __name__ == '__main__':
    update_html()
    update_css()
