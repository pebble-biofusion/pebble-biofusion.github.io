---
layout: page
title: "How to Contribute"
permalink: /contribute/
---

# How to Contribute

This platform hosts teaching materials and research outputs from the Pebble Biofusion Summer School. Here's how to add your content.

## Adding New Projects

### Project Structure
```
summerschool/2026/your-project-name/
├── presentations/      # Keynote/PPT files
├── notebooks/         # Jupyter notebooks
├── posters/          # PDF poster files
├── manuscripts/      # Research papers and reports
└── README.md         # Project description
```

### Project Template
Use the project template: `summerschool/templates/project-template.md`

## Content Guidelines

### Required Files
- `README.md` - Project description with metadata
- At least one analysis/presentation file

### Recommended Structure
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
year: 2026
topic: "research-topic"
authors: ["Full Name", "Co-author Name"]
status: "completed"  # or "ongoing", "planned"
tags: [relevant, tags, here]
project_image: "optional-preview.png"
date: 2026-07-25
---
```

## Submission Process

1. **Create Project Directory** following the structure above
2. **Add Your Materials** to appropriate folders
3. **Update Project Metadata** in README.md
4. **Test Locally** using `bundle exec jekyll serve`
5. **Submit Changes** via pull request or direct push

## Quality Standards

### Clear Descriptions
- Explain research context and methods
- Provide reproducible code with requirements.txt
- Include all referenced files
- Credit all contributors appropriately

### File Organization
- Use descriptive filenames
- Organize materials in standard directories
- Include README with project overview
- Follow consistent naming conventions

## Technical Requirements

### Software Dependencies
Include a `requirements.txt` file:
```
numpy>=1.20.0
pandas>=1.3.0
matplotlib>=3.4.0
jupyter>=1.0.0
```

### Code Documentation
- Comment complex code sections
- Include usage instructions
- Provide example outputs
- Document dependencies

## Review Process

Content is reviewed for:
- Scientific accuracy
- Code reproducibility
- Documentation completeness
- File organization standards

## Questions?

Contact the summer school organizing committee for guidance on contributing materials.

---

*For more information, see the [Program Overview](/summer-camp/)*
