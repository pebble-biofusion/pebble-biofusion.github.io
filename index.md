---
layout: home
title: PEBBLE
---

<div class="pebble-home">

  <!-- Main Two-Column Layout -->
  <div class="home-grid">

    <!-- Left Column: Workshop -->
    <section class="home-column workshop-column">
      <h2 class="column-heading">workshop</h2>

      <div class="workshop-year">
        <h3 class="year-label">2026</h3>
        <ul class="workshop-items">
          <li>
            <a href="{{ site.baseurl }}/years/2026/" class="workshop-link">
              <span class="item-marker"></span>
              ignition
            </a>
          </li>
          <li>
            <a href="{{ site.baseurl }}/years/2026/" class="workshop-link">
              <span class="item-marker"></span>
              synthesis
            </a>
          </li>
        </ul>
      </div>
    </section>

    <!-- Divider -->
    <div class="column-divider"></div>

    <!-- Right Column: About -->
    <section class="home-column about-column">
      <h2 class="column-heading">About</h2>

      <div class="mission-block">
        <p class="intro-text">
          <strong>PEBBLE BioFusion 2026</strong> is designed from the ground up for the age of AI. We are not adding AI as a tool on top of a traditional curriculum. Instead, we are rethinking what a summer school should train when AI makes tutorials, literature review, coding, and draft generation available on demand. In this new landscape, three things become critically important:
        </p>
        <ul class="core-skills">
          <li><span class="skill-name">Taste</span> &mdash; the ability to ask deep, well-chosen questions. Which problems are alive? Which framings reveal new structure?</li>
          <li><span class="skill-name">Scientific Reasoning</span> &mdash; the ability to develop a full, in-depth chain of logic that tells a complete, convincing story.</li>
          <li><span class="skill-name">Courage</span> &mdash; the willingness to ask bold questions, and the determination to pursue them all the way through.</li>
        </ul>
        <p class="intro-text">
          These are precisely what AI does not reliably provide. They are what <strong>PEBBLE BioFusion</strong> trains.
        </p>
      </div>

      <!-- Stats with Circles -->
      <div class="stats-row">
        <div class="stat-circle">
          <div class="stat-number">500<span class="stat-plus">+</span></div>
          <div class="stat-label">contributor</div>
        </div>
        <div class="stat-circle">
          <div class="stat-number">50<span class="stat-plus">+</span></div>
          <div class="stat-label">products</div>
        </div>
        <div class="stat-circle">
          <div class="stat-number">3<span class="stat-plus">+</span></div>
          <div class="stat-label">years</div>
        </div>
      </div>
    </section>

  </div>

</div>

<style>
  /* ===== Home Page Layout ===== */
  .pebble-home {
    width: 100%;
  }

  .home-grid {
    display: grid;
    grid-template-columns: 1fr 1px 1.4fr;
    gap: 3rem;
    align-items: start;
    margin-top: 1rem;
  }

  /* ===== Columns ===== */
  .home-column {
    padding: 0.5rem 0;
  }

  .column-heading {
    font-size: 1.1rem;
    font-weight: 600;
    text-transform: lowercase;
    letter-spacing: 0.5px;
    color: #1f2937;
    margin: 0 0 2rem 0;
    padding-bottom: 0.6rem;
    border-bottom: 2px solid #1f2937;
  }

  /* ===== Divider ===== */
  .column-divider {
    background: #e0e0e0;
    width: 1px;
    height: 100%;
    min-height: 300px;
    align-self: stretch;
  }

  /* ===== Workshop Column ===== */
  .workshop-year {
    margin-bottom: 1.5rem;
  }

  .year-label {
    font-size: 1rem;
    font-weight: 500;
    color: #6b7280;
    margin: 0 0 1rem 0;
    letter-spacing: 1px;
  }

  .workshop-items {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .workshop-items li {
    margin-bottom: 0.5rem;
  }

  .workshop-link {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    color: #1f2937;
    text-decoration: none;
    font-size: 1rem;
    padding: 0.4rem 0;
    transition: color 0.2s, transform 0.2s;
  }

  .workshop-link:hover {
    color: #0066cc;
    transform: translateX(4px);
  }

  .item-marker {
    width: 6px;
    height: 6px;
    background: #1f2937;
    border-radius: 50%;
    flex-shrink: 0;
    transition: background 0.2s;
  }

  .workshop-link:hover .item-marker {
    background: #0066cc;
  }

  /* ===== About Column ===== */
  .mission-block {
    margin-bottom: 2.5rem;
  }

  .intro-text {
    font-size: 1rem;
    line-height: 1.75;
    color: #374151;
    margin: 0 0 1.25rem 0;
  }

  .intro-text strong {
    color: #1f2937;
    font-weight: 600;
  }

  .core-skills {
    list-style: none;
    padding: 0;
    margin: 1.5rem 0;
  }

  .core-skills li {
    font-size: 1rem;
    line-height: 1.7;
    color: #374151;
    margin-bottom: 0.85rem;
    padding-left: 1.3rem;
    position: relative;
  }

  .core-skills li::before {
    content: "•";
    position: absolute;
    left: 0;
    top: 0;
    color: #FF6C0C;
    font-weight: 700;
    font-size: 1.1rem;
  }

  .skill-name {
    font-weight: 700;
    color: #FF6C0C;
  }

  /* ===== Stats Circles ===== */
  .stats-row {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    margin-top: 2rem;
  }

  .stat-circle {
    width: 90px;
    height: 90px;
    border: 2px solid #1f2937;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: transform 0.2s, border-color 0.2s;
  }

  .stat-circle:hover {
    transform: translateY(-3px);
    border-color: #0066cc;
  }

  .stat-number {
    font-size: 1.4rem;
    font-weight: 600;
    color: #1f2937;
    line-height: 1;
  }

  .stat-plus {
    font-size: 1rem;
    font-weight: 500;
  }

  .stat-label {
    font-size: 0.7rem;
    color: #6b7280;
    margin-top: 0.2rem;
    text-transform: lowercase;
  }

  /* ===== Responsive ===== */
  @media (max-width: 768px) {
    .home-grid {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .column-divider {
      width: 100%;
      height: 1px;
      min-height: 1px;
    }

    .stats-row {
      gap: 1rem;
    }

    .stat-circle {
      width: 78px;
      height: 78px;
    }
  }
</style>
