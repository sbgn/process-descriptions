.PHONY: clean

SVG_FILES := $(wildcard *.svg)

PDF_FILES := $(patsubst %.svg,%.pdf, $(SVG_FILES))

%.pdf : %.svg
	inkscape -D -z --file=$< --export-pdf=$@

all: $(PDF_FILES)
#	echo $(PDF_FILES)





clean:
	-rm -f *.pdf


