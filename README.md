# SSC JE Prep · Lokesh’s Study Desk

A free personal SSC JE Electrical preparation website. No paid notes, checkout or subscriptions.

**Live website:** https://je-notes-lokesh.lokesh254.chatgpt.site

The hosted personal site currently retains its owner-only access. This GitHub repository is public. Personal progress is stored only in each visitor’s browser and is never committed here.

## Included

- Syllabus-first dashboard with seven Electrical subject groups, plus Reasoning and General Awareness checklists.
- Countdown to **30 October 2026, 00:00 IST**, a personal preparation target, not an announced exam date.
- 26 Electrical chapters with 13,446 words of teaching notes, rendered equations and five diagrams.
- 63 original worked question models and 79 original multiple-choice practice questions.
- 44 selected, paraphrased PYQ concepts from six 2023/2024 paper reproductions, with paper, question and PDF-page references and independently worked answers.
- Completion tracking, chapter bookmarks, personal notes, mistake review and JSON progress import/export.
- Downloadable Markdown chapters, existing circuit PDFs and browser print-to-PDF layouts.
- **Weekly schedule deliberately pending:** Lokesh will supply a photo. No schedule has been invented.

## Coverage and editorial limits

Notes cover the seven Electrical groups. Full Reasoning/General Awareness notes are not included. The PYQ bank is a selected sample, not a complete archive or transcription. Some chapters have no indexed PYQ yet. Recurrence labels count related concepts in this collected sample, not all SSC exams or future weightage. “Chosen Option” on a candidate response sheet is not used as an answer key. Source links and coverage information are available inside the website.

The chapter notes and original questions were written for this project. Linked paper reproductions remain on their source host; external rights remain with their respective owners. Earlier circuit PDFs are retained supplementary study drafts with their own references. Legal installation requirements must be checked against applicable regulations; this is exam study material.

## Run and edit

This is a buildless static site. Serve `dist/` with any static HTTP server, for example `python -m http.server 8000 --directory dist`, then open the local address. Plain HTML, CSS and JavaScript require no runtime framework or secret keys.

- `dist/index.html`, `styles.css`, `app.js`: interface and interactions.
- `dist/state.js`: progress validation, countdown and scoring functions.
- `scripts/build_content.py`: editable notes, questions and source metadata; writes `dist/content.js`, `content.json`, chapter Markdown and notes ZIP.
- `scripts/create_diagrams.py`: original circuit and conceptual SVG figures.
- `scripts/package_source.py`: refreshes the downloadable website ZIP without Git/hosting metadata or personal state.
- `scripts/check-site.mjs`: content, local-link, state, route-render and numerical checks.

To regenerate content, install Python `matplotlib`, then run `python scripts/build_content.py`. Regenerate figures with `python scripts/create_diagrams.py`. Run checks with `node scripts/check-site.mjs`; refresh the source ZIP with `python scripts/package_source.py`.

The website works without an external JavaScript/CDN dependency. Fonts use Google Fonts with local system fallbacks. All formulas are pre-rendered SVGs with accessible text. Source PDFs require network access to the original hosts.

## Hosting

The current live site is hosted separately via Sites. The same `dist/` directory can be hosted by GitHub Pages or another static host. A GitHub Pages Actions workflow is included; enable Pages with **GitHub Actions** as the build source in repository settings to use it. The workflow being present does not by itself mean GitHub Pages is enabled or deployed.

## Verification

Automated checks cover content references, answer indices, mathematical worked results, local assets, safe backup filtering, scoring, countdown boundaries and source-bundle contents. Browser visual/interaction QA was unavailable in the build environment; responsiveness and printing have been implemented but not visually browser-verified.
