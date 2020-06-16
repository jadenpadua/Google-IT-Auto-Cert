#!/bin/bash
> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for i in $files; do
    if test -e ~/$i; then
        echo "$HOME$i" >> oldFiles.txt;
    
    else
        echo "File does not exist"; fi
done
