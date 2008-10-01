# =============================================================================
# $Id: Makefile 390 2008-09-23 10:10:00Z lenov $
# Top-level Makefile for the SBGN Process Diagram specification.
#
# $HeadURL: https://sbgn.svn.sourceforge.net/svnroot/sbgn/trunk/documents/specifications/ProcessDiagram/Level1/Makefile $
# =============================================================================

MAIN   = sbgn_PD-level1_1

LATEX  = pdflatex
BIBTEX = bibtex

all default:
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN).tex
