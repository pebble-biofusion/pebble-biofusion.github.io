---
layout: home
title: Pebble Summer School Portal
---

# 🎓 Welcome to the Pebble Summer School Portal

This platform hosts teaching materials, project outputs, and research results from our annual summer school programs in computational biology and mathematical modeling.

## 🚀 Quick Navigation

### Browse by Year
<div class="nav-cards">
  <a href="{{ site.baseurl }}/years/2024/" class="nav-card">
    <div class="nav-icon">📅</div>
    <div class="nav-content">
      <h3>2024 Projects</h3>
      <p>Cell cycle modeling, biochemical networks, computational methods</p>
    </div>
  </a>
</div>

### Browse by Topic
<div class="nav-cards">
  <a href="{{ site.baseurl }}/topics/cell-biology/" class="nav-card">
    <div class="nav-icon">🧬</div>
    <div class="nav-content">
      <h3>Cell Biology</h3>
      <p>Cell cycle, regulatory networks, signaling pathways</p>
    </div>
  </a>

  <a href="{{ site.baseurl }}/topics/mathematical-modeling/" class="nav-card">
    <div class="nav-icon">🧮</div>
    <div class="nav-content">
      <h3>Mathematical Modeling</h3>
      <p>ODE models, simulations, parameter estimation</p>
    </div>
  </a>

  <a href="{{ site.baseurl }}/topics/biochemistry/" class="nav-card">
    <div class="nav-icon">🧪</div>
    <div class="nav-content">
      <h3>Biochemistry</h3>
      <p>Enzyme kinetics, metabolic pathways, reactions</p>
    </div>
  </a>

  <a href="{{ site.baseurl }}/topics/systems-biology/" class="nav-card">
    <div class="nav-icon">🧫</div>
    <div class="nav-content">
      <h3>Systems Biology</h3>
      <p>Network analysis, multi-scale modeling, circuits</p>
    </div>
  </a>
</div>

## 🎯 Featured Project

### [SpudCell Whole Cell Cycle ODE Analysis]({{ site.baseurl }}/summerschool/2024/spudcell-tutorials/)

<div class="featured-project">
  <div class="featured-content">
    <p>Comprehensive modeling of the complete cell cycle using coupled ODEs. This project includes interactive Jupyter notebooks, detailed presentations, and simulation data.</p>
    <div class="featured-meta">
      <span class="meta-tag">📅 2024</span>
      <span class="meta-tag">🧬 Cell Biology</span>
      <span class="meta-tag">💻 Jupyter Notebooks</span>
    </div>
  </div>
  <div class="featured-action">
    <a href="{{ site.baseurl }}/summerschool/2024/spudcell-tutorials/" class="btn-primary">Explore Project →</a>
  </div>
</div>

## 📊 What You'll Find

### Material Types
Each summer school project includes comprehensive materials:

<div class="material-types">
  <div class="material-item">
    <div class="material-icon">📊</div>
    <div class="material-info">
      <h4>Presentations</h4>
      <p>Keynote/PPT files with theoretical background and methodology</p>
    </div>
  </div>

  <div class="material-item">
    <div class="material-icon">💻</div>
    <div class="material-info">
      <h4>Jupyter Notebooks</h4>
      <p>Interactive code, analysis, and reproducible research</p>
    </div>
  </div>

  <div class="material-item">
    <div class="material-icon">📈</div>
    <div class="material-info">
      <h4>Research Posters</h4>
      <p>Conference-ready poster presentations and summaries</p>
    </div>
  </div>

  <div class="material-item">
    <div class="material-icon">📝</div>
    <div class="material-info">
      <h4>Manuscripts</h4>
      <p>Draft papers, technical reports, and documentation</p>
    </div>
  </div>
</div>

## 🎓 For Different Users

### For Students
- Access learning materials and tutorials
- Explore project examples and code
- Find resources for your own research

### For Instructors
- Share teaching materials with students
- Access reusable project templates
- Coordinate summer school programs

### For Researchers
- Explore computational approaches
- Access reproducible research examples
- Collaborate on future projects

## 📈 Impact & Statistics

<div class="stats-section">
  <div class="stat-box">
    <div class="stat-number">12+</div>
    <div class="stat-label">Research Projects</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">45+</div>
    <div class="stat-label">Jupyter Notebooks</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">30+</div>
    <div class="stat-label">Presentations</div>
  </div>
  <div class="stat-box">
    <div class="stat-number">100+</div>
    <div class="stat-label">Students & Researchers</div>
  </div>
</div>

## 🚀 Getting Started

1. **Browse Materials**: Explore projects by year or research topic
2. **Download Resources**: All materials are freely available on GitHub
3. **Reproduce Analysis**: Use Jupyter notebooks to follow the analysis
4. **Contribute**: Add your own projects using our templates

## 📞 Connect With Us

- **[About Us]({{ site.baseurl }}/about/)**: Learn more about the Pebble program
- **[Contribute]({{ site.baseurl }}/contribute/)**: How to add your own materials
- **[Contact]({{ site.baseurl }}/about/)**: Get in touch with our team

---

<style>
  .nav-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
  }

  .nav-card {
    display: flex;
    gap: 1rem;
    padding: 1.5rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 12px;
    text-decoration: none;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .nav-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
  }

  .nav-icon {
    font-size: 2rem;
  }

  .nav-content h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.25rem;
  }

  .nav-content p {
    margin: 0;
    opacity: 0.9;
    font-size: 0.9rem;
  }

  .featured-project {
    background: #f3f4f6;
    padding: 2rem;
    margin: 2rem 0;
    border-radius: 12px;
    border-left: 4px solid #6366f1;
  }

  .featured-content {
    margin-bottom: 1rem;
  }

  .featured-meta {
    display: flex;
    gap: 0.5rem;
    margin-top: 1rem;
    flex-wrap: wrap;
  }

  .meta-tag {
    background: white;
    padding: 0.3rem 0.7rem;
    border-radius: 15px;
    font-size: 0.85rem;
    color: #4b5563;
  }

  .btn-primary {
    display: inline-block;
    background: #6366f1;
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
  }

  .material-types {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
  }

  .material-item {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
  }

  .material-icon {
    font-size: 2rem;
  }

  .material-info h4 {
    margin: 0 0 0.5rem 0;
    color: #1f2937;
  }

  .material-info p {
    margin: 0;
    color: #6b7280;
    font-size: 0.9rem;
  }

  .stats-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
  }

  .stat-box {
    background: #f9fafb;
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
  }

  .stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    color: #6366f1;
    line-height: 1;
  }

  .stat-label {
    color: #6b7280;
    font-size: 0.9rem;
    margin-top: 0.5rem;
  }

  @media (max-width: 768px) {
    .nav-cards, .material-types, .stats-section {
      grid-template-columns: 1fr;
    }
  }
</style>
