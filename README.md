# 🎓 Pebble Biofusion Summer School Platform

A comprehensive platform for hosting teaching materials, project outputs, and research results from the annual Pebble Biofusion Summer School programs at Westlake University Interdisciplinary Sciences Center.

## 🌟 Website

**Visit the live site**: [https://pebble-biofusion.github.io/](https://pebble-biofusion.github.io/)

## 🎯 Purpose

This platform serves as a central repository for:
- **Teaching Materials**: Lecture slides, tutorials, and educational resources
- **Project Outputs**: Jupyter notebooks, presentations, and analysis code
- **Research Results**: Manuscripts, posters, and conference materials
- **Collaborative Work**: Multi-year, multi-institutional summer school projects

## 📁 Project Organization

### By Year Structure
```
workshop/
├── 2026/
│   ├── your-project-name/
│   │   ├── presentations/     # Keynote/PPT files
│   │   ├── notebooks/        # Jupyter notebooks
│   │   ├── posters/          # PDF poster files
│   │   ├── manuscripts/      # Draft papers
│   │   └── README.md         # Project description
```

### By Research Topics
- **Complex Systems**: Statistical physics, network dynamics, self-organization
- **Synthetic Biology**: Genetic circuits, protein design, microbial engineering
- **AI for Science**: Machine learning, data science, computational simulation
- **Biophysics**: Single-cell technologies, protein homeostasis

## 🚀 Getting Started

### For Visitors

1. Browse materials by year or research topic
2. Download resources directly from GitHub
3. Reproduce analysis using Jupyter notebooks

### For Contributors

#### Adding New Projects

1. Create project directory structure:
   ```bash
   mkdir -p workshop/2026/your-project/{presentations,notebooks,posters,manuscripts}
   ```

2. Use project template:
   Copy `workshop/templates/project-template.md`

3. Add materials with proper metadata:
   ```yaml
   ---
   layout: project
   title: "Your Project Title"
   year: 2026
   topic: "research-topic"
   authors: ["Author Name"]
   status: "completed"
   tags: [tag1, tag2]
   ---
   ```

## 🛠️ Local Development

### Setting Up Jekyll

1. Install dependencies:
   ```bash
   cd /path/to/pebble-biofusion.github.io
   bundle install
   ```

2. Start local server:
   ```bash
   bundle exec jekyll serve
   ```

3. Access site: `http://localhost:4000`

## 📦 Deployment

The site automatically deploys to GitHub Pages when you push to the main branch:

```bash
git add .
git commit -m "Add new summer school project"
git push origin main
```

## 📊 Content Guidelines

### File Organization Standards

Each project should include:

**Required Files:**
- `README.md` with metadata
- At least one analysis/presentation file

**Recommended Structure:**
- `presentations/` - `.pptx`, `.key`, `.pdf`
- `notebooks/` - `.ipynb`, `.py`, `.R`
- `posters/` - `.pdf`, `.png`
- `manuscripts/` - `.pdf`, `.docx`, `.tex`

### Metadata Requirements

Every project must include:
```yaml
---
layout: project
title: "Project title"
year: 2026
topic: "research-area"
authors: ["Name1", "Name2"]
status: "completed"
tags: [tag1, tag2]
date: 2026-07-25
---
```

## 🎓 Program Overview

### 2026 Summer School
- **Application Deadline**: June 15, 2026
- **Duration**: 6-8 weeks
- **Research Areas**: 8 interdisciplinary directions
- **Faculty**: 15+ world-class mentors
- **Institutions**: Westlake University + partner institutions

### Research Focus
- Complex systems and statistical physics
- Synthetic biology and genetic circuits
- AI for science applications
- Microbiome engineering
- Single-cell technologies
- Protein homeostasis
- Biological aging dynamics
- Developmental biology

## 🎓 Educational Use

### For Students
- Access learning materials and tutorials
- Explore code examples and analysis methods
- Use templates for your own projects

### For Instructors
- Share teaching materials with students
- Access reusable project templates
- Coordinate multi-year programs

### For Researchers
- Explore computational approaches
- Access reproducible research examples
- Build upon existing methodologies

## 🏗️ Technical Stack

- **Jekyll**: Static site generator
- **GitHub Pages**: Web hosting
- **Markdown**: Content authoring
- **Jupyter**: Interactive notebooks
- **Python/R**: Scientific computing

## 🤝 Contribution Workflow

1. Fork the repository
2. Create project branch
3. Add materials following directory structure
4. Test locally
5. Submit pull request

## 📈 Platform Statistics

- **15+** Faculty Members
- **8** Research Directions
- **6-8** Week Program Duration
- **100%** Interdisciplinary Focus

## 🔍 Navigation Guide

### Browse by Year
- [2026 Projects](/years/2026/) - Current summer school projects

### Browse by Research Topic
- [Complex Systems](/topics/complex-systems/) - Statistical physics, networks
- [Synthetic Biology](/topics/synthetic-biology/) - Genetic circuits, design
- [AI for Science](/topics/ai-for-science/) - Machine learning, simulation
- [Biophysics](/topics/biophysics/) - Single-cell, protein systems

## 📞 Support

### Questions About Materials
- Check project README files
- Review contribution guidelines
- Contact project team

### Technical Issues
- Check GitHub Issues
- Review Jekyll error logs
- Verify file paths and permissions

## 🔮 Future Enhancements

- Advanced search functionality
- Interactive code viewers
- Multi-language support
- Citation export features

---

**Built with ❤️ for the computational biology community**

*Last updated: July 2026*
