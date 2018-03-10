#!/bin/bash
#Depends on classify_image.py.
python3 classify_image.py --image_file $1 --model_dir ./model | grep pizza |awk '{sum+=$(NF)} END {printf "%.5f\n", sum}'
