# Pebble Methods Studio

A collaborative platform for the Pebble team to share methods, workflows, and research insights.

## 🚀 Getting Started

### For Visitors

Visit the site at: `https://pebble.github.io`

### For Contributors

#### Adding New Content

**Methods Documentation** (`_methods/`):
- Create `.md` files with front matter
- Use `example-method.md` as a template
- Files will appear at `/methods/your-file-name/`

**Workflows** (`_workflows/`):
- Step-by-step guides for complex processes
- Same format as methods
- Files will appear at `/workflows/your-file-name/`

**Blog Posts** (`_posts/`):
- Name files with date: `YYYY-MM-DD-title.md`
- For announcements and updates
- Files will appear at `/YYYY/MM/DD/title/`

#### Template Format

```yaml
---
title: "Your Title"
date: YYYY-MM-DD
category: methods|workflows|announcement
tags: [tag1, tag2]
author: "Your Name"
---

# Content Here

Your markdown content...
```

## 🛠️ Local Development

1. Install Ruby and Bundler
2. Run: `bundle install`
3. Start server: `bundle exec jekyll serve`
4. Visit: `http://localhost:4000`

## 📦 Deployment

This repository is automatically deployed to GitHub Pages when you push to the main branch.

- Just push your changes to GitHub
- The site will update automatically in a few minutes
- Visit `https://pebble.github.io` to see changes

## 📁 Structure

```
pebble.github.io/
├── _config.yml         # Jekyll configuration
├── _methods/           # Methods documentation
├── _workflows/         # Workflow guides
├── _posts/            # Blog posts (name with YYYY-MM-DD-)
├── _layouts/          # Custom layouts
├── index.md           # Homepage
└── Gemfile            # Ruby dependencies
```

## 🤝 Contributing

1. Create a new markdown file in the appropriate directory
2. Follow the template format
3. Commit and push to GitHub
4. Changes go live automatically!

## 💡 Tips

- Use images: Put in `images/` folder and reference with standard markdown
- Code blocks: Use triple backticks with language identifier
- Math: Use LaTeX with `$$` for blocks or `$` for inline
- Links: Use standard markdown link syntax

Happy documenting! 📝
