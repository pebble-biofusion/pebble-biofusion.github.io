---
layout: page
title: "Ignition"
permalink: /summerschool/2026/ignition/
---

<div class="ignition">

  <!-- ===== 07.25 ===== -->
  <section class="day">
    <h2 class="day-date">07.25 Saturday Q1: Cellular Information Processing</h2>
    <ul class="talk-list">

      <li class="talk">
        <a href="#" class="talk-title">Cellular Information Processing, Control theory</a>
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
    color: #6b7280;
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
    justify-content: space-between;
    align-items: baseline;
    gap: 2rem;
    padding: 1rem 0;
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
    text-align: right;
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
