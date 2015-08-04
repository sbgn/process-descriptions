If compiling the pdf from an environment like TeXnicCenter make sure to

* create PDFs from the SVG images using Inkscape
	
	call make in these folders
		/examples
		/images
		/le_images

* create the glossaries for the rules

	with Perl
		makeglossaries sbgn_PD-level1

	without Perl
		makeindex -s sbgn_PD-level1.ist -t sbgn_PD-level1.glg -o sbgn_PD-level1.gls sbgn_PD-level1.glo
