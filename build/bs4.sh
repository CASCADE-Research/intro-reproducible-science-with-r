#!/bin/sh
set -ev

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# RENDER BOOK

## BOOTSTRAP4 STYLE
cd ../
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::bs4_book')"
rm -rf docs
mkdir docs
cp -r _book/* docs
