/* ==========================================================================
   GENETIC ENGINEERING PORTFOLIO - CORE JS LIBRARY
   Features:
   - High-performance 3D Bioluminescent DNA Helix Canvas Animation
   - Dynamic Navigation Link Tracking & Header styling
   - Responsive Mobile Toggle Handler
   - Scroll-Driven Intersection Observer Fade-in Animation Engine
   - Interactive Form Handler & Transmission Confirmation
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  
  // ==========================================
  // 1. Fixed Header & Active Navigation Highlighting
  // ==========================================
  const header = document.querySelector('.main-header');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section');

  function updateHeaderState() {
    // Add border/background on scroll
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // Scroll Spy active navigation state
    let currentActiveId = '';
    const scrollPos = window.scrollY + 120; // offset for nav height

    sections.forEach(sec => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      const id = sec.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        currentActiveId = id;
      }
    });

    if (currentActiveId) {
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentActiveId}`) {
          link.classList.add('active');
        }
      });
    }
  }

  window.addEventListener('scroll', updateHeaderState);
  updateHeaderState();

  // ==========================================
  // 2. Mobile Responsive Menu Toggle
  // ==========================================
  const menuToggle = document.getElementById('menu-toggle-btn');
  const navMenu = document.querySelector('.nav-menu');

  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      menuToggle.setAttribute('aria-expanded', !isExpanded);
      menuToggle.classList.toggle('active');
      navMenu.classList.toggle('active');
    });

    // Close menu when clicking on nav link
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.classList.remove('active');
        navMenu.classList.remove('active');
      });
    });
  }

  // ==========================================
  // 3. Scroll Reveal Animation Engine (Intersection Observer)
  // ==========================================
  const animObserverOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
  };

  const animObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        
        // If skill progress bar is inside, animate its width
        const progressBars = entry.target.querySelectorAll('.progress-bar, .cat-skill-bar');
        progressBars.forEach(bar => {
          const targetWidth = bar.style.width;
          // Set width temporarily to 0, then back to trigger CSS transition
          bar.style.width = '0%';
          setTimeout(() => {
            bar.style.width = targetWidth;
          }, 50);
        });

        // Keep observing or unobserve to avoid repeat triggers
        observer.unobserve(entry.target);
      }
    });
  }, animObserverOptions);

  // Target all elements configured for scroll-animations
  const animElements = document.querySelectorAll('.animate-on-scroll, .timeline-item');
  animElements.forEach(el => animObserver.observe(el));


  // ==========================================
  // 4. 3D DNA Canvas Helix Animation Engine
  // ==========================================
  const canvas = document.getElementById('dnaCanvas');
  const ctx = canvas.getContext('2d');
  let animationFrameId;

  // Track coordinates for mouse interactions
  let mouse = { x: null, y: null, active: false };
  const parentContainer = document.querySelector('.hero-canvas-container');

  function resizeCanvas() {
    const rect = parentContainer.getBoundingClientRect();
    canvas.width = rect.width;
    canvas.height = rect.height;
  }
  
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  // Mouse hover event setup
  window.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
    
    // Check if mouse is inside the canvas bounding box
    if (e.clientX >= rect.left && e.clientX <= rect.right &&
        e.clientY >= rect.top && e.clientY <= rect.bottom) {
      mouse.active = true;
    } else {
      mouse.active = false;
    }
  });

  window.addEventListener('mouseleave', () => {
    mouse.active = false;
  });

  // DNA Configuration Parameters
  const dnaConfig = {
    dotsCount: 22,          // Number of base pairs
    radius: 75,             // Helix rotation radius
    spacing: 0.28,          // Angular phase shift per base pair
    speed: 0.007,           // Default speed of rotation
    currentTheta: 0,        // Running angle
    focalLength: 320,       // 3D Perspective compression
    waveFrequency: 0.12,    // Shape frequency
  };

  // Node class for coordinates and custom logic
  class BasePairNode {
    constructor(index) {
      this.index = index;
    }

    render(theta) {
      const spacingY = canvas.height / (dnaConfig.dotsCount + 1);
      const centerY = spacingY + (this.index * spacingY);
      const centerX = canvas.width * 0.5;

      // Phase Shift difference between node indices
      const angleOffset = this.index * dnaConfig.spacing;
      const angle1 = theta + angleOffset;
      const angle2 = theta + angleOffset + Math.PI; // 180 degrees shift (double helix)

      // Perspective scale variables
      const z1 = Math.cos(angle1) * dnaConfig.radius;
      const z2 = Math.cos(angle2) * dnaConfig.radius;

      const scale1 = dnaConfig.focalLength / (dnaConfig.focalLength + z1);
      const scale2 = dnaConfig.focalLength / (dnaConfig.focalLength + z2);

      // 3D projection to screen coordinates
      let x1 = centerX + Math.sin(angle1) * dnaConfig.radius * scale1;
      let x2 = centerX + Math.sin(angle2) * dnaConfig.radius * scale2;
      let y1 = centerY;
      let y2 = centerY;

      // Mouse influence logic: push nodes away slightly if mouse is close
      if (mouse.active) {
        const dist1 = Math.hypot(mouse.x - x1, mouse.y - y1);
        const dist2 = Math.hypot(mouse.x - x2, mouse.y - y2);

        if (dist1 < 80) {
          const force = (80 - dist1) * 0.15;
          const angle = Math.atan2(y1 - mouse.y, x1 - mouse.x);
          x1 += Math.cos(angle) * force;
        }
        if (dist2 < 80) {
          const force = (80 - dist2) * 0.15;
          const angle = Math.atan2(y2 - mouse.y, x2 - mouse.x);
          x2 += Math.cos(angle) * force;
        }
      }

      return {
        pt1: { x: x1, y: y1, z: z1, scale: scale1 },
        pt2: { x: x2, y: y2, z: z2, scale: scale2 }
      };
    }
  }

  // Populate node array
  const nodes = [];
  for (let i = 0; i < dnaConfig.dotsCount; i++) {
    nodes.push(new BasePairNode(i));
  }

  // Master Render Loop
  function animateDNA() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Dynamic speed variance: mouse movement adds friction/speed changes
    let localSpeed = dnaConfig.speed;
    if (mouse.active) {
      localSpeed = dnaConfig.speed * 1.6;
    }
    dnaConfig.currentTheta += localSpeed;

    const coordinates = nodes.map(node => node.render(dnaConfig.currentTheta));

    // 1. Draw Connecting base-pair bonds (Hydrogen bonds) first (renders behind nodes)
    coordinates.forEach((coord, idx) => {
      // Alternate bonds coloring: represent GC (3 hydrogen bonds) and AT (2 bonds)
      // Visualized using dotted/dashed styling
      const { pt1, pt2 } = coord;
      const isGC = idx % 2 === 0;

      // Calculate base pair color values based on mean Z depth
      const meanZ = (pt1.z + pt2.z) / 2;
      const alpha = 0.08 + (0.2 * (1 - (meanZ + dnaConfig.radius) / (2 * dnaConfig.radius)));

      ctx.beginPath();
      ctx.moveTo(pt1.x, pt1.y);
      ctx.lineTo(pt2.x, pt2.y);
      ctx.strokeStyle = isGC ? `rgba(0, 245, 155, ${alpha})` : `rgba(0, 210, 196, ${alpha})`;
      ctx.lineWidth = isGC ? 2 : 1;
      if (!isGC) ctx.setLineDash([3, 4]);
      else ctx.setLineDash([]);
      ctx.stroke();
    });
    ctx.setLineDash([]); // Reset dash state

    // 2. Draw Helix Nodes & Outer strands
    // Sort nodes to draw background elements first (3D Painters Algorithm)
    const pointsList = [];
    coordinates.forEach((coord, index) => {
      pointsList.push({
        x: coord.pt1.x, y: coord.pt1.y, z: coord.pt1.z, 
        scale: coord.pt1.scale, strand: 1, index
      });
      pointsList.push({
        x: coord.pt2.x, y: coord.pt2.y, z: coord.pt2.z, 
        scale: coord.pt2.scale, strand: 2, index
      });
    });

    pointsList.sort((a, b) => b.z - a.z); // Far away z first

    // Render sorted elements
    pointsList.forEach(pt => {
      const baseRadius = pt.strand === 1 ? 5.5 : 4.5;
      const dotRadius = baseRadius * pt.scale;
      
      // Calculate individual opacity from Z depth
      const zPercent = (pt.z + dnaConfig.radius) / (2 * dnaConfig.radius); // 0 (closest) to 1 (furthest)
      const alpha = 0.35 + (0.65 * (1 - zPercent));

      ctx.beginPath();
      ctx.arc(pt.x, pt.y, dotRadius, 0, Math.PI * 2);
      
      if (pt.strand === 1) {
        // Emerald Green Node
        ctx.fillStyle = `rgba(0, 245, 155, ${alpha})`;
        ctx.shadowBlur = 10 * pt.scale;
        ctx.shadowColor = 'rgba(0, 245, 155, 0.6)';
      } else {
        // Cyber Teal Node
        ctx.fillStyle = `rgba(0, 210, 196, ${alpha})`;
        ctx.shadowBlur = 8 * pt.scale;
        ctx.shadowColor = 'rgba(0, 210, 196, 0.5)';
      }

      ctx.fill();
      ctx.shadowBlur = 0; // Reset shadow glow
    });

    animationFrameId = requestAnimationFrame(animateDNA);
  }

  // Start Animation
  animateDNA();

  // ==========================================
  // 5. Interactive Form Handler & Transmission
  // ==========================================
  const contactForm = document.getElementById('portfolio-contact-form');
  const successAlert = document.getElementById('form-success-alert');

  if (contactForm && successAlert) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const btnSubmit = contactForm.querySelector('.btn-submit');
      const originalBtnHTML = btnSubmit.innerHTML;

      // Enter glowing loading state
      btnSubmit.disabled = true;
      btnSubmit.style.opacity = '0.7';
      btnSubmit.innerHTML = `
        <span>Compiling sequence...</span>
        <svg class="btn-icon" style="animation: logo-rotate 1.5s linear infinite" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10" stroke-dasharray="8 8"/>
        </svg>
      `;

      // Mock sending packet over cybernetic link (simulate 1.5s delay)
      setTimeout(() => {
        // Restore button state
        btnSubmit.disabled = false;
        btnSubmit.style.opacity = '1';
        btnSubmit.innerHTML = originalBtnHTML;

        // Reset inputs
        contactForm.reset();

        // Reveal beautiful bioluminescent confirmation prompt
        successAlert.style.display = 'flex';

        // Auto-hide alert after 8 seconds
        setTimeout(() => {
          successAlert.style.animation = 'fade-in-up 0.4s reverse forwards';
          setTimeout(() => {
            successAlert.style.display = 'none';
            successAlert.style.animation = 'fade-in-up 0.4s cubic-bezier(0.1, 0.8, 0.2, 1) forwards';
          }, 400);
        }, 8000);

      }, 1500);
    });
  }

});

// Global functions for NPTEL Certificate Modal Window
window.openCertModal = function(title, fullTitle, org, desc) {
  const modal = document.getElementById('certModal');
  const titleEl = document.getElementById('modalCertTitle');
  const orgEl = document.getElementById('modalCertOrg');
  const specEl = document.getElementById('modalCertSpec');
  const descEl = document.getElementById('modalCertDesc');

  if (modal) {
    if (titleEl) titleEl.textContent = title;
    if (orgEl) orgEl.textContent = `Issued by ${org}`;
    if (specEl) specEl.textContent = `For successfully completing: ${fullTitle}`;
    if (descEl) descEl.textContent = desc;

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
};

window.closeCertModal = function() {
  const modal = document.getElementById('certModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
};

// Close modal when clicking backdrop
document.addEventListener('click', (e) => {
  const modal = document.getElementById('certModal');
  if (modal && e.target === modal) {
    closeCertModal();
  }
});

// Close modal on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeCertModal();
  }
});

