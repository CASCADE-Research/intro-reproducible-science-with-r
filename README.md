# Reproducible Data Science

***Author:*** Nelson Roque, PhD

[nur375@psu.edu](mailto:nur375@psu.edu)

Director of the CASCADE Lab at The Pennsylvania State University

## Intention of this Web Course

To train the next-generation of scientists to work with data - regardless of the type.

## Background

A reproducibility crisis (Ioannidis, 2005; Open Science Collaboration, 2015) has emerged as a threat to the scientific
enterprise. Over the last decade I've engaged in learning opportunities to become proficient across topics including
data wrangling and modeling of text, image, video, and eye-tracking data, as well as more recently sensor data, and
look forward to training the next generation of scientists on code-based methods to apply in their research.
Ioannidis, John P A. 2005. “Why Most Published Research Findings Are False.” PLoS Medicine 2 (8): e124.
doi:10.1371/journal.pmed.0020124.
Open Science Collaboration. 2015. “Estimating the Reproducibility of Psychological Science.” Science 349 (6251):
aac4716–aac4716. doi:10.1126/science.aac4716.

For those that come next in line to have an easier start than those that came before.

## Workshop Objectives

- Describe various tools and techniques supportive of open and reproducible science.
- List and describe the FAIR Principles (https://www.go-fair.org/fair-principles)
- Develop a code-only pipeline to allow reproducibility of data prep and analyses.
- Develop a long-term learning plan for practicing reproducible science tools and techniques.

## Lesson Plan

- What is reproducible science? Why should you care?
    - Using Endnote for Reference Management
    - Using Github for code management and collaboration
- What is R? Markdown?
    - Intro to R Syntax, Packages
- Special topics in R
    - Data Wrangling
    - Data Visualization
    - Modeling
    - Text Mining
    - Keystroke data
- Special topics in Python
    - Image/Video data

## Build the site

The course is published with [Quarto](https://quarto.org/). Quarto renders the
source lessons directly to the `docs/` directory used by GitHub Pages.

```bash
quarto preview
```

Create a production build with:

```bash
quarto render
```

The production build includes the complete PDF book at
`docs/reproducible-data-science.pdf`. Pushes to `main` trigger the GitHub Actions
workflow in `.github/workflows/publish.yml`, which renders and deploys the
`docs/` artifact through GitHub Pages.

### First-time GitHub Pages setup

In the GitHub repository, open **Settings → Pages** and set **Build and
deployment → Source** to **GitHub Actions**. This one-time administrative step
must be completed before the deployment workflow can publish the site.
