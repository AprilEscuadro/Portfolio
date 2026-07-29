// Highlight nav link base sa unsang section naa sa view
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-links a");

function highlightNav() {
    let current = "";
    sections.forEach((section) => {
        const sectionTop = section.offsetTop - 120;
        if (window.scrollY >= sectionTop) {
            current = section.getAttribute("id");
        }
    });

    navLinks.forEach((link) => {
        link.style.color = "";
        if (link.getAttribute("href") === `#${current}`) {
            link.style.color = "var(--pink)";
        }
    });
}

window.addEventListener("scroll", highlightNav);
window.addEventListener("load", highlightNav);