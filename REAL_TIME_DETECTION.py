import os
import cv2
import matplotlib.pyplot as plt
import random
import numpy as np
from sklearn import datasets, svm, metrics

nsum = []

bsum = []

img_data = []
img_labels = []

dir_normal = r'C:\Users\HP\OneDrive\Pictures\eyes\nob'
dir_malaria = r'C:\Users\HP\OneDrive\Pictures\eyes\blink'

face_cascade = cv2.CascadeClassifier(r'C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier(r'C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_eye.xml')


print('Fettching Data')

for normal_img in (os.listdir(dir_normal)):
    path = os.path.join(dir_normal, normal_img)
    img = cv2.imread(path,0)
    try:
        img = cv2.resize(img, (50,50))
        img = np.reshape(img, (2500,))
        img_data.append(img/256)
        img_labels.append(0)

        nsum.append(img.sum())
    except:
        pass

for malaria_img in (os.listdir(dir_malaria)):
    path = os.path.join(dir_malaria, malaria_img)
    img = cv2.imread(path,0)
    try:
        img = cv2.resize(img, (50, 50))
        img = np.reshape(img, (2500,))
        img_data.append(img/256)
        img_data.append(img/256)
        img_data.append(img/256)
        img_data.append(img/256)
        img_data.append(img/256)
        img_data.append(img/256)
        img_labels.append(1)
        img_labels.append(1)
        img_labels.append(1)
        img_labels.append(1)
        img_labels.append(1)
        img_labels.append(1)
        bsum.append(img.sum())
    except:
        pass

allz = []

ziped = list(zip(img_data, img_labels))
random.shuffle(ziped)

img_data, img_labels = zip(*ziped)
