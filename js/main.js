console.log('Portfolio initialized');

document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once visible
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.section, .hero-content, .project-card').forEach(el => {
        el.classList.add('fade-in-up');
        observer.observe(el);
    });

    // Theme Initialization
    const html = document.documentElement;
    const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
    html.setAttribute('data-theme', savedTheme);

    // Theme Selector Event Listener
    const themeSelect = document.getElementById('theme-select');
    if (themeSelect) {
        themeSelect.value = savedTheme;
        themeSelect.addEventListener('change', (e) => {
            const theme = e.target.value;
            html.setAttribute('data-theme', theme);
            localStorage.setItem('portfolio-theme', theme);
        });
    }

    // Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const sidebar = document.querySelector('.sidebar');
    const body = document.body;

    if (mobileBtn && sidebar) {
        mobileBtn.addEventListener('click', () => {
            const isOpen = sidebar.classList.toggle('active');
            mobileBtn.classList.toggle('active');

            // Prevent scrolling when menu is open
            if (isOpen) {
                body.style.overflow = 'hidden';
            } else {
                body.style.overflow = '';
            }
        });

        // Close mobile menu when clicking a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                sidebar.classList.remove('active');
                mobileBtn.classList.remove('active');
                body.style.overflow = '';
            });
        });
    }

    // Smooth Scroll for anchor links (polyfill/enhancement)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Set current year in footer
    console.log('Setting current year in footer');
    document.getElementById('year').textContent = new Date().getFullYear();
});
