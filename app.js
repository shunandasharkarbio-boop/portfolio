/* ==========================================================================
   SHUNANDA PORTFOLIO - INTERACTIVE APPLICATION LOGIC
   Features:
   - Bioluminescent DNA Helix 3D Canvas Animation
   - Mobile Navigation Toggle
   - Smooth Scroll Offset for Anchor Links
   - Scroll Triggered Animations (Intersection Observer)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const menuToggleBtn = document.getElementById('menu-toggle-btn');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (menuToggleBtn && navMenu) {
    menuToggleBtn.addEventListener('click', () => {
      const isExpanded = menuToggleBtn.getAttribute('aria-expanded') === 'true';
      menuToggleBtn.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('active');
      menuToggleBtn.classList.toggle('active');
    });

    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        menuToggleBtn.classList.remove('active');
        menuToggleBtn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // 2. Scroll Animation Observer
  const animateElements = document.querySelectorAll('.animate-on-scroll');
  
  if ('IntersectionObserver' in window) {
    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -50px 0px',
      threshold: 0.15
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    animateElements.forEach(el => scrollObserver.observe(el));
  } else {
    // Fallback for older browsers
    animateElements.forEach(el => el.classList.add('is-visible'));
  }

  // 3. Bioluminescent DNA Canvas Particle & Helix Animation
  const canvas = document.getElementById('dnaCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let animationFrameId;

    function resizeCanvas() {
      canvas.width = canvas.parentElement.clientWidth || window.innerWidth;
      canvas.height = canvas.parentElement.clientHeight || window.innerHeight;
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Particle system for ambient bio-sparks
    const particleCount = 40;
    const particles = [];

    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 2 + 0.5,
        color: Math.random() > 0.4 ? '#00f59b' : '#00d2c4',
        alpha: Math.random() * 0.5 + 0.2,
        speedX: (Math.random() - 0.5) * 0.4,
        speedY: (Math.random() - 0.5) * 0.4,
        pulseSpeed: Math.random() * 0.02 + 0.01
      });
    }

    let time = 0;

    function animate() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      time += 0.015;

      // Draw floating bioluminescent particles
      particles.forEach(p => {
        p.x += p.speedX;
        p.y += p.speedY;
        p.alpha += Math.sin(time * 2) * 0.005;

        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;

        ctx.save();
        ctx.globalAlpha = Math.max(0.1, Math.min(0.8, p.alpha));
        ctx.fillStyle = p.color;
        ctx.shadowColor = p.color;
        ctx.shadowBlur = 10;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      });

      // Draw 3D Rotating DNA Strand across background right side
      const centerX = canvas.width * 0.75;
      const startY = canvas.height * 0.1;
      const endY = canvas.height * 0.9;
      const numNodes = 28;
      const nodeSpacing = (endY - startY) / numNodes;
      const amplitude = Math.min(100, canvas.width * 0.12);

      for (let i = 0; i < numNodes; i++) {
        const y = startY + i * nodeSpacing;
        const phase = time * 1.5 + (i * 0.25);
        const x1 = centerX + Math.sin(phase) * amplitude;
        const x2 = centerX - Math.sin(phase) * amplitude;
        const z1 = Math.cos(phase);
        const z2 = -Math.cos(phase);

        // Calculate size based on depth (z-index simulation)
        const r1 = Math.max(1.5, 3.5 + z1 * 1.5);
        const r2 = Math.max(1.5, 3.5 + z2 * 1.5);

        const alpha1 = Math.max(0.2, 0.5 + z1 * 0.3);
        const alpha2 = Math.max(0.2, 0.5 + z2 * 0.3);

        // Draw horizontal base pair rung connecting the two strands
        ctx.save();
        ctx.globalAlpha = Math.min(alpha1, alpha2) * 0.35;
        ctx.strokeStyle = '#00d2c4';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(x1, y);
        ctx.lineTo(x2, y);
        ctx.stroke();
        ctx.restore();

        // Draw Strand 1 Node
        ctx.save();
        ctx.globalAlpha = alpha1;
        ctx.fillStyle = '#00f59b';
        ctx.shadowColor = '#00f59b';
        ctx.shadowBlur = 8;
        ctx.beginPath();
        ctx.arc(x1, y, r1, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();

        // Draw Strand 2 Node
        ctx.save();
        ctx.globalAlpha = alpha2;
        ctx.fillStyle = '#00d2c4';
        ctx.shadowColor = '#00d2c4';
        ctx.shadowBlur = 8;
        ctx.beginPath();
        ctx.arc(x2, y, r2, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }

      animationFrameId = requestAnimationFrame(animate);
    }

    animate();
  }

  // 4. Certificate Lightbox Modal Logic
  const certModal = document.getElementById('certModal');
  const certModalClose = document.getElementById('certModalClose');
  const modalCertTitle = document.getElementById('modalCertTitle');
  const modalCertIssuer = document.getElementById('modalCertIssuer');
  const modalCertDesc = document.getElementById('modalCertDesc');
  const viewCertBtns = document.querySelectorAll('.btn-view-cert');

  if (certModal && viewCertBtns.length > 0) {
    viewCertBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const title = btn.getAttribute('data-title') || 'Certificate';
        const issuer = btn.getAttribute('data-issuer') || 'Issuer';
        const desc = btn.getAttribute('data-desc') || '';

        if (modalCertTitle) modalCertTitle.textContent = title;
        if (modalCertIssuer) modalCertIssuer.textContent = issuer;
        if (modalCertDesc) modalCertDesc.textContent = desc;

        certModal.classList.add('active');
        certModal.setAttribute('aria-hidden', 'false');
      });
    });

    const closeModal = () => {
      certModal.classList.remove('active');
      certModal.setAttribute('aria-hidden', 'true');
    };

    if (certModalClose) {
      certModalClose.addEventListener('click', closeModal);
    }

    certModal.addEventListener('click', (e) => {
      if (e.target === certModal) {
        closeModal();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && certModal.classList.contains('active')) {
        closeModal();
      }
    });
  }
});
