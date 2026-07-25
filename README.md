# 🎓 Pebble Summer School Portal

A comprehensive platform for hosting teaching materials, project outputs, and research results from annual summer school programs in computational biology and mathematical modeling.

## 🌟 Website

**Visit the live site**: [https://pebble-biofusion.github.io/](https://pebble-biofusion.github.io/)

## 🎯 Purpose

This portal serves as a central repository for:
- **Teaching Materials**: Lecture slides, tutorials, and educational resources
- **Project Outputs**: Jupyter notebooks, presentations, and analysis code
- **Research Results**: Manuscripts, posters, and conference materials
- **Collaborative Work**: Multi-year, multi-institutional summer school projects

## 📁 Project Organization

### By Year Structure
```
summerschool/
├── 2024/
│   ├── spudcell-tutorials/
│   │   ├── presentations/     # Keynote/PPT files
│   │   ├── notebooks/        # Jupyter notebooks
│   │   ├── posters/          # PDF poster files
│   │   ├── manuscripts/      # Draft papers
│   │   └── README.md         # Project description
│   └── project-2/
└── 2025/
    └── upcoming-projects/
```

### By Topic Navigation
- **Cell Biology**: Cell cycle modeling, regulatory networks
- **Mathematical Modeling**: ODE models, simulations
- **Biochemistry**: Enzyme kinetics, metabolic pathways
- **Systems Biology**: Network analysis, multi-scale modeling

## 🚀 Getting Started

### For Visitors

1. **Browse Materials**: Navigate by year or research topic
2. **Download Resources**: All files are available on GitHub
3. **Reproduce Analysis**: Use Jupyter notebooks interactively

### For Contributors

#### Adding New Projects

1. **Create Project Directory**
   ```bash
   mkdir -p summerschool/2025/your-project-name/{presentations,notebooks,posters,manuscripts}
   ```

2. **Use Project Template**
   - Copy: `summerschool/templates/project-template.md`
   - Rename to: `summerschool/2025/your-project-name/README.md`

3. **Add Your Materials**
   ```bash
   # Add presentations
   cp your-presentation.pptx summerschool/2025/your-project-name/presentations/

   # Add notebooks
   cp your-analysis.ipynb summerschool/2025/your-project-name/notebooks/

   # Add other materials to appropriate directories
   ```

4. **Update Project Metadata**
   Edit the front matter in `README.md`:
   ```yaml
   ---
   layout: project
   title: "Your Project Title"
   year: 2025
   topic: "your-topic"
   authors: ["Author Name", "Co-author"]
   status: "completed"
   tags: [tag1, tag2, tag3]
   project_image: "preview-image.png"
   date: 2025-07-25
   ---
   ```

## 🛠️ Local Development

### Setting Up Jekyll

1. **Install Dependencies**
   ```bash
   cd /path/to/pebble-biofusion.github.io
   bundle install
   ```

2. **Start Local Server**
   ```bash
   bundle exec jekyll serve
   ```

3. **Access Site**
   - Open: `http://localhost:4000`
   - Changes auto-refresh

### Testing Changes

- Edit files and refresh browser to see changes
- Check console for Jekyll errors
- Test navigation and links

## 📦 Deployment

### Automatic Deployment

The site automatically deploys to GitHub Pages when you push to the main branch:

```bash
git add .
git commit -m "Add new summer school project"
git push origin main
```

### Manual Build Verification

Check deployment status: [GitHub Actions](https://github.com/pebble-biofusion/pebble-biofusion.github.io/actions)

## 📊 Content Guidelines

### File Organization Standards

Each project should include:

**Required Files:**
- `README.md` - Project description with metadata
- At least one analysis/presentation file

**Recommended Structure:**
- `presentations/` - `.pptx`, `.key`, `.pdf`
- `notebooks/` - `.ipynb`, `.py`, `.R`
- `posters/` - `.pdf`, `.png`
- `manuscripts/` - `.pdf`, `.docx`, `.tex`
- `data/` - `.csv`, `.xlsx`, `.json`

### Metadata Requirements

Every project `README.md` must include:

```yaml
---
layout: project
title: "Descriptive project title"
year: 2025
topic: "research-topic"
authors: ["Full Name", "Co-author Name"]
status: "completed"  # or "ongoing", "planned"
tags: [relevant, tags, here]
project_image: "optional-preview.png"
date: 2025-07-25
---
```

### Quality Standards

- **Clear Descriptions**: Explain research context and methods
- **Reproducible Code**: Include requirements.txt or environment.yml
- **Complete Materials**: All referenced files should be present
- **Proper Attribution**: Credit all contributors appropriately

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

1. **Fork the Repository**
2. **Create Project Branch**: `git checkout -b feature/new-project`
3. **Add Your Materials**: Follow directory structure
4. **Test Locally**: `bundle exec jekyll serve`
5. **Submit Pull Request**: Describe your project

## 📈 Project Statistics

- **12+** Research Projects
- **45+** Jupyter Notebooks
- **30+** Presentations
- **100+** Students & Researchers
- **4** Research Topics

## 🔍 Navigation Guide

### Browse by Year
- [2024 Projects](/years/2024/) - Cell cycle modeling, biochemical networks
- [2025 Projects](/years/2025/) - Coming soon!

### Browse by Topic
- [Cell Biology](/topics/cell-biology/) - Cell cycle, regulatory networks
- [Mathematical Modeling](/topics/mathematical-modeling/) - ODE models, simulations
- [Biochemistry](/topics/biochemistry/) - Enzyme kinetics, metabolism
- [Systems Biology](/topics/systems-biology/) - Network analysis

## 📞 Support & Contact

### Questions About Materials
- Check project README files for specific information
- Review the [Contribution Guide](/contribute/)
- Contact the project team

### Technical Issues
- Check [GitHub Issues](https://github.com/pebble-biofusion/pebble-biofusion.github.io/issues)
- Review Jekyll error logs
- Verify file paths and permissions

## 🔮 Future Enhancements

Planned improvements:
- [ ] Advanced search functionality
- [ ] Interactive code viewers
- [ ] Video tutorial integration
- [ ] Multi-language support
- [ ] Citation export features

---

**Built with ❤️ for the computational biology community**

*Last updated: July 2025*
