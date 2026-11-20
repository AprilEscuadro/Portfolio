// Mobile navigation
const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.main-nav');
toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? '\u00d7' : '\u2630';
});
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.textContent = '\u2630';
}));

// Project filters (a card can belong to several categories)
document.querySelectorAll('.filter').forEach(button => {
    button.addEventListener('click', () => {
        document.querySelector('.filter.active')?.classList.remove('active');
        button.classList.add('active');
        const selected = button.dataset.filter;
        document.querySelectorAll('.work-card').forEach(card => {
            const cats = card.dataset.category.split(' ');
            card.classList.toggle('hidden', selected !== 'all' && !cats.includes(selected));
        });
    });
});

// Highlight the nav link of the section currently in view
const navLinks = document.querySelectorAll('.main-nav a');
const sections = [...navLinks].map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
function setActive() {
    let current = sections[0];
    sections.forEach(sec => {
        if (sec.id === 'about' && window.scrollY < 300) return; // About sits inside the hero
        if (sec.getBoundingClientRect().top <= 160) current = sec;
    });
    navLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + current.id));
}
window.addEventListener('scroll', setActive, { passive: true });
setActive();