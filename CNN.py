
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense,Dropout,BatchNormalization
import keras
import numpy as np
from sklearn.model_selection import train_test_split
import os
import matplotlib.image as mpimg

images = []
labels = []

def get_path(path_name):
    count = 0
    for item in os.listdir(path_name):
        full_path = os.path.join(path_name, item)

        if os.path.isdir(full_path):
            get_path(full_path)
        else:
            if item.endswith('.png') and count<=5000:
                image = mpimg.imread(full_path)
                image = image.reshape(28,28,1).astype('float32')
                print(image.shape)
                images.append(image)
                labels.append(path_name)
                count = count+1
    #print(images)
    #print(labels)
    return images, labels


x_train,labels = get_path("./A_Z Handwritten Data")
for i in range(len(labels)):
        if labels[i].endswith('A'):
            labels[i] = 0
        elif labels[i].endswith('B'):
            labels[i] = 1
        elif labels[i].endswith('C'):
            labels[i] = 2
        elif labels[i].endswith('D'):
            labels[i] = 3
        elif labels[i].endswith('E'):
            labels[i] = 4
        elif labels[i].endswith('F'):
            labels[i] = 5
        elif labels[i].endswith('G'):
            labels[i] = 6
        elif labels[i].endswith('H'):
            labels[i] = 7
        elif labels[i].endswith('I'):
            labels[i] = 8
        elif labels[i].endswith('J'):
            labels[i] = 9
        elif labels[i].endswith('K'):
            labels[i] = 10
        elif labels[i].endswith('L'):
            labels[i] = 11
        elif labels[i].endswith('M'):
            labels[i] = 12
        elif labels[i].endswith('N'):
            labels[i] = 13
        elif labels[i].endswith('O'):
            labels[i] = 14
        elif labels[i].endswith('P'):
            labels[i] = 15
        elif labels[i].endswith('Q'):
            labels[i] = 16
        elif labels[i].endswith('R'):
            labels[i] = 17
        elif labels[i].endswith('S'):
            labels[i] = 18
        elif labels[i].endswith('T'):
            labels[i] = 19
        elif labels[i].endswith('U'):
            labels[i] = 20
        elif labels[i].endswith('V'):
            labels[i] = 21
        elif labels[i].endswith('W'):
            labels[i] = 22
        elif labels[i].endswith('X'):
            labels[i] = 23
        elif labels[i].endswith('Y'):
            labels[i] = 24
        elif labels[i].endswith('Z'):
            labels[i] = 25
#print(x_train)
#print(labels)
x_train,x_test,y_train,y_test = train_test_split(x_train,labels,test_size=0.2,random_state = 35)
x_train = np.array(x_train)
x_test = np.array(x_test)



y_train = np.array(y_train)
y_test = np.array(y_test)


y_train = keras.utils.to_categorical(y_train,26)
y_test = keras.utils.to_categorical(y_test,26)
#print(y_train)
#x_train.reshape(297960,28,28,1).astype('float32')
x_train = x_train/255.0
x_test = x_test/255.0
#shape = x_train.shape[1:]
#print(shape)
model = Sequential()
model.add(Conv2D(32,(3,3),input_shape = (28,28,1),activation = 'relu'))
model.add(Conv2D(32,(3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))
#model.add(BatchNormalization())
model.add(Conv2D(64,(3,3),activation = 'relu'))
model.add(Conv2D(64,(3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(26,activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#np.reshape(x_train,(297960,28,28,1))
#x_train.reshape(len(x_train),28,28,1)
model.fit(x_train,y_train,epochs=10)

test_loss, test_accuracy = model.evaluate(x_test, y_test)
model.save('./model.h5')
print("test_loss:",test_loss)
print("test_accuracy:",test_accuracy)
