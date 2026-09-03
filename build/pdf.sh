#!/bin/sh
set -ev

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# RENDER BOOK

## PDF
cd ../
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::pdf_book')"
