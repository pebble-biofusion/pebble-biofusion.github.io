---
layout: page
title: Contribute
permalink: /contribute/
---

# How to Contribute

Adding content to Pebble Methods Studio is easy! Here's how:

## Quick Start

1. **Clone the repository** (or just edit directly on GitHub)
2. **Create a new markdown file** in the appropriate directory
3. **Follow the template format** (see examples below)
4. **Push to GitHub** - the site updates automatically!

## File Locations

### Methods Documentation
- **Directory**: `_methods/`
- **URL Pattern**: `/methods/your-file-name/`
- **Example**: `_methods/cell-culture.md` → `/methods/cell-culture/`

### Workflows
- **Directory**: `_workflows/`
- **URL Pattern**: `/workflows/your-file-name/`
- **Example**: `_workflows/data-analysis.md` → `/workflows/data-analysis/`

### Blog Posts
- **Directory**: `_posts/`
- **File Format**: `YYYY-MM-DD-title.md`
- **URL Pattern**: `/YYYY/MM/DD/title/`
- **Example**: `_posts/2026-07-25-new-method.md` → `/2026/07/25/new-method/`

## Template Format

### For Methods & Workflows:

```yaml
---
title: "Your Title Here"
date: 2026-07-25
category: methods  # or "workflows"
tags: [tag1, tag2, tag3]
author: "Your Name"
---

# Title

Brief description...

## Overview

What this method/workflow does...

## Steps

1. First step
2. Second step
3. Continue as needed

## Results

Expected outcomes...

## Notes

Any additional information...
```

### For Blog Posts:

```yaml
---
layout: post
title: "Post Title"
date: 2026-07-25
category: announcement
tags: [news, update]
author: "Your Name"
---

# Post Title

Your content here...
```

## Best Practices

### Content Quality
- **Be Clear**: Write in clear, simple language
- **Be Specific**: Include exact details and parameters
- **Be Complete**: Cover all steps and considerations
- **Be Current**: Update documents when things change

### Formatting
- Use headings (`#`, `##`) to organize content
- Use code blocks for commands and scripts
- Include images when helpful (place in `images/` directory)
- Use bullet points for lists

### Code Blocks
```
    ```bash
    # For shell commands
    pip install package-name
    ```

    ```python
    # For Python code
    import pandas as pd
    ```

    ```R
    # For R code
    library(tidyverse)
    ```
```

### Images
```markdown
![Description](images/your-image.png)
```

## Review Process

Currently, we use a direct push model:
1. Make your changes
2. Push to the main branch
3. Site updates automatically
4. Team can review and suggest improvements

## Need Help?

- Check existing methods/workflows for examples
- Ask a team member for guidance
- Start simple and expand over time

---

*Happy contributing! 🎉*
