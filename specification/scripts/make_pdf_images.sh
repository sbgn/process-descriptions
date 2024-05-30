#!/bin/bash
SRC_DIR=../src/images
BUILD_DIR=$SRC_DIR/build
rm -rf $BUILD_DIR
mkdir $BUILD_DIR
for input_file_path in "$SRC_DIR"/*.final.svg
do
    input_file_name="${input_file_path##*/}"
    output_file_name=${input_file_name/%final.svg/pdf}
    output_file_path=$BUILD_DIR/"$output_file_name"
    echo "Converting $input_file_path to $output_file_path"
    inkscape --export-filename=$output_file_path $input_file_path
    echo "Cropping $output_file_path"
    pdfcrop $output_file_path $output_file_path > /dev/null
done
