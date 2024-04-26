#!/bin/bash
if [[ -d $1 ]]; then
    find $1 -maxdepth 1 -name "*.tex" -type f -print0 | xargs -0 -I file pdfcrop file file
elif [[ -f $1 ]]; then
    pdfcrop $1 $1
else
    echo "$1 is not valid"
    exit 1
fi
