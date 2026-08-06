const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.type(), msg.text()));
  page.on('pageerror', error => console.log('BROWSER ERROR:', error.message));

  console.log('Navigating to live site...');
  await page.goto('https://shunandasharkarbio-boop.github.io/portfolio/', { waitUntil: 'networkidle' });
  
  console.log('Taking screenshot...');
  await page.screenshot({ path: 'live_site.png', fullPage: true });

  // Evaluate visibility of about section
  const aboutInfo = await page.evaluate(() => {
    const about = document.querySelector('#about');
    if (!about) return 'NOT FOUND';
    const rect = about.getBoundingClientRect();
    const style = window.getComputedStyle(about);
    return {
      rect,
      display: style.display,
      visibility: style.visibility,
      opacity: style.opacity,
      height: about.offsetHeight,
    };
  });
  console.log('About Section Info:', aboutInfo);

  // Evaluate animation elements
  const animElements = await page.evaluate(() => {
    const els = document.querySelectorAll('.about-section .animate-on-scroll');
    return Array.from(els).map(el => {
      const style = window.getComputedStyle(el);
      return {
        className: el.className,
        display: style.display,
        visibility: style.visibility,
        opacity: style.opacity
      };
    });
  });
  console.log('Animate Elements in About Section:', animElements);

  await browser.close();
})();
