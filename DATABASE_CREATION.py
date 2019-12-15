import matplotlib.pyplot as plt
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(r'C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier(r'C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

all_faces = []

thiz = []

for dff in range(5000):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        roi_gray = cv2.resize(roi_gray, (256, 256))
        all_faces.append(roi_gray)




    cv2.imshow('img',roi_gray)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


for i in range(len(all_faces)):
    path = r'C:\Users\dbryc\Desktop\images'
    name = 'im'+str(i)+'.jpg'
    f = os.path.join(path, name)
    cv2.imwrite(f, faces[i])


cap.release()
cv2.destroyAllWindows()


for img in (os.listdir(r'C:\Users\HP\OneDrive\Pictures\COPIED')):
    path = os.path.join(r'C:\Users\HP\OneDrive\Pictures\COPIED', img)
    img = cv2.imread(path,0)
    images.append(img)


def extracteyes(data):
    asd = []
    for i in range(len(data)):
        t = []
        eyes = eye_cascade.detectMultiScale(images[i])
        for (ex,ey,ew,eh) in eyes:
            eyes = images[i][ey:ey+eh, ex:ex+ew]
            if np.shape(eyes)[0] >38:
                eyes = cv2.resize(eyes, (50,50))
                t.append(eyes)
        asd.append(t)

    return asd
GitHub
