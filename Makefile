# =============================================================================
# $Id$
# Top-level Makefile for the SBGN Process Diagram specification.
#
# $HeadURL$
# =============================================================================

.PHONY: clean, dist_clean, images, examples

MAIN   = sbgn_PD-level1

LATEX  = pdflatex
BIBTEX = bibtex

all default: images examples
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN).tex

images:
	$(MAKE) -C images

examples:
	$(MAKE) -C images


clean:
	$(MAKE) -C images clean
	-rm -f *.bbl
	-rm -f *.blg
	-rm -f *.out
	-rm -f *.dvi
	-rm -f *.toc
	-rm -f *.aux
	-rm -f *.log
	-rm -f *.tmp
	-rm -f *.prv
	-rm -f sbgn_PD-level1.fdb_latexmk

dist_clean: clean
	-rm -f *.pdf
