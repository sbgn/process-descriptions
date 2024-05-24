Primary sources for images are either:
    - a GraphML file, to be edited in SBGN-ED;
    - an SVG file, to be edited in Inkscape, in the case there is no corresponding GraphML file (except for the files `sbgn_node_taxonomy.final.svg` and `sbgn_edge_taxonomy.final.svg`, see below).

Final sources for images are always SVG files labeled "final".
These are the files that are converted to PDFs and cropped to the `../../build/images/` directory using the `../../scripts/make_pdf_images.sh` script (uses Inkscape and pdfcrop).
They are either:
    - direct exports from SBGN-ED when they have a corresponding GraphML file and no intermediate SVG version (see below);
    - direct exports from Inkscape when they have a GraphML and an intermediate version;
    - direct exports from the BOUML software for files `sbgn_node_taxonomy.final.svg` and `sbgn_edge_taxonomy.final.svg`.
When they have no corresponding GraphML file or are not exports from BOUML, they are themselves a source file, and should be edited in Inkscape.

Some SVG files are used as intermediate files between the GraphML source and the "final" SVG file.
They are exports from SBGN-ED, and contain invisible nodes that were removed in the "final" SVG file using Inkscape.
These intermediate files are never labeled "final".

Some files also have and SBGN-ML version.
These are not sources for the images and are not needed for compiling the specification.
