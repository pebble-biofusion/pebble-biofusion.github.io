---
layout: page
title: "Synthesis"
permalink: /summerschool/2026/synthesis/
---

<div class="synthesis">

  <!-- Left: Manuscripts -->
  <section class="syn-col">
    <h2 class="syn-heading">Manuscripts</h2>
    <ul class="paper-list">
      <li>
        <a href="#" class="paper-title">Emergent dynamics in synthetic gene circuits</a>
        <div class="paper-meta">Z. Chen, T. Wu, et al. · 2026 · Preprint</div>
      </li>
      <li>
        <a href="#" class="paper-title">AI-guided design of protein switches</a>
        <div class="paper-meta">T. Wu, Z. Wang, et al. · 2026 · In preparation</div>
      </li>
      <li>
        <a href="#" class="paper-title">Quantitative principles of microbial community assembly</a>
        <div class="paper-meta">B. He, Z. Li, et al. · 2026 · Preprint</div>
      </li>
      <li>
        <a href="#" class="paper-title">Nonlinear dynamics of biological aging</a>
        <div class="paper-meta">Y. Yang, et al. · 2026 · Preprint</div>
      </li>
    </ul>
    <p class="syn-note">Demo content — replace with real manuscripts.</p>
  </section>

  <!-- Right: Poster -->
  <section class="syn-col">
    <h2 class="syn-heading">Poster</h2>
    <div class="poster-frame">
      <div class="poster-placeholder">
        <div class="poster-icon">📄</div>
        <div class="poster-title">Demo Poster</div>
        <div class="poster-sub">Poster preview will appear here</div>
      </div>
    </div>
  </section>

</div>

<style>
  .synthesis {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: start;
  }

  .syn-heading {
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #6b7280;
    margin: 0 0 1.5rem 0;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid #f0f0f0;
  }

  /* ===== Manuscript list ===== */
  .paper-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .paper-list li {
    margin-bottom: 1.5rem;
  }

  .paper-list li:last-child {
    margin-bottom: 0;
  }

  .paper-title {
    display: block;
    font-size: 1.02rem;
    font-weight: 500;
    color: #1f2937;
    text-decoration: none;
    line-height: 1.5;
    margin-bottom: 0.3rem;
    transition: color 0.2s;
  }

  .paper-title:hover {
    color: #FF6C0C;
  }

  .paper-meta {
    font-size: 0.85rem;
    color: #9ca3af;
  }

  .syn-note {
    font-size: 0.8rem;
    color: #d1d5db;
    font-style: italic;
    margin-top: 2rem;
    margin-bottom: 0;
  }

  /* ===== Poster frame ===== */
  .poster-frame {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    background: #fafafa;
    aspect-ratio: 3 / 4;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    transition: border-color 0.2s;
  }

  .poster-frame:hover {
    border-color: #FF6C0C;
  }

  .poster-placeholder {
    text-align: center;
    color: #9ca3af;
  }

  .poster-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
  }

  .poster-title {
    font-size: 1.05rem;
    font-weight: 500;
    color: #6b7280;
    margin-bottom: 0.3rem;
  }

  .poster-sub {
    font-size: 0.85rem;
    color: #9ca3af;
  }

  /* ===== Responsive ===== */
  @media (max-width: 768px) {
    .synthesis {
      grid-template-columns: 1fr;
      gap: 2.5rem;
    }
  }
</style>
