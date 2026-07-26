---
layout: page
title: "Ignition"
permalink: /summerschool/2026/ignition/
---

<div class="ignition">

  <!-- ===== Day: 07.25 ===== -->
  <section class="day">
    <h2 class="day-date">07.25</h2>
    <ul class="talk-list">

      <li class="talk">
        <span class="talk-time">09:00</span>
        <div class="talk-body">
          <a href="#" class="talk-title">Opening remarks</a>
          <span class="talk-speaker">Chao Tang</span>
        </div>
      </li>

      <li class="talk">
        <span class="talk-time">09:30</span>
        <div class="talk-body">
          <a href="#" class="talk-title">Talk title — demo</a>
          <span class="talk-speaker">Qingyu Cheng</span>
        </div>
      </li>

      <li class="talk">
        <span class="talk-time">11:00</span>
        <div class="talk-body">
          <a href="#" class="talk-title">Talk title — demo</a>
          <span class="talk-speaker">Speaker name</span>
        </div>
      </li>

      <li class="talk">
        <span class="talk-time">14:00</span>
        <div class="talk-body">
          <a href="#" class="talk-title">Talk title — demo</a>
          <span class="talk-speaker">Speaker name</span>
        </div>
      </li>

    </ul>
  </section>

  <p class="ign-note">Demo content — replace with the real schedule and talk materials.</p>

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
    color: #FF6C0C;
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
    display: grid;
    grid-template-columns: 80px 1fr;
    gap: 1.5rem;
    align-items: baseline;
    padding: 1rem 0;
  }

  .talk:not(:last-child) {
    border-bottom: 1px solid #f3f4f6;
  }

  .talk-time {
    font-size: 0.9rem;
    color: #9ca3af;
    font-variant-numeric: tabular-nums;
  }

  .talk-body {
    min-width: 0;
  }

  .talk-title {
    display: inline;
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
    display: block;
    font-size: 0.88rem;
    color: #9ca3af;
    margin-top: 0.2rem;
  }

  .ign-note {
    font-size: 0.8rem;
    color: #d1d5db;
    font-style: italic;
    margin-top: 2rem;
    margin-bottom: 0;
  }

  /* ===== Responsive ===== */
  @media (max-width: 600px) {
    .talk {
      grid-template-columns: 60px 1fr;
      gap: 1rem;
    }
  }
</style>
