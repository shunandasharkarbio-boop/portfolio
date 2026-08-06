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
  const animateElements = document.querySelectorAll('.animate-on-scroll, .timeline-item, .project-card, .achievement-card');
  
  if ('IntersectionObserver' in window) {
    const observerOptions = {
      root: null,
      rootMargin: '50px 0px 50px 0px',
      threshold: 0.05
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    animateElements.forEach(el => scrollObserver.observe(el));
  } else {
    // Fallback for older browsers
    animateElements.forEach(el => {
      el.classList.add('is-visible');
      el.classList.add('visible');
    });
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
      document.body.style.overflow = 'hidden';
    }

    function closeAchievementLightbox() {
      achievementLightbox.classList.remove('active');
      achievementLightbox.setAttribute('aria-hidden', 'true');
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

    achievementCards.forEach(card => {
      const imgContainer = card.querySelector('.achievement-img-container');
      if (imgContainer) {
        imgContainer.addEventListener('click', () => openAchievementLightbox(card));
        imgContainer.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            openAchievementLightbox(card);
          }
        });
      }
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

    slides.forEach(slide => {
      const imgWrap = slide.querySelector('.slide-image-wrapper');
      if (imgWrap) {
        imgWrap.addEventListener('click', () => {
          const imgEl = slide.querySelector('.slide-img');
          const titleEl = slide.querySelector('.slide-title');
          const descEl = slide.querySelector('.slide-desc');

          if (academicLightboxImg && imgEl) {
            academicLightboxImg.src = imgEl.src;
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
});
