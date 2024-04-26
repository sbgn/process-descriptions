# =============================================================================
# $Id$
# Top-level Makefile for the SBGN Process Diagram specification.
#
# $HeadURL$
# =============================================================================

MAIN   = sbgn_PD-level1

LATEX  = pdflatex
BIBTEX = bibtex

all default:
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN).tex
