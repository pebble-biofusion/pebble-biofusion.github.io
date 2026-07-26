---
layout: page
title: "How to Contribute"
permalink: /contribute/
---

## Adding Content

This platform hosts teaching materials and research outputs from the Pebble Biofusion Summer School.

## Project Structure

```
workshop/2026/your-project-name/
├── presentations/      # Keynote/PPT files
├── notebooks/         # Jupyter notebooks
├── posters/          # PDF poster files
├── manuscripts/      # Research papers
└── README.md         # Project description
```

## Project Template

Use: `workshop/templates/project-template.md`

## Required Files

- `README.md` with metadata
- At least one analysis/presentation file

## Recommended Structure

- `presentations/` - `.pptx`, `.key`, `.pdf`
- `notebooks/` - `.ipynb`, `.py`, `.R`
- `posters/` - `.pdf`, `.png`
- `manuscripts/` - `.pdf`, `.docx`, `.tex`
- `data/` - `.csv`, `.xlsx`, `.json`

## Metadata Format

Every project `README.md` must include:

```yaml
---
layout: project
title: "Project Title"
year: 2026
topic: "research-topic"
authors: ["Full Name", "Co-author"]
status: "completed"
tags: [tag1, tag2]
date: 2026-07-25
---
```

## Submission Process

1. Create project directory structure
2. Add materials to appropriate folders
3. Update project metadata in README.md
4. Test locally: `bundle exec jekyll serve`
5. Submit via pull request or direct push

## Quality Standards

- Clear research context and methods
- Reproducible code with requirements.txt
- Include all referenced files
- Credit all contributors appropriately
- Use descriptive filenames
- Follow consistent naming conventions

## Software Dependencies

Include `requirements.txt`:
```
numpy>=1.20.0
pandas>=1.3.0
matplotlib>=3.4.0
jupyter>=1.0.0
```

## Local Development

```bash
cd /path/to/pebble-biofusion.github.io
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000
```

## Contact

For guidance on contributing materials, contact the summer school organizing committee.
