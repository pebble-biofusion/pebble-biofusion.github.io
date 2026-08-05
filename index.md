---
layout: home
---

<div class="pebble-home">

  <!-- ===== Photo Carousel ===== -->
  <section class="hero-carousel" aria-label="Workshop Photo Carousel">
    <div class="carousel-container">
      <div class="carousel-slides">
        
        <!-- Slide 1 -->
        <div class="carousel-slide" data-index="0">
          <img src="{{ site.baseurl }}/images/carousel/LJY_7939.jpg" alt="Pebble BioFusion Workshop Photo 1">
        </div>
        
        <!-- Slide 2 -->
        <div class="carousel-slide" data-index="1">
          <img src="{{ site.baseurl }}/images/carousel/A1_06206.jpg" alt="Pebble BioFusion Workshop Photo 2">
        </div>
        
        <!-- Slide 3 -->
        <div class="carousel-slide" data-index="2">
          <img src="{{ site.baseurl }}/images/carousel/A1_05198.jpg" alt="Pebble BioFusion Workshop Photo 3">
        </div>
        
        <!-- Slide 4 -->
        <div class="carousel-slide" data-index="3">
          <img src="{{ site.baseurl }}/images/carousel/A1_05311.jpg" alt="Pebble BioFusion Workshop Photo 4">
        </div>
        
        <!-- Slide 5 -->
        <div class="carousel-slide" data-index="4">
          <img src="{{ site.baseurl }}/images/carousel/A1_05455.jpg" alt="Pebble BioFusion Workshop Photo 5">
        </div>
        
        <!-- Slide 6 -->
        <div class="carousel-slide" data-index="5">
          <img src="{{ site.baseurl }}/images/carousel/A1_04375.jpg" alt="Pebble BioFusion Workshop Photo 6">
        </div>
        
      </div>
      
      <!-- Navigation Controls -->
      <button class="carousel-control prev" aria-label="Previous slide" type="button">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      
      <button class="carousel-control next" aria-label="Next slide" type="button">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>
      
      <!-- Indicators -->
      <div class="carousel-indicators">
        <button class="carousel-indicator active" data-index="0" aria-label="Go to slide 1" type="button"></button>
        <button class="carousel-indicator" data-index="1" aria-label="Go to slide 2" type="button"></button>
        <button class="carousel-indicator" data-index="2" aria-label="Go to slide 3" type="button"></button>
        <button class="carousel-indicator" data-index="3" aria-label="Go to slide 4" type="button"></button>
        <button class="carousel-indicator" data-index="4" aria-label="Go to slide 5" type="button"></button>
        <button class="carousel-indicator" data-index="5" aria-label="Go to slide 6" type="button"></button>
      </div>
      
      <!-- Pause Indicator -->
      <div class="carousel-pause-indicator" aria-hidden="true">
        <span class="pause-icon">❚❚</span>
      </div>
    </div>
  </section>

  <section class="about-section">

    <p class="intro">
      <strong>PEBBLE BioFusion 2026</strong> is designed from the ground up for the age of AI. We are not adding AI as a tool on top of a traditional curriculum. Instead, we are rethinking what a workshop should train when AI makes tutorials, literature review, coding, and draft generation available on demand. In this new landscape, three things become critically important:
    </p>

    <ul class="skills">
      <li>
        <span class="skill-name">Taste</span>
        <span class="skill-desc">the ability to ask deep, well-chosen questions. Which problems are alive? Which framings reveal new structure?</span>
      </li>
      <li>
        <span class="skill-name">Rigor</span>
        <span class="skill-desc">the ability to develop a full, in-depth chain of logic that tells a complete, convincing story.</span>
      </li>
      <li>
        <span class="skill-name">Courage</span>
        <span class="skill-desc">the willingness to ask bold questions, and the determination to pursue them all the way through.</span>
      </li>
    </ul>

    <p class="closing">
      These are precisely what AI does not reliably provide. They are what <strong>PEBBLE BioFusion</strong> trains.
    </p>

    <div class="stats">
      <div class="stat">
        <div class="stat-number">50<span>+</span></div>
        <div class="stat-label">contributors</div>
      </div>
      <div class="stat">
        <div class="stat-number">20<span>+</span></div>
        <div class="stat-label">products</div>
      </div>
      <div class="stat">
        <div class="stat-number">2<span>+</span></div>
        <div class="stat-label">years</div>
      </div>
    </div>

  </section>

</div>

