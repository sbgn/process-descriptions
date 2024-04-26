#!/bin/bash
if [[ -d $1 ]]; then
    find $1 -maxdepth 1 -name "*.tex" -type f -print0 | xargs -0 -I % python remove_commands_from_file.py --in-place bak %
elif [[ -f $1 ]]; then
    python remove_commands_from_file.py --in-place bas $1
else
    echo "$1 is not valid"
    exit 1
fi
