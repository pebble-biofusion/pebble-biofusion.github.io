---
layout: page
title: "Synthesis"
permalink: /workshop/2026/synthesis/
---

<div class="synthesis">

  <article class="paper-row">
    <div class="paper-info">
      <a href="#" class="paper-title">Emergent dynamics in synthetic gene circuits</a>
      <div class="paper-meta">Z. Chen, T. Wu, et al. · 2026 · Preprint</div>
    </div>
    <a href="#" class="paper-poster">
      <span class="poster-tag">Demo poster</span>
    </a>
  </article>

  <article class="paper-row">
    <div class="paper-info">
      <a href="#" class="paper-title">AI-guided design of protein switches</a>
      <div class="paper-meta">T. Wu, Z. Wang, et al. · 2026 · In preparation</div>
    </div>
    <a href="#" class="paper-poster">
      <span class="poster-tag">Demo poster</span>
    </a>
  </article>

  <article class="paper-row">
    <div class="paper-info">
      <a href="#" class="paper-title">Quantitative principles of microbial community assembly</a>
      <div class="paper-meta">B. He, Z. Li, et al. · 2026 · Preprint</div>
    </div>
    <a href="#" class="paper-poster">
      <span class="poster-tag">Demo poster</span>
    </a>
  </article>

  <article class="paper-row">
    <div class="paper-info">
      <a href="#" class="paper-title">Nonlinear dynamics of biological aging</a>
      <div class="paper-meta">Y. Yang, et al. · 2026 · Preprint</div>
    </div>
    <a href="#" class="paper-poster">
      <span class="poster-tag">Demo poster</span>
    </a>
  </article>

  <p class="syn-note">Demo content — replace with real manuscripts and posters.</p>

</div>

<style>
  .synthesis {
    width: 100%;
  }

  /* ===== Each paper = one row (info | poster) ===== */
  .paper-row {
    display: grid;
    grid-template-columns: 150px 1fr;
    gap: 2rem;
    align-items: center;
    padding: 1.75rem 0;
  }

  .paper-row:not(:last-child) {
    border-bottom: 1px solid #f3f4f6;
  }

  /* ===== Paper info (left) ===== */
  .paper-info {
    min-width: 0;
    order: 2;
  }

  .paper-title {
    display: block;
    font-size: 1.05rem;
    font-weight: 500;
    color: #1f2937;
    text-decoration: none;
    line-height: 1.5;
    margin-bottom: 0.35rem;
    transition: color 0.2s;
  }

  .paper-title:hover {
    color: #FF6C0C;
  }

  .paper-meta {
    font-size: 0.88rem;
    color: #9ca3af;
  }

  /* ===== Poster preview (right) ===== */
  .paper-poster {
    aspect-ratio: 3 / 4;
    order: 1;
    border: 1px solid #e5e7eb;
    border-radius: 6px;
    background: #fafafa;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    transition: border-color 0.2s, transform 0.2s;
  }

  .paper-poster:hover {
    border-color: #FF6C0C;
    transform: translateY(-2px);
  }

  .poster-tag {
    font-size: 0.78rem;
    color: #9ca3af;
    text-align: center;
    padding: 0 0.5rem;
  }

  .syn-note {
    font-size: 0.8rem;
    color: #d1d5db;
    font-style: italic;
    margin-top: 2rem;
    margin-bottom: 0;
  }

  /* ===== Responsive ===== */
  @media (max-width: 600px) {
    .paper-row {
      grid-template-columns: 1fr;
      gap: 1rem;
    }

    .paper-poster {
      max-width: 200px;
    }
  }
</style>
