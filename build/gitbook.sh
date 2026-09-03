#!/bin/sh
set -ev

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# RENDER BOOK

## GITBOOK
cd ../
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"
