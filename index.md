---
layout: home
---

<div class="pebble-home">

  <section class="about-section">

    <p class="intro">
      <strong>PEBBLE BioFusion 2026</strong> is designed from the ground up for the age of AI. We are not adding AI as a tool on top of a traditional curriculum. Instead, we are rethinking what a summer school should train when AI makes tutorials, literature review, coding, and draft generation available on demand. In this new landscape, three things become critically important:
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
        <div class="stat-number">500<span>+</span></div>
        <div class="stat-label">contributor</div>
      </div>
      <div class="stat">
        <div class="stat-number">50<span>+</span></div>
        <div class="stat-label">products</div>
      </div>
      <div class="stat">
        <div class="stat-number">3<span>+</span></div>
        <div class="stat-label">years</div>
      </div>
    </div>

  </section>

</div>

<style>
  /* ===== Layout ===== */
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
  @media (max-width: 768px) {
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
</style>
