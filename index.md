---
layout: home
title: Pebble Methods Studio
---

# Welcome to Pebble Methods Studio

This is the collaborative space for the Pebble team to share methods, workflows, and research insights.

## Recent Updates

{% for post in site.posts limit: 5 %}
- **[{{ post.title }}]({{ post.url }})** - {{ post.date | date: "%B %d, %Y" }}
  {{ post.excerpt | strip_html | truncatewords: 30 }}
{% endfor %}

## Categories

- [All Posts]({{ site.baseurl }}/posts/)
- [Methods]({{ site.baseurl }}/category/methods/)
- [Workflows]({{ site.baseurl }}/category/workflows/)
- [Resources]({{ site.baseurl }}/category/resources/)

## Quick Links

- [About Us]({{ site.baseurl }}/about/)
- [Contribution Guide]({{ site.baseurl }}/contribute/)
