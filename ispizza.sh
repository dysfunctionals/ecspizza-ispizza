#!/bin/bash
#Depends on classify_image.py.
python classify_image.py --image_file $1 | grep pizza |awk '{sum+=$(NF)} END {printf "%.5f\n", sum}'
