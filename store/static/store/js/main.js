// =============================================
// VastraVerse — Enhanced JavaScript
// =============================================

document.addEventListener('DOMContentLoaded', () => {

    // --- Theme Toggle ---
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        const icon = themeToggle.querySelector('i');
        
        // Update icon on initial load
        if (document.documentElement.getAttribute('data-theme') === 'dark') {
            icon.classList.replace('fa-moon', 'fa-sun');
        }

        themeToggle.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            if (newTheme === 'dark') {
                icon.classList.replace('fa-moon', 'fa-sun');
            } else {
                icon.classList.replace('fa-sun', 'fa-moon');
            }
            
            // Pulse animation for the button
            themeToggle.style.transform = 'scale(1.3)';
            setTimeout(() => {
                themeToggle.style.transform = 'scale(1)';
            }, 200);
        });
    }

    // --- Mobile Navigation Toggle ---
    const mobileToggle = document.getElementById('mobileToggle');
    const navLinks = document.getElementById('navLinks');

    if (mobileToggle && navLinks) {
        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.replace('fa-bars', 'fa-times');
            } else {
                icon.classList.replace('fa-times', 'fa-bars');
            }
        });

        // Close menu on link click
        navLinks.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                mobileToggle.querySelector('i').classList.replace('fa-times', 'fa-bars');
            });
        });

        // Close menu on click outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.nav-inner') && navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileToggle.querySelector('i').classList.replace('fa-times', 'fa-bars');
            }
        });
    }

    // --- Sticky Navbar Shadow on Scroll ---
    const navbar = document.getElementById('navbar');
    if (navbar) {
        const handleScroll = () => {
            if (window.scrollY > 20) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        };
        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();
    }

    // --- Auto-dismiss Alerts with smooth exit ---
    document.querySelectorAll('.alert').forEach((alert, index) => {
        setTimeout(() => {
            alert.style.transition = 'all 0.5s cubic-bezier(0.4, 0, 0.2, 1)';
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(120%) scale(0.9)';
            setTimeout(() => alert.remove(), 500);
        }, 3500 + (index * 600));
    });

    // --- Smooth Scroll for anchor links with offset ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offset = navbar ? navbar.offsetHeight + 20 : 80;
                const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });

    // --- Intersection Observer: Staggered Reveal Animation ---
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                // Add stagger delay based on position in viewport
                const siblings = Array.from(entry.target.parentElement.children);
                const index = siblings.indexOf(entry.target);
                const delay = index * 80;

                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, delay);

                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.08,
        rootMargin: '0px 0px -40px 0px'
    });

    // Apply to cards and sections
    const animateElements = document.querySelectorAll(
        '.product-card, .category-card, .feature-card, .cart-item'
    );
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(28px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        revealObserver.observe(el);
    });

    // --- Section titles reveal ---
    const titleObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                titleObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.section-title, .section-subtitle, .page-title').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease 0.1s, transform 0.6s ease 0.1s';
        titleObserver.observe(el);
    });

    // --- Add to Cart Button Feedback ---
    document.querySelectorAll('.btn-add-cart').forEach(btn => {
        btn.addEventListener('click', function (e) {
            // Brief pulse effect on the button
            this.style.transform = 'scale(1.3)';
            setTimeout(() => {
                this.style.transform = '';
            }, 200);

            // Bounce the cart icon
            const cartIcon = document.getElementById('cartIcon');
            if (cartIcon) {
                cartIcon.style.transition = 'transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';
                cartIcon.style.transform = 'scale(1.3)';
                setTimeout(() => {
                    cartIcon.style.transform = 'scale(1)';
                }, 400);
            }
        });
    });

    // --- Hero Parallax Effect ---
    const hero = document.querySelector('.hero');
    if (hero) {
        const heroContent = hero.querySelector('.hero-content');
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            if (scrolled < hero.offsetHeight) {
                const rate = scrolled * 0.3;
                if (heroContent) {
                    heroContent.style.transform = `translateY(${rate}px)`;
                    heroContent.style.opacity = 1 - (scrolled / hero.offsetHeight) * 0.6;
                }
            }
        }, { passive: true });
    }

    // --- Image Lazy Load with Fade-in ---
    document.querySelectorAll('.product-img, .category-img').forEach(img => {
        if (img.tagName === 'IMG') {
            img.style.opacity = '0';
            img.style.transition = 'opacity 0.5s ease';
            if (img.complete) {
                img.style.opacity = '1';
            } else {
                img.addEventListener('load', function () {
                    this.style.opacity = '1';
                });
                img.addEventListener('error', function () {
                    this.style.opacity = '1';
                });
            }
        }
    });

    // --- Product Detail Image Zoom on Hover ---
    const detailImg = document.querySelector('.product-detail-img img');
    if (detailImg) {
        const container = detailImg.parentElement;
        container.addEventListener('mousemove', (e) => {
            const rect = container.getBoundingClientRect();
            const x = ((e.clientX - rect.left) / rect.width) * 100;
            const y = ((e.clientY - rect.top) / rect.height) * 100;
            detailImg.style.transformOrigin = `${x}% ${y}%`;
            detailImg.style.transform = 'scale(1.15)';
        });
        container.addEventListener('mouseleave', () => {
            detailImg.style.transformOrigin = 'center center';
            detailImg.style.transform = 'scale(1)';
        });
    }

    // --- Newsletter Form Feedback ---
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const btn = this.querySelector('.newsletter-btn');
            const input = this.querySelector('.newsletter-input');
            if (input.value.trim()) {
                btn.textContent = '✓ Subscribed!';
                btn.style.background = 'linear-gradient(135deg, #10b981, #34d399)';
                input.value = '';
                input.disabled = true;
                setTimeout(() => {
                    btn.textContent = 'Subscribe';
                    btn.style.background = '';
                    input.disabled = false;
                }, 3000);
            }
        });
    }

    // --- Size selector visual feedback ---
    document.querySelectorAll('.size-options input[type="radio"]').forEach(radio => {
        radio.addEventListener('change', function () {
            const label = this.nextElementSibling;
            if (label) {
                label.style.transition = 'all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';
                label.style.transform = 'scale(1.08)';
                setTimeout(() => {
                    label.style.transform = '';
                }, 200);
            }
        });
    });

});
