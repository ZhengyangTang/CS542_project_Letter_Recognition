from keras.models import load_model
import matplotlib.image as mpimg
import os
#import cv2
model = load_model('./model.h5')

count = 0
#images = []
images = 'Result: '
for item in os.listdir('./'):

    if item.endswith('.png'):
        image = mpimg.imread('./' + item)
        image = image.reshape(1,28,28,1).astype('float32')
        predict = model.predict(image)
        if predict[0][0]==1.0:
            images = (images+'A')
        if predict[0][1]==1.0:
            images = (images+'B')
        if predict[0][2]==1.0:
            images = (images+'C')
        if predict[0][3]==1.0:
            images = (images+'D')
        if predict[0][4]==1.0:
            images = (images+'E')
        if predict[0][5]==1.0:
            images = (images+'F')
        if predict[0][6]==1.0:
            images = (images+'G')
        if predict[0][7]==1.0:
            images = (images+'H')
        if predict[0][8]==1.0:
            images = (images+'I')
        if predict[0][9]==1.0:
            images = (images+'J')
        if predict[0][10]==1.0:
            images = (images+'K')
        if predict[0][11]==1.0:
            images = (images+'L')
        if predict[0][12]==1.0:
            images = (images+'M')
        if predict[0][13]==1.0:
            images = (images+'N')
        if predict[0][14]==1.0:
            images = (images+'O')
        if predict[0][15]==1.0:
            images = (images+'P')
        if predict[0][16]==1.0:
            images = (images+'Q')
        if predict[0][17]==1.0:
            images = (images+'R')
        if predict[0][18]==1.0:
            images = (images+'S')
        if predict[0][19]==1.0:
            images = (images+'T')
        if predict[0][20]==1.0:
            images = (images+'U')
        if predict[0][21]==1.0:
            images = (images+'V')
        if predict[0][22]==1.0:
            images = (images+'W')
        if predict[0][23]==1.0:
            images = (images+'X')
        if predict[0][24]==1.0:
            images = (images+'Y')
        if predict[0][25]==1.0:
            images = (images+'Z')


print(images)
