---
layout: page
title: "Gallery"
permalink: /workshop/2026/gallery/
---

<div class="gallery">

  <div class="gallery-intro">
    <h2>Workshop Gallery</h2>
    <p>Moments from the 2026 Pebble BioFusion Workshop</p>
  </div>

  <!-- ===== Gallery Grid ===== -->
  <div class="gallery-grid">
    
    <!-- Add your images here -->
    <!-- Example format:
    <div class="gallery-item">
      <a href="{{ site.baseurl }}/images/workshop2026/photo1.jpg" class="gallery-link" target="_blank">
        <img src="{{ site.baseurl }}/images/workshop2026/photo1.jpg" alt="Workshop photo 1">
      </a>
      <div class="gallery-caption">Photo description</div>
    </div>
    -->

  </div>

</div>

<style>
  .gallery {
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem 0;
  }

  /* ===== Introduction ===== */
  .gallery-intro {
    text-align: center;
    margin-bottom: 3rem;
    padding: 0 1rem;
  }

  .gallery-intro h2 {
    font-size: 2rem;
    font-weight: 700;
    color: #1f2937;
    margin-bottom: 0.5rem;
  }

  .gallery-intro p {
    font-size: 1.1rem;
    color: #6b7280;
  }

  /* ===== Gallery Grid ===== */
  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    padding: 0 1rem;
  }

  /* ===== Gallery Item ===== */
  .gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
    background: #f9fafb;
    aspect-ratio: 4/3;
  }

  .gallery-link {
    display: block;
    width: 100%;
    height: 100%;
    text-decoration: none;
    position: relative;
  }

  .gallery-link img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }

  .gallery-link:hover img {
    transform: scale(1.05);
  }

  /* ===== Caption ===== */
  .gallery-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
    color: white;
    padding: 1rem 0.75rem 0.75rem;
    font-size: 0.9rem;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .gallery-item:hover .gallery-caption {
    opacity: 1;
  }

  /* ===== Responsive ===== */
  @media (max-width: 768px) {
    .gallery-grid {
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 1rem;
    }

    .gallery-intro h2 {
      font-size: 1.5rem;
    }
  }

  @media (max-width: 480px) {
    .gallery-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<script>
  // Optional: Lightbox functionality for image viewing
  document.querySelectorAll('.gallery-link').forEach(function(link) {
    link.addEventListener('click', function(e) {
      // You can add lightbox functionality here if needed
      console.log('Image clicked:', this.href);
    });
  });
</script>
