import re
import os

workspace = r"d:\shunanda( natto don't delete)\shunanda portfolio"
app_file = os.path.join(workspace, "app.js")
style_file = os.path.join(workspace, "style.css")

# 1. Update app.js (InnerCarousel class)
with open(app_file, 'r', encoding='utf-8') as f:
    js = f.read()

# We need to replace the entire InnerCarousel class.
# Let's find it using regex.
new_class = '''class InnerCarousel {
    constructor(container) {
      this.container = container;
      this.folder = container.getAttribute('data-folder');
      this.track = container.querySelector('.inner-carousel-track');
      this.prevBtn = container.querySelector('.inner-carousel-prev');
      this.nextBtn = container.querySelector('.inner-carousel-next');
      this.dotsContainer = container.querySelector('.inner-carousel-dots');
      
      this.images = [];
      this.currentIndex = 0;
      this.autoplayTimer = null;
      this.isHovering = false;
      this.touchStartX = 0;
      this.touchEndX = 0;

      // Optimistically add the first image immediately so there's no blank flash
      this.images.push(`${this.folder}img_1.png`);
      this.renderSlides();
      this.setupControls();
      this.bindEvents();

      // Probe for more images asynchronously
      this.probeMoreImages();
    }

    async probeMoreImages() {
      let imgIndex = 2;
      let keepLooking = true;

      while (keepLooking) {
        const src = `${this.folder}img_${imgIndex}.png`;
        const exists = await this.checkImageExists(src);
        if (exists) {
          this.images.push(src);
          this.appendSlide(src, this.images.length - 1);
          imgIndex++;
        } else {
          keepLooking = false;
        }
      }

      // If we found more images, update controls and autoplay
      if (this.images.length > 1) {
        this.prevBtn.style.display = 'flex';
        this.nextBtn.style.display = 'flex';
        this.dotsContainer.style.display = 'flex';
        this.setupControls(); // Rebind or ensure bound
        this.startAutoplay();
      }
    }

    checkImageExists(url) {
      return new Promise(resolve => {
        // Use HEAD request for speed, fallback to Image object
        fetch(url, { method: 'HEAD' })
          .then(res => resolve(res.ok))
          .catch(() => {
            const img = new Image();
            img.onload = () => resolve(true);
            img.onerror = () => resolve(false);
            img.src = url;
          });
      });
    }

    renderSlides() {
      this.track.innerHTML = '';
      this.dotsContainer.innerHTML = '';
      
      this.images.forEach((src, index) => {
        this.appendSlide(src, index, false);
      });

      if (this.images.length <= 1) {
        this.prevBtn.style.display = 'none';
        this.nextBtn.style.display = 'none';
        this.dotsContainer.style.display = 'none';
      }
    }

    appendSlide(src, index, updateDOM = true) {
      const slide = document.createElement('div');
      slide.className = `inner-carousel-slide ${index === 0 ? 'active' : ''}`;
      const img = document.createElement('img');
      img.src = src;
      img.className = 'slide-img'; // CRITICAL FOR ZOOM FX
      img.loading = "lazy";
      slide.appendChild(img);
      this.track.appendChild(slide);

      const dot = document.createElement('div');
      dot.className = `inner-dot ${index === 0 ? 'active' : ''}`;
      dot.addEventListener('click', (e) => {
        e.stopPropagation();
        this.goTo(index);
      });
      this.dotsContainer.appendChild(dot);

      this.slides = this.track.querySelectorAll('.inner-carousel-slide');
      this.dots = this.dotsContainer.querySelectorAll('.inner-dot');
    }

    setupControls() {
      // Remove old listeners to prevent duplicates
      const newPrev = this.prevBtn.cloneNode(true);
      const newNext = this.nextBtn.cloneNode(true);
      this.prevBtn.parentNode.replaceChild(newPrev, this.prevBtn);
      this.nextBtn.parentNode.replaceChild(newNext, this.nextBtn);
      this.prevBtn = newPrev;
      this.nextBtn = newNext;

      this.prevBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.prev();
      });
      this.nextBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.next();
      });
    }

    bindEvents() {
      this.container.addEventListener('mouseenter', () => {
        this.isHovering = true;
        this.stopAutoplay();
      });
      
      this.container.addEventListener('mouseleave', () => {
        this.isHovering = false;
        this.startAutoplay();
      });

      this.container.addEventListener('touchstart', (e) => {
        this.touchStartX = e.changedTouches[0].screenX;
        this.stopAutoplay();
      }, { passive: true });

      this.container.addEventListener('touchend', (e) => {
        this.touchEndX = e.changedTouches[0].screenX;
        this.handleSwipe();
        if (!this.isHovering) this.startAutoplay();
      }, { passive: true });

      this.container.addEventListener('keydown', (e) => {
        if (this.images.length > 1) {
          if (e.key === 'ArrowLeft') {
            e.stopPropagation();
            this.prev();
          } else if (e.key === 'ArrowRight') {
            e.stopPropagation();
            this.next();
          }
        }
      });
    }

    handleSwipe() {
      const swipeThreshold = 40;
      if (this.touchEndX < this.touchStartX - swipeThreshold) {
        this.next();
      }
      if (this.touchEndX > this.touchStartX + swipeThreshold) {
        this.prev();
      }
    }

    goTo(index) {
      if (this.images.length <= 1 || !this.slides || !this.slides[this.currentIndex]) return;
      this.slides[this.currentIndex].classList.remove('active');
      if (this.dots[this.currentIndex]) this.dots[this.currentIndex].classList.remove('active');

      this.currentIndex = index;

      if (this.slides[this.currentIndex]) this.slides[this.currentIndex].classList.add('active');
      if (this.dots[this.currentIndex]) this.dots[this.currentIndex].classList.add('active');
    }

    next() {
      if (this.images.length <= 1) return;
      const newIndex = (this.currentIndex + 1) % this.images.length;
      this.goTo(newIndex);
    }

    prev() {
      if (this.images.length <= 1) return;
      const newIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
      this.goTo(newIndex);
    }

    startAutoplay() {
      if (this.images.length > 1 && !this.autoplayTimer) {
        this.autoplayTimer = setInterval(() => {
          this.next();
        }, 3000);
      }
    }

    stopAutoplay() {
      if (this.autoplayTimer) {
        clearInterval(this.autoplayTimer);
        this.autoplayTimer = null;
      }
    }
  }'''

