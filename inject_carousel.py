import re

workspace = r"d:\shunanda( natto don't delete)\shunanda portfolio"

# ─── 1. REMOVE DUPLICATE OLD CARDS (if any leftover) ─────────────────────────
with open(f"{workspace}/index.html", 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the old floating card block that was left over from the bad partial replace
old_block_pattern = re.compile(
    r"\s*<!-- Card 1: University Handball Team -->.*?</section>",
    re.DOTALL
)
# Count matches
matches = list(old_block_pattern.finditer(html))
print(f"Old block matches: {len(matches)}")

# Remove every match after the first section tag
cleaned = old_block_pattern.sub('', html, count=5)
with open(f"{workspace}/index.html", 'w', encoding='utf-8') as f:
    f.write(cleaned)
print("Cleaned index.html")

# ─── 2. INJECT CSS ───────────────────────────────────────────────────────────
with open(f"{workspace}/style.css", 'r', encoding='utf-8') as f:
    css = f.read()

if ".ach-carousel-wrapper" not in css:
    carousel_css = """
/* ═══════════════════════════════════════════════════
   ACHIEVEMENTS INFINITE HORIZONTAL CAROUSEL
   ═══════════════════════════════════════════════════ */
.ach-carousel-wrapper {
  position: relative;
  width: 100%;
  overflow: hidden;
  margin-top: 3.5rem;
  /* Padding so the cards pop up on hover without clipping */
  padding: 1.5rem 0 2.5rem;
}

/* Edge fade overlays */
.ach-fade {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 120px;
  z-index: 20;
  pointer-events: none;
}
.ach-fade-left {
  left: 0;
  background: linear-gradient(90deg, var(--color-bg, #040914) 0%, transparent 100%);
}
.ach-fade-right {
  right: 0;
  background: linear-gradient(-90deg, var(--color-bg, #040914) 0%, transparent 100%);
}

/* The scrolling row — width set by JS */
.ach-track {
  display: flex;
  gap: 2rem;
  width: max-content;
  will-change: transform;
  /* animation driven by JS requestAnimationFrame */
}

/* Individual carousel card sizing */
.ach-carousel-card {
  /* Desktop: 3 visible → ~(100vw - padding) / 3 */
  flex: 0 0 clamp(280px, calc(33.33vw - 3rem), 420px);
  width: clamp(280px, calc(33.33vw - 3rem), 420px);
  cursor: pointer;
  /* Override translateY so hover lift doesn't clip */
  transform-origin: center bottom;
  transition:
    transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1),
    border-color 0.3s ease,
    box-shadow 0.3s ease;
}

.ach-carousel-card:hover {
  transform: translateY(-10px) scale(1.025);
  border-color: rgba(0, 245, 155, 0.75);
  box-shadow:
    0 20px 50px rgba(0, 245, 155, 0.22),
    0 0 30px rgba(0, 210, 196, 0.18),
    inset 0 1px 1px rgba(0, 245, 155, 0.25);
}

.ach-carousel-card:hover::before {
  opacity: 1;
  box-shadow: 0 0 18px var(--color-primary);
}

/* Tablet: 2 cards visible */
@media (max-width: 1024px) {
  .ach-carousel-card {
    flex: 0 0 clamp(240px, calc(50vw - 2.5rem), 380px);
    width: clamp(240px, calc(50vw - 2.5rem), 380px);
  }
  .ach-fade { width: 60px; }
}

/* Mobile: 1 card visible */
@media (max-width: 640px) {
  .ach-carousel-card {
    flex: 0 0 clamp(240px, calc(85vw), 340px);
    width: clamp(240px, calc(85vw), 340px);
  }
  .ach-fade { width: 30px; }
}
"""
    css += carousel_css
    with open(f"{workspace}/style.css", 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated style.css")
else:
    print("CSS already injected, skipping")

# ─── 3. INJECT JS ────────────────────────────────────────────────────────────
with open(f"{workspace}/app.js", 'r', encoding='utf-8') as f:
    js = f.read()

if "achCarouselInit" not in js:
    carousel_js = """
  // ── 8. ACHIEVEMENTS INFINITE HORIZONTAL CAROUSEL ──────────────────────────
  function achCarouselInit() {
    const wrapper = document.getElementById('achCarouselWrapper');
    const track   = document.getElementById('achTrack');
    if (!wrapper || !track) return;

    // Clone all original cards to make the loop seamless
    const origCards = Array.from(track.children);
    if (origCards.length === 0) return;

    // Clone enough times so we always have cards off-screen
    // We need at least 2 full sets for a seamless loop
    const cloneCount = 3; // total = origCards * (1 + cloneCount)
    for (let c = 0; c < cloneCount; c++) {
      origCards.forEach(card => {
        const clone = card.cloneNode(true);
        clone.setAttribute('aria-hidden', 'true');
        track.appendChild(clone);
      });
    }

    // Rebind lightbox on ALL cards (including clones)
    rebindCarouselCardListeners();

    const SPEED = 0.6;      // px per frame at 60fps  ≈ 36px/s
    let offset   = 0;
    let paused   = false;
    let rafId    = null;

    // Width of ONE full set of original cards (cards + gaps)
    function getSetWidth() {
      const gap = parseFloat(getComputedStyle(track).gap) || 32;
      return origCards.reduce((acc, card) => acc + card.offsetWidth + gap, 0);
    }

    function tick() {
      if (!paused) {
        offset += SPEED;
        const setW = getSetWidth();
        // When we've scrolled one full set, jump back seamlessly
        if (setW > 0 && offset >= setW) {
          offset -= setW;
        }
        track.style.transform = `translate3d(-${offset}px, 0, 0)`;
      }
      rafId = requestAnimationFrame(tick);
    }

    // Pause on hover
    wrapper.addEventListener('mouseenter', () => { paused = true; });
    wrapper.addEventListener('mouseleave', () => { paused = false; });

    // Touch / swipe drag
    let touchStartX = 0, touchOffsetStart = 0;
    wrapper.addEventListener('touchstart', (e) => {
      paused = true;
      touchStartX = e.touches[0].clientX;
      touchOffsetStart = offset;
    }, { passive: true });
    wrapper.addEventListener('touchmove', (e) => {
      const dx = touchStartX - e.touches[0].clientX;
      offset = touchOffsetStart + dx;
      // Keep offset in range
      const setW = getSetWidth();
      if (setW > 0) {
        offset = ((offset % setW) + setW) % setW;
      }
      track.style.transform = `translate3d(-${offset}px, 0, 0)`;
    }, { passive: true });
    wrapper.addEventListener('touchend', () => {
      paused = false;
    }, { passive: true });

    // Mouse-wheel horizontal scroll
    wrapper.addEventListener('wheel', (e) => {
      if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) {
        e.preventDefault();
        offset += e.deltaX * 0.8;
        const setW = getSetWidth();
        if (setW > 0) offset = ((offset % setW) + setW) % setW;
      }
    }, { passive: false });

    // Start animation
    rafId = requestAnimationFrame(tick);
  }

  function rebindCarouselCardListeners() {
    const track = document.getElementById('achTrack');
    if (!track) return;

    // Remove existing listeners by replacing nodes is expensive on clones;
    // instead use event delegation on the track
    track.addEventListener('click', (e) => {
      // Find the card ancestor
      const card = e.target.closest('.ach-carousel-card');
      if (!card || card.getAttribute('aria-hidden') === 'true') return;

      // Reuse existing lightbox logic — dispatch a custom event
      card.dispatchEvent(new CustomEvent('open-achievement-lightbox', { bubbles: true }));
    });
  }

  achCarouselInit();
"""

    # Insert before the closing }); of DOMContentLoaded
    js = js.rstrip()
    if js.endswith('});'):
        js = js[:-3] + carousel_js + '\n});\n'
    else:
        js += '\n' + carousel_js

    with open(f"{workspace}/app.js", 'w', encoding='utf-8') as f:
        f.write(js)
    print("Updated app.js")
else:
    print("JS already injected, skipping")
