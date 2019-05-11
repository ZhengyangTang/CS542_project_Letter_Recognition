# CS542_project_Letter_Recognition

## Dataset

Download dataset from https://www.kaggle.com/sachinpatel21/az-handwritten-alphabets-in-csv-format, and put it under project directory.
Using 'csv-to-images.py' to transform the 'A_Z Handwritten Data.csv' to images  

## Segmentation
run 'Segment.py' to do the letter segmentation of the picture in the directory of 'orginal'  
The output will be image files which are labled in 'count_number.png' under the main directory.  
## Training
Run CNN.py to train, test and generate model named 'model.h5'. (Trained model is too large to upload)

## Predicting
Run predict.py to get the result for every file ends with '.png' under project directory.
