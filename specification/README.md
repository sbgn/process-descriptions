# Editing and compiling the specification

The specification is generally edited and compiled online using Overeaf.
The Overleaf project can be found [here]().

It can also be edited and compiled locally using this repository, which is synchronized with Overleaf.

## Organization of the directory

* `src/`: contains all source files;
* `src/images/`: contains the source files for the images;
* `src/images/build/`: contains the PDF files used as sources for the images in the TeX files; built from the source SVG files in `src/images/` with extension `*.final.svg` using the script `scripts/make_pdf_images.sh`.
* `scripts/`: scripts to be run before compiling the specification. Currently only contains the `scripts/make_pdf_images.sh` script.
* `templates/`: templates for writing the description of glyphs.

## How to compile the specification

The specification is compiled automatically in Overleaf when editing the specification online.
> :warning: This automatic compilation does not build the source files for the images.
If the source files for the images have changed, these should be re-built locally using the instructions below.

The specification can also be compiled locally using `latexmk`, in a manner compatible with Overleaf.

### Prerequisites

Make sure you have the following software installed:
* `Inkscape` and `pdfcrop` for building the image source files;
* `pdflatex` and `latexmk` for compiling the specificationa (these are the tools used by Overleaf, and are usually already included in TeX distributions).

### Building the sources of the images

Before compiling the specification, one should make sure that all images have been built into PDF files, that are the source files for images included in the TeX sources of the specification.
To build the PDF files, just run the `scripts/make_pdf_images.sh` script from the `scripts/` directory, which converts all SVG source files with extension `*.final.svg` from the `src/images/` directory into PDF files into the `src/images/build/` directory using Inkscape, and crops them using pdfcrop.
More information on how to create images for the specification can be found [here](src/images/README.md).

### Compiling the specification

The main source file is `src/main.tex`.
It should be compiled using `latexmk` from the root directory of the specification or from the `src/` directory.
The configuration files for compiling with `latexmk` are `.latexmkrc` (compiling from root) and `src/.latexmkrc` (compiling from `src/`).
To compile the specification, just run:

```
    latexmk
```

The files resulting from the compilation, including the end PDF file, will appear in the `build/` directory.
