# CS542_project_Letter_Recognition

## Dataset

Download dataset from https://www.kaggle.com/sachinpatel21/az-handwritten-alphabets-in-csv-format, and put it at [GoogleDrive](https://drive.google.com/drive/folders/0AK8Vo4lZwwOiUk9PVA)
Using 'csv-to-images.py' to transform the 'A_Z Handwritten Data.csv' to images.  

## Segmentation
run `Segment.py` to do the letter segmentation of the picture in the directory of `orginal`  
The output will be image files which are labled in `count_number.png` under the main directory.  
## Training
Run CNN.py to train, test and generate model named 'model.h5'. The trained model is at [GoogleDrive](https://drive.google.com/drive/folders/0AK8Vo4lZwwOiUk9PVA).[sdadsas](https://drive.google.com/open?id=1nFKdv9tI82gwUnerl-ZYVEJgV2ncfM7O)

## Predicting
Download trained model "model.h5" from [GoogleDrive](https://drive.google.com/drive/folders/0AK8Vo4lZwwOiUk9PVA). Run `Segment.py` to do the letter segmentation of the picture in the directory `orginal`, and then run predict.py to get the result for every file ends with '.png' under project directory, using trained model "model.h5".

## Result Example

![result](https://github.com/ZhengyangTang/CS542_project_Letter_Recognition/blob/master/result.JPG) 
