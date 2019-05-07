from keras.models import load_model
import matplotlib.image as mpimg
import os
#import cv2
model = load_model('./model.h5')

count = 0
images = []

for item in os.listdir('./'):

    if item.endswith('1.png') or item.endswith('h.png'):
        image = mpimg.imread('./' + item)
        image = image.reshape(1,28,28,1).astype('float32')
        predict = model.predict(image)
        if predict[0][0]==1.0:
            images.append('A')
        if predict[0][1]==1.0:
            images.append('B')
        if predict[0][2]==1.0:
            images.append('C')
        if predict[0][3]==1.0:
            images.append('D')
        if predict[0][4]==1.0:
            images.append('E')
        if predict[0][5]==1.0:
            images.append('F')
        if predict[0][6]==1.0:
            images.append('G')
        if predict[0][7]==1.0:
            images.append('H')
        if predict[0][8]==1.0:
            images.append('I')
        if predict[0][9]==1.0:
            images.append('J')
        if predict[0][10]==1.0:
            images.append('K')
        if predict[0][11]==1.0:
            images.append('L')
        if predict[0][12]==1.0:
            images.append('M')
        if predict[0][13]==1.0:
            images.append('N')
        if predict[0][14]==1.0:
            images.append('O')
        if predict[0][15]==1.0:
            images.append('P')
        if predict[0][16]==1.0:
            images.append('Q')
        if predict[0][17]==1.0:
            images.append('R')
        if predict[0][18]==1.0:
            images.append('S')
        if predict[0][19]==1.0:
            images.append('T')
        if predict[0][20]==1.0:
            images.append('U')
        if predict[0][21]==1.0:
            images.append('V')
        if predict[0][22]==1.0:
            images.append('W')
        if predict[0][23]==1.0:
            images.append('X')
        if predict[0][24]==1.0:
            images.append('Y')
        if predict[0][25]==1.0:
            images.append('Z')


print(images)
