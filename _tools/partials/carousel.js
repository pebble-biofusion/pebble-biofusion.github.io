  // ===== Carousel Functionality =====
  (function() {
    'use strict';

    const carousel = {
      slides: document.querySelectorAll('.carousel-slide'),
      indicators: document.querySelectorAll('.carousel-indicator'),
      prevBtn: document.querySelector('.carousel-control.prev'),
      nextBtn: document.querySelector('.carousel-control.next'),
      pauseIndicator: document.querySelector('.carousel-pause-indicator'),
      currentIndex: 0,
      interval: null,
      isPaused: false,
      autoScrollDelay: 4000, // 4 seconds

      init() {
        if (this.slides.length === 0) return;

        // Set initial state
        this.slides[0].classList.add('active');
        this.indicators[0].classList.add('active');

        // Bind events
        this.bindEvents();

        // Start auto-scroll
        this.startAutoScroll();
      },

      bindEvents() {
        // Previous button
        this.prevBtn.addEventListener('click', () => {
          this.prevSlide();
          this.restartAutoScroll();
        });

        // Next button
        this.nextBtn.addEventListener('click', () => {
          this.nextSlide();
          this.restartAutoScroll();
        });

        // Indicator clicks
        this.indicators.forEach((indicator, index) => {
          indicator.addEventListener('click', () => {
            this.goToSlide(index);
            this.restartAutoScroll();
          });
        });

        // Pause on hover
        const container = document.querySelector('.carousel-container');
        container.addEventListener('mouseenter', () => {
          this.pause();
        });

        container.addEventListener('mouseleave', () => {
          this.resume();
        });

        // Touch support
        let touchStartX = 0;
        let touchEndX = 0;

        container.addEventListener('touchstart', (e) => {
          touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        container.addEventListener('touchend', (e) => {
          touchEndX = e.changedTouches[0].screenX;
          this.handleSwipe(touchStartX, touchEndX);
        }, { passive: true });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
          if (e.key === 'ArrowLeft') {
            this.prevSlide();
            this.restartAutoScroll();
          } else if (e.key === 'ArrowRight') {
            this.nextSlide();
            this.restartAutoScroll();
          } else if (e.key === ' ') {
            e.preventDefault();
            this.togglePause();
          }
        });
      },

      handleSwipe(startX, endX) {
        const swipeThreshold = 50;
        const diff = startX - endX;

        if (Math.abs(diff) > swipeThreshold) {
          if (diff > 0) {
            this.nextSlide();
          } else {
            this.prevSlide();
          }
          this.restartAutoScroll();
        }
      },

      goToSlide(index) {
        // Remove current active classes
        this.slides[this.currentIndex].classList.remove('active');
        this.indicators[this.currentIndex].classList.remove('active');

        // Set new current index
        this.currentIndex = index;

        // Add active classes
        this.slides[this.currentIndex].classList.add('active');
        this.indicators[this.currentIndex].classList.add('active');
      },

      nextSlide() {
        const nextIndex = (this.currentIndex + 1) % this.slides.length;
        this.goToSlide(nextIndex);
      },

      prevSlide() {
        const prevIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
        this.goToSlide(prevIndex);
      },

      startAutoScroll() {
        if (this.interval) return;
        this.interval = setInterval(() => {
          if (!this.isPaused) {
            this.nextSlide();
          }
        }, this.autoScrollDelay);
      },

      stopAutoScroll() {
        if (this.interval) {
          clearInterval(this.interval);
          this.interval = null;
        }
      },

      restartAutoScroll() {
        this.stopAutoScroll();
        this.startAutoScroll();
      },

      pause() {
        this.isPaused = true;
        this.pauseIndicator.style.opacity = '1';
      },

      resume() {
        this.isPaused = false;
        this.pauseIndicator.style.opacity = '0';
      },

      togglePause() {
        if (this.isPaused) {
          this.resume();
        } else {
          this.pause();
        }
      }
    };

    // Initialize carousel when DOM is ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => carousel.init());
    } else {
      carousel.init();
    }
  })();
