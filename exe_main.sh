#!/bin/bash

cd /home/hvianna/Desktop/ANBIMA_extract
chmod a+x main.py
./main.py > READ_METADATA.txt
line="$(sed -ne 5p READ_METADATA.txt)"
mv /home/hvianna/Desktop/ANBIMA_extract/READ_METADATA.txt "$line"
