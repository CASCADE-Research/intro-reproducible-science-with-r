#!/bin/sh
set -ev

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# RENDER BOOK

## EPUB
cd ../
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::epub_book')"