<style>
  /* ===== Carousel Styles ===== */
  .hero-carousel {
    width: 100%;
    margin-bottom: 2.5rem;
    position: relative;
  }

  .carousel-container {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 10;
    max-width: 900px;
    max-height: 550px;
    margin: 0 auto;
    overflow: hidden;
    border-radius: 12px;
    background: #f9fafb;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  }

  .carousel-slides {
    position: relative;
    width: 100%;
    height: 100%;
  }

  .carousel-slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    pointer-events: none;
  }

  .carousel-slide.active {
    opacity: 1;
    pointer-events: auto;
    z-index: 1;
  }

  .carousel-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  /* ===== Navigation Controls ===== */
  .carousel-control {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.9);
    border: none;
    border-radius: 50%;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    transition: all 0.2s ease;
    color: #374151;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .carousel-control:hover {
    background: #fff;
    color: #FF6C0C;
    box-shadow: 0 4px 12px rgba(255, 108, 12, 0.3);
  }

  .carousel-control:focus {
    outline: 2px solid #FF6C0C;
    outline-offset: 2px;
  }

  .carousel-control.prev {
    left: 1rem;
  }

  .carousel-control.next {
    right: 1rem;
  }

  /* ===== Indicators ===== */
  .carousel-indicators {
    position: absolute;
    bottom: 1rem;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 0.5rem;
    z-index: 10;
  }

  .carousel-indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.5);
    border: 2px solid rgba(255, 255, 255, 0.8);
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .carousel-indicator:hover {
    background: rgba(255, 255, 255, 0.8);
    transform: scale(1.1);
  }

  .carousel-indicator.active {
    background: #FF6C0C;
    border-color: #FF6C0C;
    transform: scale(1.2);
  }

  .carousel-indicator:focus {
    outline: 2px solid #FF6C0C;
    outline-offset: 2px;
  }

  /* ===== Pause Indicator ===== */
  .carousel-pause-indicator {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: rgba(0, 0, 0, 0.5);
    color: white;
    padding: 0.4rem 0.6rem;
    border-radius: 20px;
    font-size: 0.75rem;
    opacity: 0;
    transition: opacity 0.3s ease;
    z-index: 10;
  }

  .carousel-container:hover .carousel-pause-indicator {
    opacity: 1;
  }

  .pause-icon {
    font-size: 0.8rem;
    letter-spacing: 1px;
  }

  /* ===== Carousel Layout ===== */
  .pebble-home {
    width: 100%;
  }

  /* ===== Intro & Closing paragraphs ===== */
  .intro,
  .closing {
    font-size: 1.1rem;
    line-height: 1.85;
    color: #374151;
    margin: 0;
  }

  .intro {
    margin-bottom: 3rem;
  }

  .closing {
    margin-bottom: 5rem;
  }

  .intro strong,
  .closing strong {
    color: #1f2937;
    font-weight: 600;
  }

  /* ===== Three core skills (name | description) ===== */
  .skills {
    list-style: none;
    padding: 0;
    margin: 0 0 3rem 0;
  }

  .skills li {
    display: flex;
    gap: 2rem;
    align-items: baseline;
    margin-bottom: 1.75rem;
  }

  .skills li:last-child {
    margin-bottom: 0;
  }

  .skill-name {
    font-size: 1rem;
    font-weight: 600;
    color: #FF6C0C;
    letter-spacing: 0.2px;
    flex-shrink: 0;
  }

  .skill-desc {
    font-size: 0.95rem;
    line-height: 1.7;
    color: #6b7280;
    flex: 1;
  }

  /* ===== Stats ===== */
  .stats {
    display: flex;
    gap: 2.5rem;
    flex-wrap: wrap;
  }

  .stat {
    width: 86px;
    height: 86px;
    border: 1px solid #e5e7eb;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: border-color 0.2s, transform 0.2s;
  }

  .stat:hover {
    border-color: #FF6C0C;
    transform: translateY(-2px);
  }

  .stat-number {
    font-size: 1.5rem;
    font-weight: 600;
    color: #FF6C0C;
    line-height: 1;
  }

  .stat-label {
    font-size: 0.65rem;
    color: #9ca3af;
    margin-top: 0.3rem;
    text-transform: lowercase;
    letter-spacing: 0.3px;
  }

  /* ===== Responsive ===== */
  @media (max-width: 1200px) {
    .carousel-container {
      max-width: 750px;
      max-height: 500px;
    }
  }

  @media (max-width: 768px) {
    .carousel-container {
      aspect-ratio: 16 / 10;
      max-width: 100%;
      max-height: 400px;
    }

    .carousel-control {
      width: 40px;
      height: 40px;
    }

    .carousel-control.prev {
      left: 0.5rem;
    }

    .carousel-control.next {
      right: 0.5rem;
    }

    .carousel-indicator {
      width: 10px;
      height: 10px;
    }

    .skills li {
      flex-direction: column;
      gap: 0.35rem;
    }

    .skill-name {
      font-size: 1rem;
      text-align: left;
    }

    .stats {
      gap: 1.5rem;
    }

    .stat {
      width: 74px;
      height: 74px;
    }

    .stat-number {
      font-size: 1.3rem;
    }
  }

  @media (max-width: 480px) {
    .carousel-container {
      aspect-ratio: 4 / 3;
      max-width: 100%;
      max-height: 350px;
      border-radius: 8px;
    }

    .carousel-control {
      width: 36px;
      height: 36px;
    }

    .carousel-control.prev {
      left: 0.25rem;
    }

    .carousel-control.next {
      right: 0.25rem;
    }

    .carousel-indicator {
      width: 8px;
      height: 8px;
      gap: 0.4rem;
    }

    .carousel-pause-indicator {
      top: 0.5rem;
      right: 0.5rem;
      font-size: 0.7rem;
      padding: 0.3rem 0.5rem;
    }
  }
</style>

<script>
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
</script>
