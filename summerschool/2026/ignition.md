---
layout: page
title: "Ignition"
permalink: /summerschool/2026/ignition/
---

<div class="ignition">

  <!-- ===== 07.26 ===== -->
  <section class="day">
    <h2 class="day-date">07.26 Sunday Q2: Complex Cellular Behaviors</h2>
    <ul class="talk-list">

      <li class="talk">
        <a href="#" class="talk-title">Mechanism-driven single-cell modelling</a>
        <span class="talk-speaker">Yuhao Chen</span>
      </li>

      <li class="talk">
        <a href="#" class="talk-title">Data-driven approaches</a>
        <span class="talk-speaker">Tailin Wu</span>
      </li>

      <li class="talk">
        <a href="#" class="talk-title">Multiscale modelling</a>
        <span class="talk-speaker">Zhennan Zhou</span>
      </li>

    </ul>
  </section>

  <!-- ===== 07.25 ===== -->
  <section class="day">
    <h2 class="day-date">07.25 Saturday Q1: Cellular Information Processing</h2>
    <ul class="talk-list">

      <li class="talk">
        <a href="#" class="talk-title">Control theory</a>
        <span class="talk-speaker">Fangzhou Xiao</span>
      </li>

      <li class="talk">
        <a href="#" class="talk-title">Protein computation</a>
        <span class="talk-speaker">Zibo Chen</span>
      </li>

      <li class="talk">
        <a href="#" class="talk-title">Probabilistic reasoning in cells</a>
        <span class="talk-speaker">Zitong (Jerry) Wang</span>
      </li>

      <li class="talk">
        <a href="#" class="talk-title">A scientific story that spreads like a virus</a>
        <span class="talk-speaker">Fangzhou Xiao</span>
      </li>

      <li class="talk">
        <a href="#" class="talk-title">From a story to a publishable paper: A deep dive in AI-native scientific research</a>
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
    margin-bottom: 3rem;
  }

  .day:last-of-type {
    margin-bottom: 0;
  }

  .day-date {
    font-size: 1.3rem;
    font-weight: 600;
    color: #374151;
    margin: 0 0 1.5rem 0;
    letter-spacing: 0.5px;
  }

  /* ===== Talk list ===== */
  .talk-list {
    list-style: none;
    padding: 0;
    margin: 0;
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

  .talk-title {
    font-size: 1.02rem;
    font-weight: 500;
    color: #1f2937;
    text-decoration: none;
    line-height: 1.5;
    transition: color 0.2s;
  }

  .talk-title:hover {
    color: #FF6C0C;
  }

  .talk-speaker {
    font-size: 0.88rem;
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
