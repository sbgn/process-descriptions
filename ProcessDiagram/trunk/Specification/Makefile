# =============================================================================
# $Id$
# Top-level Makefile for the SBGN Process Diagram specification.
#
# $HeadURL$
# =============================================================================

.PHONY: clean, dist_clean

MAIN   = sbgn_PD-level1

LATEX  = pdflatex
BIBTEX = bibtex
MKIDX = makeindex

all default: images examples
	$(MAKE) -C examples
	$(MAKE) -C images
	$(MAKE) -C le_images
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex
	$(MKIDX) $(MAIN)
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN).tex

clean:
	$(MAKE) -C images clean
	$(MAKE) -C examples clean
	-rm -f *.bbl
	-rm -f *.blg
	-rm -f *.out
	-rm -f *.dvi
	-rm -f *.toc
	-rm -f *.aux
	-rm -f *.log
	-rm -f *.tmp
	-rm -f *.prv
	-rm -f *.idx
	-rm -f sbgn_PD-level1.fdb_latexmk

dist_clean: clean
	-rm -f *.pdf
