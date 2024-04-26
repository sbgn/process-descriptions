Primary sources for images are either:
    - a GraphML file, to be edited in SBGN-ED;
    - an SVG file, to be edited in Inkscape, in the case there is no corresponding GraphML file.

Final sources for images are always SVG files labeled "final".
These are the files that are converted to PDFs in the `../build` directory.
They are direct exports from SBGN-ED when they have a corresponding GraphML file and no intermediate version (see below), and from Inkscape when they have a GraphML and an intermediate version.
When they have no corresponding GraphML file, they are themselves a source file, and should be edited in Inkscape.

Some SVG files are used as intermediate files between the GraphML source and the "final" SVG file.
They are exports from SBGN-ED, and contain invisible nodes that were removed in the "final" SVG file using Inkscape.
These intermediate files are never labeled "final".

Some files also have and SBGN-ML version.
These are not sources for the images and are not needed for compiling the specification.
