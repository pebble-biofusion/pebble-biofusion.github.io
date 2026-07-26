---
layout: page
title: "Ignition"
permalink: /summerschool/2026/ignition/
---

<div class="ignition">

  <!-- ===== 07.26 ===== -->
  <section class="day">
    <button class="day-toggle" type="button" aria-expanded="false">
      <span class="day-arrow">▸</span>
      <span class="day-date">07.26 Sunday Q2: Complex Cellular Behaviors</span>
    </button>
    <ul class="talk-list collapsed">
      <li class="talk">
        <span class="talk-title">Mechanism-driven single-cell modelling</span>
        <span class="talk-speaker">Yuhao Chen</span>
      </li>
      <li class="talk">
        <span class="talk-title">Data-driven approaches</span>
        <span class="talk-speaker">Tailin Wu</span>
      </li>
      <li class="talk">
        <span class="talk-title">Multiscale modelling</span>
        <span class="talk-speaker">Zhennan Zhou</span>
      </li>
    </ul>
  </section>

  <!-- ===== 07.25 ===== -->
  <section class="day">
    <button class="day-toggle" type="button" aria-expanded="false">
      <span class="day-arrow">▸</span>
      <span class="day-date">07.25 Saturday Q1: Cellular Information Processing</span>
    </button>
    <ul class="talk-list collapsed">
      <li class="talk">
        <span class="talk-title">Control theory</span>
        <span class="talk-speaker">Fangzhou Xiao</span>
      </li>
      <li class="talk">
        <span class="talk-title">Protein computation</span>
        <span class="talk-speaker">Zibo Chen</span>
      </li>
      <li class="talk">
        <span class="talk-title">Probabilistic reasoning in cells</span>
        <span class="talk-speaker">Zitong (Jerry) Wang</span>
      </li>
      <li class="talk">
        <span class="talk-title">A scientific story that spreads like a virus</span>
        <span class="talk-speaker">Fangzhou Xiao</span>
      </li>
      <li class="talk">
        <span class="talk-title">From a story to a publishable paper: A deep dive in AI-native scientific research</span>
        <span class="talk-speaker">Fangzhou Xiao</span>
      </li>
    </ul>
  </section>

</div>

<style>
  .ignition {
    width: 100%;
  }

  /* ===== Day block ===== */
  .day {
    margin-bottom: 1rem;
  }

  .day:last-of-type {
    margin-bottom: 0;
  }

  /* ===== Collapsible day header ===== */
  .day-toggle {
    display: flex;
    align-items: baseline;
    gap: 0.6rem;
    width: 100%;
    background: none;
    border: none;
    border-bottom: 1px solid #f3f4f6;
    padding: 0.85rem 0;
    font-family: inherit;
    text-align: left;
    cursor: pointer;
  }

  .day-arrow {
    display: inline-block;
    font-size: 0.75rem;
    color: #9ca3af;
    transition: transform 0.2s, color 0.2s;
  }

  .day-toggle[aria-expanded="true"] .day-arrow {
    transform: rotate(90deg);
    color: #FF6C0C;
  }

  .day-date {
    font-size: 1.2rem;
    font-weight: 600;
    color: #374151;
    letter-spacing: 0.5px;
    transition: color 0.2s;
  }

  .day-toggle:hover .day-date {
    color: #FF6C0C;
  }

  /* ===== Talk list ===== */
  .talk-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .talk-list.collapsed {
    display: none;
  }

  .talk {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    padding: 1rem 0;
    flex-wrap: wrap;
  }

  .talk:not(:last-child) {
    border-bottom: 1px solid #f3f4f6;
  }

  /* Default: no material yet — plain gray, not clickable */
  .talk-title {
    font-size: 1rem;
    font-weight: 500;
    color: #9ca3af;
    line-height: 1.5;
  }

  /* When a talk has material, it becomes a clickable link */
  a.talk-title {
    color: #1f2937;
    text-decoration: none;
    cursor: pointer;
    transition: color 0.2s;
  }

  a.talk-title:hover {
    color: #FF6C0C;
  }

  .talk-speaker {
    font-size: 0.83rem;
    color: #9ca3af;
    flex-shrink: 0;
  }

  /* ===== Responsive ===== */
  @media (max-width: 600px) {
    .talk {
      flex-direction: column;
      gap: 0.3rem;
      align-items: flex-start;
    }

    .talk-speaker {
      text-align: left;
    }
  }
</style>

<script>
  document.querySelectorAll('.day-toggle').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var expanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', !expanded);
      var list = this.nextElementSibling;
      if (list) {
        list.classList.toggle('collapsed');
      }
    });
  });
</script>
