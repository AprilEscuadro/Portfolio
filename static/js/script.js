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