---
layout: page
title: Summer School Projects
permalink: /workshop/
---

# Summer School Materials Portal

Welcome to the Pebble Summer School materials repository! This platform hosts teaching materials, project outputs, and research results from our annual summer school programs.

## 📁 Browse Materials

### By Year
{% assign years = "2025,2024,2023" | split: "," %}
{% for year in years %}
<div class="year-card">
  <h3>{{ year }} Summer School</h3>
  <p>Explore projects, presentations, and outputs from {{ year }}.</p>
  <a href="{{ site.baseurl }}/years/{{ year }}/" class="btn-year">View {{ year }} Projects</a>
</div>
{% endfor %}

### By Research Topic
<div class="topics-grid">
  <div class="topic-card">
    <h4>🧬 Cell Biology</h4>
    <p>Cell cycle modeling, regulatory networks, signaling pathways</p>
    <a href="{{ site.baseurl }}/topics/cell-biology/">Explore Cell Biology Projects</a>
  </div>

  <div class="topic-card">
    <h4>🧮 Mathematical Modeling</h4>
    <p>ODE models, stochastic simulations, parameter estimation</p>
    <a href="{{ site.baseurl }}/topics/mathematical-modeling/">Explore Modeling Projects</a>
  </div>

  <div class="topic-card">
    <h4>🧪 Biochemistry</h4>
    <p>Enzyme kinetics, metabolic pathways, reaction networks</p>
    <a href="{{ site.baseurl }}/topics/biochemistry/">Explore Biochemistry Projects</a>
  </div>

  <div class="topic-card">
    <h4>🧫 Systems Biology</h4>
    <p>Network analysis, multi-scale modeling, biological circuits</p>
    <a href="{{ site.baseurl }}/topics/systems-biology/">Explore Systems Biology Projects</a>
  </div>
</div>

## 📊 Project Statistics

<div class="stats-container">
  <div class="stat-card">
    <div class="stat-number">12+</div>
    <div class="stat-label">Research Projects</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">45+</div>
    <div class="stat-label">Jupyter Notebooks</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">30+</div>
    <div class="stat-label">Presentations</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">100+</div>
    <div class="stat-label">Students & Researchers</div>
  </div>
</div>

## 🎓 Featured Projects

### 🔬 Recent Highlights

<div class="featured-projects">
  <div class="featured-project">
    <h4>SpudCell Whole Cell Cycle ODE Analysis</h4>
    <p>Complete cell cycle modeling using coupled ODEs</p>
    <a href="{{ site.baseurl }}/workshop/2024/spudcell-tutorials/">View Project →</a>
  </div>

  <div class="featured-project">
    <h4>Computational Biochemistry Workshop</h4>
    <p>Hands-on computational approaches to biochemical problems</p>
    <a href="{{ site.baseurl }}/workshop/2024/biochemistry-workshop/">View Project →</a>
  </div>
</div>

## 📚 Material Types

Each project includes comprehensive materials:

- **📊 Presentations**: Keynote/PPT files with theoretical background
- **💻 Jupyter Notebooks**: Interactive code and analysis
- **📈 Research Posters**: Conference-ready poster presentations
- **📝 Manuscripts**: Draft papers and technical reports
- **🎬 Video Tutorials**: Supplementary learning materials

## 🚀 Getting Started

### For New Visitors
1. Browse projects by year or topic
2. Download materials directly from GitHub
3. Follow the analysis in Jupyter notebooks

### For Contributors
1. Use our [project template]({{ site.baseurl }}/workshop/templates/project-template/)
2. Organize materials in the standard directory structure
3. Submit your project via pull request

## 🔍 Search & Filter

Use the navigation above to explore:
- **By Year**: See evolution of research topics across years
- **By Topic**: Find all projects in your area of interest
- **By Material Type**: Access specific types of resources

---

*Questions or suggestions? Please reach out to the [Pebble team]({{ site.baseurl }}/about/)*

<style>
  .year-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    margin: 1rem 0;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .year-card h3 {
    margin: 0 0 0.5rem 0;
  }

  .year-card p {
    margin: 0.5rem 0 1rem 0;
    opacity: 0.9;
  }

  .btn-year {
    display: inline-block;
    background: white;
    color: #667eea;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
  }

  .topics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
  }

  .topic-card {
    background: white;
    border: 1px solid #e5e7eb;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  .topic-card h4 {
    margin: 0 0 0.5rem 0;
    color: #1f2937;
  }

  .topic-card p {
    color: #6b7280;
    margin: 0.5rem 0 1rem 0;
    font-size: 0.9rem;
  }

  .topic-card a {
    color: #6366f1;
    text-decoration: none;
    font-weight: 600;
  }

  .stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
  }

  .stat-card {
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

  .featured-projects {
    margin: 2rem 0;
  }

  .featured-project {
    background: #f3f4f6;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 12px;
    border-left: 4px solid #6366f1;
  }

  .featured-project h4 {
    margin: 0 0 0.5rem 0;
    color: #1f2937;
  }

  .featured-project p {
    color: #6b7280;
    margin: 0.5rem 0;
  }

  .featured-project a {
    color: #6366f1;
    text-decoration: none;
    font-weight: 600;
  }

  @media (max-width: 768px) {
    .topics-grid, .stats-container {
      grid-template-columns: 1fr;
    }
  }
</style>
