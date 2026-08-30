/* ==========================================================================
   SHUNANDA PORTFOLIO - INTERACTIVE APPLICATION LOGIC
   Features:
   - Bioluminescent DNA Helix 3D Canvas Animation
   - Mobile Navigation Toggle
   - Smooth Scroll Offset for Anchor Links
   - Scroll Triggered Animations (Intersection Observer)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // 0. Dark & Light (White) Mode Theme Controller
  function initThemeToggle() {
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const mobileThemeToggleBtn = document.getElementById('mobile-theme-toggle-btn');

    function getPreferredTheme() {
      const savedTheme = localStorage.getItem('shunanda_portfolio_theme');
      if (savedTheme === 'light' || savedTheme === 'dark') {
        return savedTheme;
      }
      return 'dark'; // Default bioluminescent futuristic
    }

    function applyTheme(theme) {
      document.documentElement.classList.add('theme-transition');
      document.documentElement.setAttribute('data-theme', theme);
      try {
        localStorage.setItem('shunanda_portfolio_theme', theme);
      } catch (e) {}

      setTimeout(() => {
        document.documentElement.classList.remove('theme-transition');
      }, 350);

      const isLight = theme === 'light';
      const label = isLight ? 'Switch to Dark Mode' : 'Switch to Light Mode';
      if (themeToggleBtn) {
        themeToggleBtn.setAttribute('aria-label', label);
        themeToggleBtn.setAttribute('title', label);
      }
      if (mobileThemeToggleBtn) {
        mobileThemeToggleBtn.setAttribute('aria-label', label);
        mobileThemeToggleBtn.setAttribute('title', label);
        const textEl = mobileThemeToggleBtn.querySelector('.theme-switch-label');
        if (textEl) {
          textEl.textContent = isLight ? 'Dark Mode' : 'Light Mode';
        }
      }
    }

    function toggleTheme() {
      const currentTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
      const nextTheme = currentTheme === 'light' ? 'dark' : 'light';
      applyTheme(nextTheme);
    }

    const currentTheme = getPreferredTheme();
    applyTheme(currentTheme);

    if (themeToggleBtn) {
      themeToggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
        toggleTheme();
      });
    }

    if (mobileThemeToggleBtn) {
      mobileThemeToggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
        toggleTheme();
      });
    }

    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('shunanda_portfolio_theme')) {
          applyTheme(e.matches ? 'dark' : 'light');
        }
      });
    }
  }

  initThemeToggle();

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
      document.body.classList.toggle('nav-active', navMenu.classList.contains('active'));
    });

    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        menuToggleBtn.classList.remove('active');
        menuToggleBtn.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('nav-active');
      });
    });
  }

  // 2. Scroll Animation Observer
  const animateElements = document.querySelectorAll('.animate-on-scroll, .timeline-item, .project-card, .achievement-card');

  function revealVisibleElements() {
    const windowHeight = window.innerHeight || document.documentElement.clientHeight;
    animateElements.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top <= windowHeight + 200 && rect.bottom >= -200) {
        el.classList.add('is-visible');
        el.classList.add('visible');
      }
    });
  }

  function checkHashTarget() {
    if (window.location.hash) {
      try {
        const targetSec = document.querySelector(window.location.hash);
        if (targetSec) {
          const innerAnimates = targetSec.querySelectorAll('.animate-on-scroll, .timeline-item, .project-card, .achievement-card');
          innerAnimates.forEach(el => {
            el.classList.add('is-visible');
            el.classList.add('visible');
          });
        }
      } catch (err) {}
    }
  }

  window.addEventListener('hashchange', checkHashTarget);
  setTimeout(checkHashTarget, 200);

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.05,
      rootMargin: '100px 0px 100px 0px'
    });

    animateElements.forEach(el => {
      observer.observe(el);
    });

    window.addEventListener('scroll', revealVisibleElements, { passive: true });
    window.addEventListener('load', revealVisibleElements);
  } else {
    animateElements.forEach(el => {
      el.classList.add('is-visible');
      el.classList.add('visible');
    });
  }

  document.querySelectorAll('.skd-cat-card, .skd-tab, .filter-chip, .coursework-card, .project-card, .achievement-card').forEach(item => {
    item.style.pointerEvents = 'auto';
  });

  // 3. Bioluminescent DNA Canvas Particle & Helix Animation
  const canvas = document.getElementById('dnaCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let animationFrameId;

    function resizeCanvas() {
      if (canvas) {
        const parent = canvas.parentElement;
        canvas.width = (parent && parent.clientWidth) ? parent.clientWidth : (window.innerWidth || 1200);
        canvas.height = (parent && parent.clientHeight) ? parent.clientHeight : (window.innerHeight || 800);
      }
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const particleCount = 40;
    const particles = [];

    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * (canvas.width || 800),
        y: Math.random() * (canvas.height || 600),
        radius: Math.random() * 2 + 0.5,
        type: Math.random() > 0.4 ? 'primary' : 'secondary',
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

      const isLight = document.documentElement.getAttribute('data-theme') === 'light';
      const colorPrimary = isLight ? '#059669' : '#00f59b';
      const colorSecondary = isLight ? '#0d9488' : '#00d2c4';
      const glowBlur = isLight ? 4 : 10;

      // Draw floating bioluminescent particles
      particles.forEach(p => {
        p.x += p.speedX;
        p.y += p.speedY;
        p.alpha += Math.sin(time * 2) * 0.005;

        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;

        const pColor = p.type === 'primary' ? colorPrimary : colorSecondary;

        ctx.save();
        ctx.globalAlpha = Math.max(0.1, Math.min(0.8, p.alpha));
        ctx.fillStyle = pColor;
        ctx.shadowColor = pColor;
        ctx.shadowBlur = glowBlur;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      });

      // Draw 3D Rotating DNA Strand across background right side
      const centerX = canvas.width * 0.5;
      const startY = canvas.height * 0.1;
      const endY = canvas.height * 0.9;
      const numNodes = 28;
      const nodeSpacing = (endY - startY) / numNodes;
      const amplitude = Math.min(120, canvas.width * 0.22);

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
        ctx.globalAlpha = Math.min(alpha1, alpha2) * (isLight ? 0.45 : 0.35);
        ctx.strokeStyle = colorSecondary;
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(x1, y);
        ctx.lineTo(x2, y);
        ctx.stroke();
        ctx.restore();

        // Draw Strand 1 Node
        ctx.save();
        ctx.globalAlpha = alpha1;
        ctx.fillStyle = colorPrimary;
        ctx.shadowColor = colorPrimary;
        ctx.shadowBlur = glowBlur;
        ctx.beginPath();
        ctx.arc(x1, y, r1, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();

        // Draw Strand 2 Node
        ctx.save();
        ctx.globalAlpha = alpha2;
        ctx.fillStyle = colorSecondary;
        ctx.shadowColor = colorSecondary;
        ctx.shadowBlur = glowBlur;
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
  const modalCertImage = document.getElementById('modalCertImage');
  const viewCertBtns = document.querySelectorAll('.btn-view-cert');

  if (certModal && viewCertBtns.length > 0) {
    viewCertBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const title = btn.getAttribute('data-title') || 'Certificate';
        const issuer = btn.getAttribute('data-issuer') || 'Issuer';
        const desc = btn.getAttribute('data-desc') || '';
        const img = btn.getAttribute('data-img') || '';

        if (modalCertTitle) modalCertTitle.textContent = title;
        if (modalCertIssuer) modalCertIssuer.textContent = issuer;
        if (modalCertDesc) modalCertDesc.textContent = desc;
        if (modalCertImage) {
          if (img) {
            modalCertImage.src = img;
            modalCertImage.style.display = 'block';
          } else {
            modalCertImage.style.display = 'none';
          }
        }

        certModal.classList.add('active');
        certModal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('cert-modal-open');
      });
    });

    const closeModal = () => {
      certModal.classList.remove('active');
      certModal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('cert-modal-open');
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

  // 5. Achievement Lightbox Modal & Multi-Image Gallery Logic
  const achievementCards = document.querySelectorAll('.achievement-card');
  const achievementLightbox = document.getElementById('achievementLightbox');
  const lightboxOverlay = document.getElementById('lightboxOverlay');
  const lightboxCloseBtn = document.getElementById('lightboxCloseBtn');
  const lightboxPrevBtn = document.getElementById('lightboxPrevBtn');
  const lightboxNextBtn = document.getElementById('lightboxNextBtn');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxPlaceholder = document.getElementById('lightboxPlaceholder');
  const lightboxTitle = document.getElementById('lightboxTitle');
  const lightboxBadge = document.getElementById('lightboxBadge');
  const lightboxDesc = document.getElementById('lightboxDesc');
  const lightboxCounter = document.getElementById('lightboxCounter');
  const lightboxMain = document.getElementById('lightboxMain');

  if (achievementLightbox && achievementCards.length > 0) {
    let currentGallery = [];
    let currentIndex = 0;
    let currentCardData = {};

    function openAchievementLightbox(card) {
      const rawGallery = card.getAttribute('data-gallery');
      let gallery = [];
      try {
        if (rawGallery) gallery = JSON.parse(rawGallery);
      } catch (err) {
        gallery = [];
      }

      const imgEl = card.querySelector('.achievement-img');
      const imgSrc = imgEl ? imgEl.getAttribute('src') : '';

      if (!Array.isArray(gallery) || gallery.length === 0) {
        gallery = [imgSrc || ''];
      }

      currentGallery = gallery;
      currentIndex = 0;
      currentCardData = {
        title: card.getAttribute('data-title') || '',
        badge: card.getAttribute('data-badge') || card.getAttribute('data-date') || '',
        desc: card.getAttribute('data-desc') || ''
      };

      updateLightboxContent();
      achievementLightbox.classList.add('active');
      achievementLightbox.setAttribute('aria-hidden', 'false');
      document.body.classList.add('lightbox-open');
      document.body.style.overflow = 'hidden';
    }

    function closeAchievementLightbox() {
      achievementLightbox.classList.remove('active');
      achievementLightbox.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('lightbox-open');
      document.body.style.overflow = '';
    }

    function updateLightboxContent() {
      if (currentGallery.length === 0) return;

      const activeSrc = currentGallery[currentIndex];

      if (lightboxTitle) lightboxTitle.textContent = currentCardData.title;
      if (lightboxBadge) lightboxBadge.textContent = currentCardData.badge;
      if (lightboxDesc) lightboxDesc.textContent = currentCardData.desc;

      if (lightboxCounter) {
        lightboxCounter.textContent = `${currentIndex + 1} / ${currentGallery.length}`;
      }

      if (activeSrc && activeSrc.trim() !== '') {
        if (lightboxImg) {
          lightboxImg.src = activeSrc;
          lightboxImg.style.display = 'block';
          lightboxImg.onerror = function() {
            this.style.display = 'none';
            if (lightboxPlaceholder) lightboxPlaceholder.style.display = 'flex';
          };
          lightboxImg.onload = function() {
            this.style.display = 'block';
            if (lightboxPlaceholder) lightboxPlaceholder.style.display = 'none';
          };
        }
      } else {
        if (lightboxImg) {
          lightboxImg.src = '';
          lightboxImg.style.display = 'none';
        }
        if (lightboxPlaceholder) lightboxPlaceholder.style.display = 'flex';
      }

      if (currentGallery.length > 1) {
        if (lightboxPrevBtn) lightboxPrevBtn.style.display = 'flex';
        if (lightboxNextBtn) lightboxNextBtn.style.display = 'flex';
      } else {
        if (lightboxPrevBtn) lightboxPrevBtn.style.display = 'none';
        if (lightboxNextBtn) lightboxNextBtn.style.display = 'none';
      }
    }

    function showNextImage() {
      if (currentGallery.length <= 1) return;
      currentIndex = (currentIndex + 1) % currentGallery.length;
      updateLightboxContent();
    }

    function showPrevImage() {
      if (currentGallery.length <= 1) return;
      currentIndex = (currentIndex - 1 + currentGallery.length) % currentGallery.length;
      updateLightboxContent();
    }

    // Use event delegation so cloned carousel cards also trigger the lightbox
    document.addEventListener('click', (e) => {
      const imgContainer = e.target.closest('.achievement-img-container');
      if (!imgContainer) return;
      const card = imgContainer.closest('.achievement-card');
      if (!card) return;
      openAchievementLightbox(card);
    });
    document.addEventListener('keydown', (e) => {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      const imgContainer = document.activeElement && document.activeElement.closest
        ? document.activeElement.closest('.achievement-img-container')
        : null;
      if (!imgContainer) return;
      const card = imgContainer.closest('.achievement-card');
      if (!card) return;
      e.preventDefault();
      openAchievementLightbox(card);
    });

    if (lightboxCloseBtn) lightboxCloseBtn.addEventListener('click', closeAchievementLightbox);
    if (lightboxOverlay) lightboxOverlay.addEventListener('click', closeAchievementLightbox);
    if (lightboxNextBtn) lightboxNextBtn.addEventListener('click', showNextImage);
    if (lightboxPrevBtn) lightboxPrevBtn.addEventListener('click', showPrevImage);

    document.addEventListener('keydown', (e) => {
      if (!achievementLightbox.classList.contains('active')) return;

      if (e.key === 'Escape') {
        closeAchievementLightbox();
      } else if (e.key === 'ArrowRight') {
        showNextImage();
      } else if (e.key === 'ArrowLeft') {
        showPrevImage();
      }
    });

    // Touch Swipe Support for Mobile
    let touchStartX = 0;
    let touchEndX = 0;

    if (lightboxMain) {
      lightboxMain.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      lightboxMain.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
      }, { passive: true });
    }

    function handleSwipe() {
      const swipeThreshold = 40;
      if (touchEndX < touchStartX - swipeThreshold) {
        showNextImage();
      }
      if (touchEndX > touchStartX + swipeThreshold) {
        showPrevImage();
      }
    }
  }

  // 6. Academic Evolution Gallery Slider Logic
  const sliderTrack = document.getElementById('sliderTrack');
  const sliderCard = document.getElementById('academicSliderCard');
  const prevBtn = document.getElementById('sliderPrevBtn');
  const nextBtn = document.getElementById('sliderNextBtn');
  const dots = document.querySelectorAll('#sliderDots .dot-btn');
  const slides = document.querySelectorAll('.academic-slide');

  if (sliderTrack && slides.length > 0) {
    let currentSlide = 0;
    const totalSlides = slides.length;
    let autoplayTimer = null;

    function goToSlide(index) {
      currentSlide = (index + totalSlides) % totalSlides;
      sliderTrack.style.transform = `translateX(-${currentSlide * 100}%)`;

      slides.forEach((slide, idx) => {
        if (idx === currentSlide) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });

      dots.forEach((dot, idx) => {
        if (idx === currentSlide) {
          dot.classList.add('active');
        } else {
          dot.classList.remove('active');
        }
      });
    }

    function startAutoplay() {
      stopAutoplay();
      autoplayTimer = setInterval(() => {
        goToSlide(currentSlide + 1);
      }, 4000);
    }

    function stopAutoplay() {
      if (autoplayTimer) {
        clearInterval(autoplayTimer);
        autoplayTimer = null;
      }
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        goToSlide(currentSlide + 1);
        startAutoplay();
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        goToSlide(currentSlide - 1);
        startAutoplay();
      });
    }

    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const slideIndex = parseInt(dot.getAttribute('data-slide'), 10);
        if (!isNaN(slideIndex)) {
          goToSlide(slideIndex);
          startAutoplay();
        }
      });
    });

    if (sliderCard) {
      sliderCard.addEventListener('mouseenter', stopAutoplay);
      sliderCard.addEventListener('mouseleave', startAutoplay);
    }

    // Touch Swipe Support for Slider on Mobile
    let sliderTouchStartX = 0;
    let sliderTouchEndX = 0;

    sliderTrack.addEventListener('touchstart', (e) => {
      sliderTouchStartX = e.changedTouches[0].screenX;
      stopAutoplay();
    }, { passive: true });

    sliderTrack.addEventListener('touchend', (e) => {
      sliderTouchEndX = e.changedTouches[0].screenX;
      const swipeThreshold = 35;
      if (sliderTouchEndX < sliderTouchStartX - swipeThreshold) {
        goToSlide(currentSlide + 1);
      } else if (sliderTouchEndX > sliderTouchStartX + swipeThreshold) {
        goToSlide(currentSlide - 1);
      }
      startAutoplay();
    }, { passive: true });

    // Start 4-second autoplay loop
    startAutoplay();

    // Academic Lightbox Modal Logic
    const academicLightbox = document.getElementById('academicLightbox');
    const academicLightboxImg = document.getElementById('academicLightboxImg');
    const academicLightboxTitle = document.getElementById('academicLightboxTitle');
    const academicLightboxDesc = document.getElementById('academicLightboxDesc');
    const academicLightboxClose = document.getElementById('academicLightboxClose');
    const academicLightboxOverlay = document.getElementById('academicLightboxOverlay');

    const timelineCards = document.querySelectorAll('.timeline-card, .academic-slide');
    timelineCards.forEach((card) => {
      const imgWrap = card.querySelector('.card-image, .slide-image-wrapper');
      if (imgWrap) {
        imgWrap.addEventListener('click', (e) => {
          if (e.target.closest('.inner-carousel-arrow') || e.target.closest('.inner-dot')) return;
          if (!academicLightbox) return;
          
          let imgEl = card.querySelector('.inner-carousel-slide.active img') || card.querySelector('.slide-img') || card.querySelector('img');
          const titleEl = card.querySelector('.card-title, .slide-title');
          const descEl = card.querySelector('.card-description, .slide-desc');

          if (imgEl && academicLightboxImg) {
            academicLightboxImg.src = imgEl.src;
            academicLightboxImg.alt = imgEl.alt || 'Academic Image';
          }
          if (academicLightboxTitle && titleEl) {
            academicLightboxTitle.textContent = titleEl.textContent;
          }
          if (academicLightboxDesc && descEl) {
            academicLightboxDesc.textContent = descEl.textContent;
          }

          if (academicLightbox) {
            academicLightbox.classList.add('active');
            academicLightbox.setAttribute('aria-hidden', 'false');
            document.body.classList.add('lightbox-open');
            document.body.style.overflow = 'hidden';
          }
        });

        imgWrap.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            imgWrap.click();
          }
        });
      }
    });

    function closeAcademicLightbox() {
      if (academicLightbox) {
        academicLightbox.classList.remove('active');
        academicLightbox.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('lightbox-open');
        document.body.style.overflow = '';
      }
    }

    if (academicLightboxClose) academicLightboxClose.addEventListener('click', closeAcademicLightbox);
    if (academicLightboxOverlay) academicLightboxOverlay.addEventListener('click', closeAcademicLightbox);

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && academicLightbox && academicLightbox.classList.contains('active')) {
        closeAcademicLightbox();
      }
    });
  }


  // 7. Inner Image Carousel for Academic Timeline Cards
  class InnerCarousel {
    constructor(container) {
      this.container = container;
      this.track = container.querySelector('.inner-carousel-track');
      this.prevBtn = container.querySelector('.inner-carousel-prev');
      this.nextBtn = container.querySelector('.inner-carousel-next');
      this.dotsContainer = container.querySelector('.inner-carousel-dots');

      // Read image list from data-images (comma-separated) — no runtime probing needed
      const rawImages = (container.getAttribute('data-images') || '').trim();
      this.images = rawImages ? rawImages.split(',').map(s => s.trim()).filter(Boolean) : [];

      this.currentIndex = 0;
      this.autoplayTimer = null;
      this.isHovering = false;
      this.touchStartX = 0;
      this.touchEndX = 0;

      if (this.images.length === 0) return;

      this.buildSlides();
      this.bindControls();
      this.bindEvents();
      this.startAutoplay();
    }

    buildSlides() {
      this.track.innerHTML = '';
      this.dotsContainer.innerHTML = '';

      this.images.forEach((src, index) => {
        // Build slide
        const slide = document.createElement('div');
        slide.className = 'inner-carousel-slide' + (index === 0 ? ' active' : '');
        const img = document.createElement('img');
        img.src = src;
        img.alt = '';
        img.className = 'slide-img';
        img.loading = 'lazy';
        slide.appendChild(img);
        this.track.appendChild(slide);

        // Build dot (only when there are multiple images)
        if (this.images.length > 1) {
          const dot = document.createElement('div');
          dot.className = 'inner-dot' + (index === 0 ? ' active' : '');
          const i = index;
          dot.addEventListener('click', (e) => {
            e.stopPropagation();
            this.goTo(i);
            this.resetAutoplay();
          });
          this.dotsContainer.appendChild(dot);
        }
      });

      // Cache NodeLists
      this.slides = this.track.querySelectorAll('.inner-carousel-slide');
      this.dots   = this.dotsContainer.querySelectorAll('.inner-dot');

      // Hide controls when only one image
      if (this.images.length <= 1) {
        this.prevBtn.style.display = 'none';
        this.nextBtn.style.display = 'none';
        this.dotsContainer.style.display = 'none';
      }
    }

    bindControls() {
      // Clone nodes to clear any old listeners
      const newPrev = this.prevBtn.cloneNode(true);
      const newNext = this.nextBtn.cloneNode(true);
      this.prevBtn.parentNode.replaceChild(newPrev, this.prevBtn);
      this.nextBtn.parentNode.replaceChild(newNext, this.nextBtn);
      this.prevBtn = newPrev;
      this.nextBtn = newNext;

      this.prevBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.prev();
        this.resetAutoplay();
      });
      this.nextBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.next();
        this.resetAutoplay();
      });
    }

    bindEvents() {
      // Pause autoplay while hovering
      this.container.addEventListener('mouseenter', () => {
        this.isHovering = true;
        this.stopAutoplay();
      });
      this.container.addEventListener('mouseleave', () => {
        this.isHovering = false;
        this.startAutoplay();
      });

      // Swipe support (mobile)
      this.container.addEventListener('touchstart', (e) => {
        this.touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });
      this.container.addEventListener('touchend', (e) => {
        this.touchEndX = e.changedTouches[0].screenX;
        const diff = this.touchStartX - this.touchEndX;
        if (Math.abs(diff) > 40) {
          diff > 0 ? this.next() : this.prev();
          this.resetAutoplay();
        }
      }, { passive: true });

      // Keyboard navigation (Left/Right arrows)
      this.container.addEventListener('keydown', (e) => {
        if (this.images.length > 1) {
          if (e.key === 'ArrowLeft')  { e.stopPropagation(); this.prev(); this.resetAutoplay(); }
          if (e.key === 'ArrowRight') { e.stopPropagation(); this.next(); this.resetAutoplay(); }
        }
      });
    }

    goTo(index) {
      if (!this.slides || this.images.length <= 1) return;
      this.slides[this.currentIndex].classList.remove('active');
      if (this.dots[this.currentIndex]) this.dots[this.currentIndex].classList.remove('active');
      this.currentIndex = (index + this.images.length) % this.images.length;
      this.slides[this.currentIndex].classList.add('active');
      if (this.dots[this.currentIndex]) this.dots[this.currentIndex].classList.add('active');
    }

    next() { this.goTo(this.currentIndex + 1); }
    prev() { this.goTo(this.currentIndex - 1); }

    startAutoplay() {
      if (this.images.length > 1 && !this.autoplayTimer) {
        this.autoplayTimer = setInterval(() => this.next(), 1200);
      }
    }

    stopAutoplay() {
      clearInterval(this.autoplayTimer);
      this.autoplayTimer = null;
    }

    resetAutoplay() {
      this.stopAutoplay();
      if (!this.isHovering) this.startAutoplay();
    }
  }

  // Initialize all inner carousels
  document.querySelectorAll('.inner-carousel-container').forEach(container => {
    new InnerCarousel(container);
  });

  // ═══════════════════════════════════════════════════════════
  // 8. ACHIEVEMENTS INFINITE HORIZONTAL CAROUSEL
  // Single-row, continuous right-to-left smooth movement (requestAnimationFrame + delta-time)
  // ═══════════════════════════════════════════════════════════
  function initAchievementCarousel() {
    const outer = document.getElementById('achCarouselOuter');
    const track = document.getElementById('achTrack');
    if (!outer || !track) return;

    // Remove any previously cloned cards to ensure clean start
    const originalCards = Array.from(track.querySelectorAll('.ach-carousel-card:not([data-clone="true"])'));
    if (originalCards.length === 0) return;

    // Clear track and re-add originals cleanly
    track.innerHTML = '';
    originalCards.forEach(card => track.appendChild(card));

    // Clone original cards twice (Set 2 & Set 3) for 100% seamless infinite loop
    for (let i = 0; i < 2; i++) {
      originalCards.forEach(card => {
        const clone = card.cloneNode(true);
        clone.setAttribute('data-clone', 'true');
        clone.setAttribute('aria-hidden', 'true');
        track.appendChild(clone);
      });
    }

    let position = 0;
    let isHovered = false;
    let isDragging = false;
    let startX = 0;
    let dragStartPos = 0;
    let hasDraggedFar = false;
    let lastTime = performance.now();

    // Movement speed: pixels per second (~60 for a lively, smooth motion)
    const SPEED = 60; 

    // Calculate exact width of 1 original card set (5 cards + gaps)
    function getSingleSetWidth() {
      const gap = parseFloat(window.getComputedStyle(track).gap) || 32;
      let totalWidth = 0;
      for (let i = 0; i < originalCards.length; i++) {
        totalWidth += originalCards[i].offsetWidth + gap;
      }
      return totalWidth;
    }

    // Animation Loop with delta-time smoothing
    function step(now) {
      const dt = Math.min((now - lastTime) / 1000, 0.1); // Cap dt at 100ms to prevent huge jumps on tab change
      lastTime = now;

      if (!isHovered && !isDragging) {
        const singleWidth = getSingleSetWidth();
        if (singleWidth > 0) {
          position += SPEED * dt;
          if (position >= singleWidth) {
            position -= singleWidth; // Seamless reset to identical position in set 2
          } else if (position < 0) {
            position += singleWidth;
          }
          track.style.transform = `translate3d(-${position}px, 0, 0)`;
        }
      }
      requestAnimationFrame(step);
    }

    // Hover Pause & Resume
    outer.addEventListener('mouseenter', () => { isHovered = true; });
    outer.addEventListener('mouseleave', () => {
      isHovered = false;
      isDragging = false;
    });

    // Mouse Drag (Desktop)
    outer.addEventListener('mousedown', (e) => {
      if (e.button !== 0) return;
      isDragging = true;
      hasDraggedFar = false;
      startX = e.clientX;
      dragStartPos = position;
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      const dx = startX - e.clientX;
      if (Math.abs(dx) > 5) hasDraggedFar = true;
      
      const singleWidth = getSingleSetWidth();
      if (singleWidth > 0) {
        position = dragStartPos + dx;
        while (position >= singleWidth) position -= singleWidth;
        while (position < 0) position += singleWidth;
        track.style.transform = `translate3d(-${position}px, 0, 0)`;
      }
    });

    window.addEventListener('mouseup', () => {
      if (isDragging) {
        setTimeout(() => { isDragging = false; }, 50);
      }
    });

    // Touch Swipe (Mobile)
    outer.addEventListener('touchstart', (e) => {
      isDragging = true;
      hasDraggedFar = false;
      startX = e.touches[0].clientX;
      dragStartPos = position;
    }, { passive: true });

    outer.addEventListener('touchmove', (e) => {
      if (!isDragging) return;
      const dx = startX - e.touches[0].clientX;
      if (Math.abs(dx) > 5) hasDraggedFar = true;

      const singleWidth = getSingleSetWidth();
      if (singleWidth > 0) {
        position = dragStartPos + dx;
        while (position >= singleWidth) position -= singleWidth;
        while (position < 0) position += singleWidth;
        track.style.transform = `translate3d(-${position}px, 0, 0)`;
      }
    }, { passive: true });

    outer.addEventListener('touchend', () => {
      isDragging = false;
    });

    // Prevent card click when dragging, allow normal click to open gallery lightbox
    track.addEventListener('click', (e) => {
      if (hasDraggedFar) {
        e.preventDefault();
        e.stopPropagation();
      }
    }, true);

    // Start smooth animation loop
    requestAnimationFrame(step);
  }

  // Initialize Carousel
  initAchievementCarousel();

  // ── 9. ABOUT SECTION PARALLAX & ANIMATED STATS COUNTER ──
  function initAboutParallaxAndStats() {
    // 1. Mouse Parallax for Dashboard & Profile Photo
    const dashCard = document.querySelector('.about-dashboard-card');
    const profileRing = document.querySelector('.about-profile-ring');

    function applyParallax(element, maxDegree = 8) {
      if (!element) return;
      const parent = element.parentElement;
      if (!parent) return;

      parent.addEventListener('mousemove', (e) => {
        const rect = parent.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        const rotX = (-y / (rect.height / 2)) * maxDegree;
        const rotY = (x / (rect.width / 2)) * maxDegree;
        element.style.transform = `rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg)`;
      });

      parent.addEventListener('mouseleave', () => {
        element.style.transform = 'rotateX(0deg) rotateY(0deg)';
      });
    }

    applyParallax(dashCard, 6);
    applyParallax(profileRing, 10);

    // 2. Count-Up Stats Counter Animation
    const statNumbers = document.querySelectorAll('.stat-number[data-count]');
    let hasCounted = false;

    function animateStats() {
      if (hasCounted) return;
      statNumbers.forEach(stat => {
        const target = parseInt(stat.getAttribute('data-count'), 10);
        if (isNaN(target)) return;

        let current = 0;
        const duration = 1500; // ms
        const increment = target / (duration / 16);

        const timer = setInterval(() => {
          current += increment;
          if (current >= target) {
            stat.textContent = target + '+';
            clearInterval(timer);
          } else {
            stat.textContent = Math.floor(current) + '+';
          }
        }, 16);
      });
      hasCounted = true;
    }

    const statsGrid = document.querySelector('.stats-grid');
    if (statsGrid && 'IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            animateStats();
            observer.disconnect();
          }
        });
      }, { threshold: 0.3 });
      observer.observe(statsGrid);
    } else {
      animateStats();
    }
  }

  initAboutParallaxAndStats();

  /* ==========================================================================
     SINGLE PERSISTENT LIVING SCIENTIST AVATAR CONTROLLER
     ========================================================================== */
  function initCornerAvatar() {
    const widget = document.getElementById('cornerAvatarWidget');
    const stage = document.getElementById('avatarStage');
    const characterLayer = document.getElementById('avatarCharacterLayer');
    const fullImg = document.getElementById('avatarFullImg');
    const propImg = document.getElementById('avatarPropImg');
    const speechBubble = document.getElementById('avatarSpeechBubble');
    const bubbleText = document.getElementById('avatarBubbleText');
    const bubbleIcon = document.getElementById('avatarBubbleIcon');
    const nextBtn = document.getElementById('avatarNextQuoteBtn');
    const closeBtn = document.getElementById('avatarCloseBtn');
    const dockBtn = document.getElementById('avatarDockBtn');

    if (!widget || !stage || !characterLayer || !fullImg) return;

    // 0. Preload Image Assets in Memory for instant zero-latency swapping
    const preloadedImages = {};
    const assetList = [
      './image/avatar_full.png',
      './image/avatar_full_blink.png',
      './image/avatar_full_happy.png',
      './image/props/prop_book.png',
      './image/props/prop_books.png',
      './image/props/prop_dna.png',
      './image/props/prop_laptop.png',
      './image/props/prop_microscope.png',
      './image/props/prop_clipboard.png',
      './image/props/prop_cert.png',
      './image/props/prop_skills.png',
      './image/props/prop_trophy.png',
      './image/props/prop_wave.png'
    ];
    assetList.forEach(src => {
      const img = new Image();
      img.src = src;
      preloadedImages[src] = img;
    });

    // 1. Section Configurations (with Responsive Desktop & Mobile Writing)
    const sectionConfigs = {
      'hero': {
        prop: null,
        baseYaw: 0,
        basePitch: 0,
        baseRoll: 0,
        isHappy: false,
        dialogue: "Hi! I'm Shunanda's lab assistant 🧬 Welcome to my portfolio!",
        mobileDialogue: "Hi! Welcome to Shunanda's lab 🧬",
        icon: "🧬"
      },
      'about': {
        prop: './image/props/prop_book.png',
        baseYaw: 14,    // Looking right toward About Me content
        basePitch: 1,
        baseRoll: 2,
        isHappy: false,
        dialogue: "Exploring molecular biology, genetic engineering & computational research.",
        mobileDialogue: "Molecular biology, genetics & computational research 📖",
        icon: "📖"
      },
      'journey': {
        prop: './image/props/prop_books.png',
        baseYaw: 4,
        basePitch: -8, // Looking up/forward with curiosity & academic growth
        baseRoll: -1,
        isHappy: false,
        dialogue: "Academic evolution: From molecular foundations to advanced bioinformatics.",
        mobileDialogue: "Academic evolution: Molecular foundations to bioinformatics 📚",
        icon: "📚"
      },
      'skills': {
        prop: './image/props/prop_skills.png',
        baseYaw: -14,   // Looking at floating skill icons
        basePitch: -4,
        baseRoll: -2,
        isHappy: false,
        dialogue: "Specialized in Python, R, RNA-seq, BLAST, Nextflow & in silico modeling.",
        mobileDialogue: "Python, R, RNA-seq, BLAST & in silico modeling ⚡",
        icon: "⚡"
      },
      'certifications': {
        prop: './image/props/prop_cert.png',
        baseYaw: 0,     // Proud gentle smile looking forward
        basePitch: -2,
        baseRoll: 0,
        isHappy: false,
        dialogue: "Certified by NPTEL & IIT Bombay in Evolutionary Dynamics & Genetic Engineering.",
        mobileDialogue: "NPTEL & IIT certified in Evolutionary Dynamics & Genetics 🎓",
        icon: "🎓"
      },
      'projects': {
        prop: './image/props/prop_microscope.png',
        baseYaw: -14,   // Looking into microscope eyepiece (hands-on research pose)
        basePitch: 14,
        baseRoll: -4,
        isHappy: false,
        dialogue: "Analyzing single-cell multi-omics & CIMA natural-cohort immune atlas!",
        mobileDialogue: "Single-cell multi-omics & immune atlas research 🔬",
        icon: "🔬"
      },
      'achievements': {
        prop: './image/props/prop_trophy.png',
        baseYaw: 0,
        basePitch: 2,
        baseRoll: -2,
        isHappy: true,  // Happy smile ^_^
        dialogue: "Celebrating university honors, athletic championships & centennial milestones!",
        mobileDialogue: "University honors & athletic milestones 🏆",
        icon: "🏆"
      },
      'contact': {
        prop: './image/props/prop_wave.png',
        baseYaw: 0,     // Waving & facing viewer
        basePitch: 0,
        baseRoll: 0,
        isHappy: false,
        dialogue: "Let's connect! Always open to bioinformatics research & collaborations.",
        mobileDialogue: "Let's connect! Open to research collaborations 👋",
        icon: "👋"
      }
    };

    // Scientific Facts Carousel (Responsive Writing)
    const biotechQuotes = [
      {
        icon: '🧬',
        text: "In silico biology turns billions of sequencing reads into targeted precision therapies.",
        mobileText: "In silico biology turns raw sequencing reads into targeted therapies 🧬"
      },
      {
        icon: '🔬',
        text: "Did you know? ~2 meters of DNA is packed inside every microscopic human cell!",
        mobileText: "~2 meters of DNA is packed inside every microscopic human cell! 🔬"
      },
      {
        icon: '💡',
        text: "Human DNA is 99.9% identical across all people; 0.1% holds our unique genetic variance.",
        mobileText: "Human DNA is 99.9% identical; 0.1% holds all unique variance 💡"
      },
      {
        icon: '📊',
        text: "Single-cell RNA-seq resolves cell states that bulk sequencing could never distinguish.",
        mobileText: "Single-cell RNA-seq reveals hidden cell states with precision 📊"
      },
      {
        icon: '🧪',
        text: "CRISPR-Cas9 enables precise genome editing for therapeutic gene correction.",
        mobileText: "CRISPR-Cas9 enables targeted genome editing for precision therapies 🧪"
      },
      {
        icon: '⚡',
        text: "Move your mouse around — I'll keep an eye on whatever you're exploring!",
        mobileText: "Tap or scroll around — I'll follow what you explore! ⚡"
      }
    ];

    let currentSectionKey = 'hero';
    let currentQuoteIdx = 0;
    let quoteTimer = null;
    let isBlinking = false;
    let currentActiveDialogue = { icon: '🧬', text: '', mobileText: '' };

    function resolveAppropriateText(text, mobileText) {
      const isMobileScreen = window.innerWidth <= 600;
      if (isMobileScreen && mobileText) {
        return mobileText;
      }
      return text;
    }

    // 2. Smooth In-Place State Transition (Single Persistent Instance)
    function setSectionState(sectionKey) {
      if (!sectionConfigs[sectionKey]) return;
      if (currentSectionKey === sectionKey) return;
      currentSectionKey = sectionKey;
      const cfg = sectionConfigs[sectionKey];

      // Update Base Character Expression
      if (!isBlinking) {
        if (cfg.isHappy) {
          fullImg.src = './image/avatar_full_happy.png';
        } else {
          fullImg.src = './image/avatar_full.png';
        }
      }

      // Smooth Single-Prop Transition
      if (propImg) {
        propImg.classList.remove('prop-active');
        setTimeout(() => {
          if (cfg.prop) {
            propImg.src = cfg.prop;
            propImg.style.display = 'block';
            void propImg.offsetWidth;
            propImg.classList.add('prop-active');
          } else {
            propImg.style.display = 'none';
            propImg.src = '';
          }
        }, 180);
      }

      // Show Section Dialogue (Responsive Writing)
      showDialogue(cfg.icon, cfg.dialogue, cfg.mobileDialogue);
    }

    function showDialogue(icon, text, mobileText = null) {
      if (!bubbleText || !bubbleIcon || !speechBubble) return;
      currentActiveDialogue = { icon, text, mobileText: mobileText || text };

      const displayText = resolveAppropriateText(text, mobileText);

      speechBubble.style.opacity = '0';
      speechBubble.style.transform = 'translateY(6px) scale(0.96)';

      setTimeout(() => {
        bubbleIcon.textContent = icon;
        bubbleText.textContent = displayText;
        speechBubble.style.opacity = '1';
        speechBubble.style.transform = 'translateY(0) scale(1)';
      }, 160);
    }

    // Dynamic viewport resize listener to adapt speech text without flicker
    let resizeTextTimer = null;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTextTimer);
      resizeTextTimer = setTimeout(() => {
        if (currentActiveDialogue.text && bubbleText) {
          const newText = resolveAppropriateText(currentActiveDialogue.text, currentActiveDialogue.mobileText);
          if (bubbleText.textContent !== newText) {
            bubbleText.textContent = newText;
          }
        }
      }, 200);
    }, { passive: true });

    function startFactAutoCycle() {
      if (quoteTimer) clearInterval(quoteTimer);
      quoteTimer = setInterval(() => {
        currentQuoteIdx = (currentQuoteIdx + 1) % biotechQuotes.length;
        const q = biotechQuotes[currentQuoteIdx];
        showDialogue(q.icon, q.text, q.mobileText);
      }, 14000);
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        currentQuoteIdx = (currentQuoteIdx + 1) % biotechQuotes.length;
        const q = biotechQuotes[currentQuoteIdx];
        showDialogue(q.icon, q.text, q.mobileText);
        startFactAutoCycle();
      });
    }

    // 3. Bidirectional Section Observer (Works both when scrolling UP and DOWN)
    const trackedSections = [
      { id: 'hero', key: 'hero' },
      { id: 'about', key: 'about' },
      { id: 'journey', key: 'journey' },
      { id: 'skills', key: 'skills' },
      { id: 'projects', key: 'projects' },
      { id: 'achievements', key: 'achievements' }
    ];

    const certSection = document.querySelector('.skd-cert-section');
    const footerElement = document.querySelector('.main-footer');

    // Deterministic scroll position calculator to ensure perfect sync in both directions
    function evaluateActiveSection() {
      const viewportCenter = window.innerHeight * 0.45;

      if (footerElement) {
        const fRect = footerElement.getBoundingClientRect();
        if (fRect.top <= window.innerHeight * 0.8) {
          setSectionState('contact');
          return;
        }
      }

      if (certSection) {
        const cRect = certSection.getBoundingClientRect();
        if (cRect.top <= viewportCenter && cRect.bottom >= viewportCenter) {
          setSectionState('certifications');
          return;
        }
      }

      // Check standard section elements
      for (let i = trackedSections.length - 1; i >= 0; i--) {
        const item = trackedSections[i];
        const el = document.getElementById(item.id);
        if (el) {
          const rect = el.getBoundingClientRect();
          if (rect.top <= viewportCenter && rect.bottom >= viewportCenter) {
            setSectionState(item.key);
            return;
          }
        }
      }

      // Top of page default
      if (window.scrollY < 200) {
        setSectionState('hero');
      }
    }

    let scrollTick = false;
    window.addEventListener('scroll', () => {
      if (!scrollTick) {
        requestAnimationFrame(() => {
          evaluateActiveSection();
          scrollTick = false;
        });
        scrollTick = true;
      }
    }, { passive: true });

    // Initial evaluation
    evaluateActiveSection();

    // 4. Autonomous Motion & Gaze Physics Engine (Single Instance with Mobile Touch Intelligence)
    let mouseX = window.innerWidth * 0.5;
    let mouseY = window.innerHeight * 0.4;
    let lastMouseMoveTime = performance.now();
    let isTouchActive = false;
    let scrollTimeout = null;

    let currentYaw = 0;
    let currentPitch = 0;
    let currentRoll = 0;
    let currentDx = 0;
    let currentDy = 0;

    let autonomousTargetYaw = 0;
    let autonomousTargetPitch = 0;
    let nextLookShiftTime = performance.now() + 2000;

    function onPointerMove(x, y, fromTouch = false) {
      mouseX = x;
      mouseY = y;
      lastMouseMoveTime = performance.now();
      if (fromTouch) {
        isTouchActive = true;
      }
    }

    window.addEventListener('mousemove', (e) => onPointerMove(e.clientX, e.clientY, false), { passive: true });
    window.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches[0]) {
        onPointerMove(e.touches[0].clientX, e.touches[0].clientY, true);
      }
    }, { passive: true });
    window.addEventListener('touchmove', (e) => {
      if (e.touches && e.touches[0]) {
        onPointerMove(e.touches[0].clientX, e.touches[0].clientY, true);
      }
    }, { passive: true });
    window.addEventListener('touchend', () => {
      isTouchActive = false;
      lastMouseMoveTime = performance.now() - 1400;
    }, { passive: true });
    window.addEventListener('touchcancel', () => {
      isTouchActive = false;
      lastMouseMoveTime = performance.now() - 1400;
    }, { passive: true });

    // Smooth mobile scroll indicator & bubble dimming so reading content is never obstructed
    window.addEventListener('scroll', () => {
      if (window.innerWidth <= 768 && speechBubble && !widget.classList.contains('minimized')) {
        speechBubble.classList.add('scrolling-dim');
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
          speechBubble.classList.remove('scrolling-dim');
        }, 450);
      }
    }, { passive: true });

    function renderAvatarFrame(now) {
      const timeSinceMove = now - lastMouseMoveTime;
      const cfg = sectionConfigs[currentSectionKey] || sectionConfigs['hero'];

      const rect = stage.getBoundingClientRect();
      const avatarCenterX = rect.left + rect.width * 0.5;
      const avatarCenterY = rect.top + rect.height * 0.38;

      // 4.1 Autonomous natural glance shift
      if (now > nextLookShiftTime) {
        const glanceOptions = [
          { yaw: 0, pitch: 0 },
          { yaw: -7, pitch: -2 },
          { yaw: 8, pitch: 2 },
          { yaw: 2, pitch: -5 },
          { yaw: -5, pitch: 6 },
          { yaw: cfg.baseYaw, pitch: cfg.basePitch }
        ];
        const chosen = glanceOptions[Math.floor(Math.random() * glanceOptions.length)];
        autonomousTargetYaw = chosen.yaw;
        autonomousTargetPitch = chosen.pitch;
        nextLookShiftTime = now + 3200 + Math.random() * 2800;
      }

      // 4.2 Multi-frequency organic breathing & drift
      const t = now * 0.0012;
      const organicDriftYaw = Math.sin(t * 0.8) * 3.0 + Math.sin(t * 1.6) * 1.5;
      const organicDriftPitch = Math.cos(t * 0.6) * 2.4 + Math.sin(t * 1.2) * 1.0;
      const organicDriftRoll = organicDriftYaw * 0.14;

      let targetYaw = cfg.baseYaw + autonomousTargetYaw + organicDriftYaw;
      let targetPitch = cfg.basePitch + autonomousTargetPitch + organicDriftPitch;
      let targetRoll = cfg.baseRoll + organicDriftRoll;

      const isMobile = window.innerWidth <= 768;
      const isCompact = window.innerWidth <= 480;
      const maxInteractDuration = isTouchActive ? 2200 : (isMobile ? 1200 : 2200);

      // 4.3 Pointer interaction blending
      if (timeSinceMove < maxInteractDuration) {
        const dx = mouseX - avatarCenterX;
        const dy = mouseY - avatarCenterY;
        const screenW = window.innerWidth || 1920;
        const screenH = window.innerHeight || 1080;

        const maxYaw = isCompact ? 10 : (isMobile ? 14 : 18);
        const maxPitch = isCompact ? 8 : (isMobile ? 11 : 14);

        const cursorYawDelta = (dx / screenW) * maxYaw;
        const cursorPitchDelta = (dy / screenH) * maxPitch;

        targetYaw = Math.max(-20, Math.min(20, cfg.baseYaw + cursorYawDelta + organicDriftYaw * 0.4));
        targetPitch = Math.max(-15, Math.min(15, cfg.basePitch + cursorPitchDelta + organicDriftPitch * 0.4));
        targetRoll = targetYaw * 0.14;
      }

      const targetDx = (targetYaw / 25) * 3.5;
      const targetDy = (targetPitch / 20) * 2.5;

      const lerp = 0.055;
      currentYaw += (targetYaw - currentYaw) * lerp;
      currentPitch += (targetPitch - currentPitch) * lerp;
      currentRoll += (targetRoll - currentRoll) * lerp;
      currentDx += (targetDx - currentDx) * lerp;
      currentDy += (targetDy - currentDy) * lerp;

      // Apply transform to the single character layer
      characterLayer.style.transform = `perspective(650px) rotateY(${currentYaw.toFixed(2)}deg) rotateX(${(-currentPitch).toFixed(2)}deg) rotateZ(${currentRoll.toFixed(2)}deg) translate3d(${currentDx.toFixed(2)}px, ${currentDy.toFixed(2)}px, 4px)`;

      requestAnimationFrame(renderAvatarFrame);
    }

    requestAnimationFrame(renderAvatarFrame);

    // 5. In-Place Blinking Engine (Swaps image src on the single element)
    function triggerBlink() {
      if (currentSectionKey === 'achievements') {
        setTimeout(triggerBlink, 3000);
        return;
      }
      isBlinking = true;
      fullImg.src = './image/avatar_full_blink.png';

      setTimeout(() => {
        const cfg = sectionConfigs[currentSectionKey] || sectionConfigs['hero'];
        fullImg.src = cfg.isHappy ? './image/avatar_full_happy.png' : './image/avatar_full.png';
        isBlinking = false;

        // 22% chance of quick organic double-blink
        if (Math.random() < 0.22) {
          setTimeout(() => {
            isBlinking = true;
            fullImg.src = './image/avatar_full_blink.png';
            setTimeout(() => {
              const currentCfg = sectionConfigs[currentSectionKey] || sectionConfigs['hero'];
              fullImg.src = currentCfg.isHappy ? './image/avatar_full_happy.png' : './image/avatar_full.png';
              isBlinking = false;
            }, 100);
          }, 130);
        }
      }, 110);

      const nextBlink = 2800 + Math.random() * 3200;
      setTimeout(triggerBlink, nextBlink);
    }

    setTimeout(triggerBlink, 2200);

    // 6. Click Interaction & Joy Bounce (with Touch Swipe Discrimination)
    let touchStartX = 0;
    let touchStartY = 0;
    let isTouchDrag = false;

    stage.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches[0]) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        isTouchDrag = false;
      }
    }, { passive: true });

    stage.addEventListener('touchmove', (e) => {
      if (e.touches && e.touches[0]) {
        const diffX = Math.abs(e.touches[0].clientX - touchStartX);
        const diffY = Math.abs(e.touches[0].clientY - touchStartY);
        if (diffX > 10 || diffY > 10) {
          isTouchDrag = true;
        }
      }
    }, { passive: true });

    function triggerAvatarJoy() {
      stage.classList.remove('joy-bounce');
      void stage.offsetWidth;
      stage.classList.add('joy-bounce');

      currentQuoteIdx = (currentQuoteIdx + 1) % biotechQuotes.length;
      const q = biotechQuotes[currentQuoteIdx];
      showDialogue(q.icon, q.text, q.mobileText);
      startFactAutoCycle();
    }

    stage.addEventListener('click', () => {
      if (isTouchDrag) {
        isTouchDrag = false;
        return;
      }
      triggerAvatarJoy();
    });

    stage.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        stage.click();
      }
    });

    // 7. Minimize & Restore Controls
    function minimizeAvatar() {
      widget.classList.add('minimized');
      if (dockBtn) {
        dockBtn.style.display = 'inline-flex';
        dockBtn.style.opacity = '0';
        setTimeout(() => {
          dockBtn.style.opacity = '1';
        }, 50);
      }
      try {
        sessionStorage.setItem('shunanda_avatar_minimized', 'true');
      } catch (err) {}
    }

    function restoreAvatar() {
      widget.classList.remove('minimized');
      if (dockBtn) {
        dockBtn.style.display = 'none';
      }
      try {
        sessionStorage.removeItem('shunanda_avatar_minimized');
      } catch (err) {}
      startFactAutoCycle();
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        minimizeAvatar();
      });
    }

    if (dockBtn) {
      dockBtn.addEventListener('click', () => {
        restoreAvatar();
      });
    }

    startFactAutoCycle();

    try {
      if (sessionStorage.getItem('shunanda_avatar_minimized') === 'true') {
        minimizeAvatar();
      }
    } catch (err) {}
  }

  // Initialize
  initAboutParallaxAndStats();
  initCornerAvatar();
});
