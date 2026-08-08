import re

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "r", encoding="utf-8") as f:
    content = f.read()

new_html = """
        <div class="hero-canvas-container">
          <style>
            /* Holographic Scene Container */
            .holo-lab-scene {
              position: absolute;
              top: 0; left: 0; right: 0; bottom: 0;
              width: 100%;
              height: 100%;
              /* Seamlessly fade edges into background */
              -webkit-mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 70%);
              mask-image: radial-gradient(ellipse at center, rgba(0,0,0,1) 30%, rgba(0,0,0,0) 70%);
              pointer-events: none; /* Let clicks pass through if necessary */
              z-index: 0;
              overflow: hidden;
            }

            /* Base Laboratory Image */
            .holo-bg-layer {
              position: absolute;
              top: -10%; left: -10%;
              width: 120%; height: 120%;
              background-image: url('./image/lab_scene_base.png');
              background-size: cover;
              background-position: center;
              opacity: 0.6;
              filter: contrast(1.2) brightness(0.8) hue-rotate(15deg);
              animation: slowPan 40s linear infinite alternate;
              z-index: 1;
            }

            @keyframes slowPan {
              0% { transform: scale(1) translate(0, 0); }
              100% { transform: scale(1.1) translate(-2%, 2%); }
            }

            /* Floating Glass Panels */
            .holo-glass-panel {
              position: absolute;
              background: rgba(10, 20, 25, 0.5);
              backdrop-filter: blur(12px);
              -webkit-backdrop-filter: blur(12px);
              border: 1px solid rgba(0, 245, 155, 0.2);
              border-top: 1px solid rgba(0, 245, 155, 0.4);
              border-radius: 8px;
              padding: 15px;
              color: rgba(255,255,255,0.9);
              font-family: 'Space Mono', monospace, sans-serif;
              z-index: 3;
              box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 0 15px rgba(0,245,155,0.05);
              animation: floatPanel 6s ease-in-out infinite alternate;
            }

            .panel-bioinformatics {
              top: 15%;
              right: 15%;
              width: 200px;
              animation-delay: 0s;
            }

            .panel-crispr {
              bottom: 25%;
              left: 20%;
              width: 180px;
              animation-delay: -3s;
            }

            @keyframes floatPanel {
              0% { transform: translateY(0px) rotateX(0deg) rotateY(0deg); }
              100% { transform: translateY(-15px) rotateX(2deg) rotateY(-5deg); }
            }

            .panel-header {
              font-size: 0.65rem;
              letter-spacing: 2px;
              color: #00f59b;
              margin-bottom: 10px;
              border-bottom: 1px solid rgba(0,245,155,0.2);
              padding-bottom: 4px;
              text-transform: uppercase;
            }

            .panel-data-row {
              display: flex;
              justify-content: space-between;
              font-size: 0.75rem;
              margin-bottom: 8px;
            }

            .pulse-text {
              animation: textPulse 2s infinite alternate;
            }
            @keyframes textPulse {
              0% { opacity: 0.5; text-shadow: 0 0 5px rgba(0,245,155,0); }
              100% { opacity: 1; text-shadow: 0 0 8px rgba(0,245,155,0.8); }
            }

            .data-bar-chart {
              display: flex;
              align-items: flex-end;
              gap: 4px;
              height: 40px;
              margin-top: 10px;
            }

            .data-bar-chart .bar {
              flex: 1;
              background: linear-gradient(to top, rgba(0,210,196,0.2), rgba(0,245,155,0.8));
              border-radius: 2px 2px 0 0;
              animation: barAnim 3s infinite alternate ease-in-out;
            }

            .data-bar-chart .bar:nth-child(2) { animation-delay: -0.5s; }
            .data-bar-chart .bar:nth-child(3) { animation-delay: -1.2s; }
            .data-bar-chart .bar:nth-child(4) { animation-delay: -0.8s; }
            .data-bar-chart .bar:nth-child(5) { animation-delay: -1.5s; }

            @keyframes barAnim {
              0% { transform: scaleY(0.6); }
              100% { transform: scaleY(1.1); }
            }

            /* CRISPR Target Reticle */
            .target-reticle {
              position: relative;
              width: 60px;
              height: 60px;
              margin: 15px auto;
            }

            .reticle-ring {
              position: absolute;
              inset: 0;
              border-radius: 50%;
              border: 1px solid dashed rgba(0,245,155,0.5);
              border-top: 2px solid #00f59b;
              border-bottom: 2px solid #00d2c4;
            }

            .spin-slow { animation: spin 8s linear infinite; }
            .spin-fast-reverse { animation: spin 4s linear infinite reverse; inset: 10px; border-width: 1px; }

            .reticle-center {
              position: absolute;
              inset: 25px;
              background: #00f59b;
              border-radius: 50%;
              box-shadow: 0 0 10px #00f59b;
              animation: pulseRing 2s infinite alternate;
            }

            @keyframes spin { 100% { transform: rotate(360deg); } }
            @keyframes pulseRing { 0% { transform: scale(0.8); opacity: 0.5; } 100% { transform: scale(1.2); opacity: 1; } }

            /* Molecular Network */
            .holo-network-svg {
              position: absolute;
              top: 0; left: 0;
              width: 100%; height: 100%;
              z-index: 2;
            }

            .pulse-node {
              animation: nodePulse 3s infinite alternate;
            }
            .pulse-node:nth-child(even) { animation-delay: -1.5s; }

            @keyframes nodePulse {
              0% { r: 1.5; opacity: 0.4; filter: drop-shadow(0 0 2px #00f59b); }
              100% { r: 3.5; opacity: 1; filter: drop-shadow(0 0 8px #00f59b); }
            }

            .holo-line {
              animation: lineFade 4s infinite alternate;
            }
            @keyframes lineFade { 0% { opacity: 0.1; } 100% { opacity: 0.6; } }

            /* Particles */
            .holo-particles {
              position: absolute;
              inset: 0;
              z-index: 2;
            }

            .holo-particle {
              position: absolute;
              width: 4px; height: 4px;
              background: #00f59b;
              border-radius: 50%;
              box-shadow: 0 0 10px 2px rgba(0,245,155,0.6);
              animation: floatParticle 8s infinite ease-in-out;
            }

            @keyframes floatParticle {
              0% { transform: translate(0, 0) scale(1); opacity: 0.1; }
              50% { opacity: 0.8; }
              100% { transform: translate(30px, -40px) scale(1.5); opacity: 0; }
            }

            /* Micro DNA */
            .holo-micro-dna-container {
              position: absolute;
              top: 40%; left: 45%;
              width: 80px; height: 160px;
              z-index: 4;
              transform-style: preserve-3d;
              animation: floatMicro 7s infinite ease-in-out alternate;
            }

            @keyframes floatMicro {
              0% { transform: translateY(0) rotate(-10deg); }
              100% { transform: translateY(-20px) rotate(5deg); }
            }

            .micro-dna-svg {
              width: 100%; height: 100%;
              filter: drop-shadow(0 0 6px rgba(0,245,155,0.6));
            }
            
            .dna-strand {
              animation: dnaUndulate 4s infinite alternate ease-in-out;
            }
            .dna-strand-2 { animation-delay: -2s; }
            .dna-rung { animation: pulseRung 2s infinite alternate; }

            @keyframes dnaUndulate {
              0% { d: path("M 30,10 C 70,30 30,70 70,90 C 30,110 70,150 30,170"); }
              100% { d: path("M 20,10 C 80,30 20,70 80,90 C 20,110 80,150 20,170"); }
            }
            @keyframes pulseRung {
              0% { stroke-width: 1px; opacity: 0.4; }
              100% { stroke-width: 2.5px; opacity: 0.9; }
            }

            /* Protein Hologram */
            .holo-protein-structure {
              position: absolute;
              top: 60%; right: 25%;
              width: 120px; height: 120px;
              z-index: 3;
              animation: spinSlow 20s linear infinite;
            }
            @keyframes spinSlow { 100% { transform: rotate(360deg); } }
            
            .protein-path-1, .protein-path-2 {
              stroke-dasharray: 200;
              stroke-dashoffset: 200;
              animation: drawProtein 6s infinite alternate ease-in-out;
            }
            .protein-path-2 { animation-delay: -3s; }
            
            @keyframes drawProtein {
              0% { stroke-dashoffset: 200; opacity: 0.2; }
              100% { stroke-dashoffset: 0; opacity: 1; filter: drop-shadow(0 0 5px rgba(0,210,196,0.8)); }
            }
          </style>

          <div class="holo-lab-scene">
            <div class="holo-bg-layer"></div>
            
            <!-- Bioinformatics Dashboard -->
            <div class="holo-glass-panel panel-bioinformatics">
              <div class="panel-header">GENOME SEQUENCE</div>
              <div class="panel-data-row">
                <div class="data-label">DATA:</div>
                <div class="data-value pulse-text">ATCG-GCTA</div>
              </div>
              <div class="data-bar-chart">
                <div class="bar" style="height: 60%"></div>
                <div class="bar" style="height: 80%"></div>
                <div class="bar" style="height: 40%"></div>
                <div class="bar" style="height: 90%"></div>
                <div class="bar" style="height: 50%"></div>
              </div>
            </div>

            <!-- CRISPR Interface -->
            <div class="holo-glass-panel panel-crispr">
              <div class="panel-header">CRISPR TARGETING</div>
              <div class="target-reticle">
                <div class="reticle-ring spin-slow"></div>
                <div class="reticle-ring spin-fast-reverse"></div>
                <div class="reticle-center"></div>
              </div>
              <div style="font-size: 0.65rem; text-align: center; color: #00d2c4;">LOCUS: 8p23.1</div>
            </div>

            <!-- Protein Hologram -->
            <div class="holo-protein-structure">
              <svg viewBox="0 0 100 100">
                <path d="M 20,50 Q 30,10 50,50 T 80,50" fill="none" stroke="rgba(0, 245, 155, 0.7)" stroke-width="2" class="protein-path-1" />
                <path d="M 20,70 Q 40,90 60,70 T 90,40" fill="none" stroke="rgba(0, 210, 196, 0.8)" stroke-width="1.5" class="protein-path-2" />
                <path d="M 40,30 Q 70,10 80,70 T 20,80" fill="none" stroke="rgba(0, 245, 155, 0.4)" stroke-width="1" class="protein-path-1" style="animation-delay: -2s;" />
              </svg>
            </div>

            <!-- Molecular Network -->
            <svg class="holo-network-svg" viewBox="0 0 100 100" preserveAspectRatio="none">
              <circle cx="20%" cy="30%" r="1" fill="#00f59b" class="pulse-node" />
              <circle cx="45%" cy="25%" r="0.8" fill="#00f59b" class="pulse-node" />
              <circle cx="70%" cy="35%" r="1.5" fill="#00f59b" class="pulse-node" />
              <circle cx="85%" cy="20%" r="0.5" fill="#00f59b" class="pulse-node" />
              <circle cx="35%" cy="70%" r="1" fill="#00f59b" class="pulse-node" />
              <circle cx="60%" cy="80%" r="1.2" fill="#00f59b" class="pulse-node" />
              <circle cx="80%" cy="65%" r="0.8" fill="#00f59b" class="pulse-node" />
              
              <line x1="20%" y1="30%" x2="45%" y2="25%" stroke="rgba(0, 245, 155, 0.3)" stroke-width="0.3" class="holo-line"/>
              <line x1="45%" y1="25%" x2="70%" y2="35%" stroke="rgba(0, 245, 155, 0.3)" stroke-width="0.3" class="holo-line"/>
              <line x1="70%" y1="35%" x2="85%" y2="20%" stroke="rgba(0, 245, 155, 0.3)" stroke-width="0.3" class="holo-line"/>
              <line x1="20%" y1="30%" x2="35%" y2="70%" stroke="rgba(0, 245, 155, 0.3)" stroke-width="0.3" class="holo-line"/>
              <line x1="35%" y1="70%" x2="60%" y2="80%" stroke="rgba(0, 245, 155, 0.3)" stroke-width="0.3" class="holo-line"/>
              <line x1="60%" y1="80%" x2="80%" y2="65%" stroke="rgba(0, 245, 155, 0.3)" stroke-width="0.3" class="holo-line"/>
              <line x1="70%" y1="35%" x2="80%" y2="65%" stroke="rgba(0, 245, 155, 0.3)" stroke-width="0.3" class="holo-line"/>
            </svg>

            <!-- Micro DNA Hologram -->
            <div class="holo-micro-dna-container">
              <svg class="micro-dna-svg" viewBox="0 0 100 200">
                <path d="M 30,20 Q 50,40 30,60 T 30,100 T 30,140 T 30,180" fill="none" stroke="rgba(0,255,180,0.8)" stroke-width="2" class="dna-strand dna-strand-1"/>
                <path d="M 70,20 Q 50,40 70,60 T 70,100 T 70,140 T 70,180" fill="none" stroke="rgba(0,180,255,0.6)" stroke-width="2" class="dna-strand dna-strand-2"/>
                <line x1="35" y1="30" x2="65" y2="30" stroke="rgba(0,255,180,0.5)" stroke-width="1.5" class="dna-rung"/>
                <line x1="45" y1="40" x2="55" y2="40" stroke="rgba(0,255,180,0.5)" stroke-width="1.5" class="dna-rung"/>
                <line x1="35" y1="70" x2="65" y2="70" stroke="rgba(0,255,180,0.5)" stroke-width="1.5" class="dna-rung"/>
                <line x1="45" y1="80" x2="55" y2="80" stroke="rgba(0,255,180,0.5)" stroke-width="1.5" class="dna-rung"/>
                <line x1="35" y1="110" x2="65" y2="110" stroke="rgba(0,255,180,0.5)" stroke-width="1.5" class="dna-rung"/>
                <line x1="45" y1="120" x2="55" y2="120" stroke="rgba(0,255,180,0.5)" stroke-width="1.5" class="dna-rung"/>
                <line x1="35" y1="150" x2="65" y2="150" stroke="rgba(0,255,180,0.5)" stroke-width="1.5" class="dna-rung"/>
                <line x1="45" y1="160" x2="55" y2="160" stroke="rgba(0,255,180,0.5)" stroke-width="1.5" class="dna-rung"/>
              </svg>
            </div>

            <!-- Particles -->
            <div class="holo-particles">
              <div class="holo-particle" style="left: 15%; top: 25%; animation-delay: 0s;"></div>
              <div class="holo-particle" style="left: 85%; top: 45%; animation-delay: 1.2s; background: #00d2c4;"></div>
              <div class="holo-particle" style="left: 45%; top: 75%; animation-delay: 2.5s;"></div>
              <div class="holo-particle" style="left: 35%; top: 85%; animation-delay: 3.1s; background: #00d2c4;"></div>
              <div class="holo-particle" style="left: 75%; top: 15%; animation-delay: 0.8s;"></div>
              <div class="holo-particle" style="left: 55%; top: 35%; animation-delay: 4.8s;"></div>
              <div class="holo-particle" style="left: 25%; top: 65%; animation-delay: 5.2s; background: #00d2c4;"></div>
            </div>

          </div>
        </div>
"""

content = re.sub(r'<div class="hero-canvas-container">\s*<canvas id="dnaCanvas"></canvas>\s*</div>', new_html, content)

with open("d:\\shunanda( natto don't delete)\\shunanda portfolio\\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced hero container!")