js = re.sub(r'class InnerCarousel \{.*?\n  \}', new_class, js, flags=re.DOTALL)
with open(app_file, 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated app.js")

# 2. Update style.css (Move inner arrows and dots)
with open(style_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Modify .inner-carousel-arrow position so it doesn't overlap global arrows
css = re.sub(
    r'\.inner-carousel-arrow \{[^}]*top:\s*50%;[^}]*transform:\s*translateY\(-50%\);[^}]*\}',
    r'''.inner-carousel-arrow {
  position: absolute;
  bottom: 45px;
  background: rgba(0, 0, 0, 0.6);
  color: var(--color-primary);
  border: 1px solid var(--color-border);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  cursor: pointer;
  z-index: 10;
  opacity: 0;
  transition: opacity 0.3s ease, background 0.3s ease, transform 0.3s ease;
}''',
    css, flags=re.DOTALL
)

css = re.sub(r'\.inner-carousel-arrow:hover \{[^}]*transform:\s*translateY\(-50%\)\s*scale\(1\.1\);[^}]*\}',
    r'''.inner-carousel-arrow:hover {
  background: rgba(0, 245, 155, 0.2);
  transform: scale(1.1);
}''', css)

# Ensure inner-carousel-dots are visible and a bit higher
css = re.sub(r'\.inner-carousel-dots \{[^}]*bottom:\s*15px;[^}]*\}',
    r'''.inner-carousel-dots {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
  z-index: 10;
  opacity: 0;
  transition: opacity 0.3s ease;
}''', css)

with open(style_file, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated style.css")
