#!/bin/bash
#MUST be run in a python3 environment, MUST have $IMAGESCRIPT set to the path to the classify_image.py script.
#For more information on the script see https://www.tensorflow.org/tutorials/image_recognition
eval python $IMAGESCRIPT --image_file $1 | grep pizza |awk '{sum+=$(NF)} END {printf "%.5f\n", sum}'
