# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based GitHub Pages site serving as a personal homepage for FaNzu. It contains CTF writeups and game development blogs.

## Technology Stack

- **Static Site Generator**: Jekyll with `jekyll-theme-minimal`
- **Hosting**: GitHub Pages (deployed automatically on push to main)
- **Plugin**: `jekyll-relative-links` for linking between markdown files

## Local Development

GitHub Pages builds the site automatically. For local preview:

```bash
# Install dependencies (requires Ruby)
gem install bundler jekyll
bundle install

# Run local server
bundle exec jekyll serve
```

## Content Structure

- `README.md` - Homepage content
- `_config.yml` - Jekyll configuration
- `DUC_CTF_2025/` - CTF writeups for DUC CTF 2025
- `L3AK_CTF_2025/` - CTF writeups for L3AK CTF 2025
- `The_Wolf_where_the_land_ends/` - Game development blog

## Adding Content

All content is written in Markdown. New CTF writeups should go in their respective CTF folder. Use relative links between markdown files (the `jekyll-relative-links` plugin handles conversion to HTML links).
