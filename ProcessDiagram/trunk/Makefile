# =============================================================================
# $Id$
# Top-level Makefile for the SBGN Process Diagram specification.
#
# $HeadURL$
# =============================================================================

.PHONY: clean, dist_clean, images

MAIN   = sbgn_PD-level1

LATEX  = pdflatex
BIBTEX = bibtex

all default: images
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN).tex

images:
	$(MAKE) -C images


clean:
	-rm *.aux
	$(MAKE) -C images clean


dist_clean: clean
	-rm *.pdf