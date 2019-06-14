import os
import numpy as np
import cv2 
count=1
'''path=os.listdir('/home/naruto/Downloads/dogs-vs-cats/train/')
c=0
for files in path:
    if files.endswith('.jpg'):
       # filee=open(files)
        img=cv2.imread(files,0)
        arr=np.asarray(img)
        print(arr.shape)
'''
img=cv2.imread('/home/naruto/Downloads/dogs-vs-cats/train/cat.0.jpg')
arr=np.asarray(img)
print(arr.shape)

name=f"cat.{count}.jpg"
print(name)
c=0
for count in range(1,25001):
        name=f"cat.{count}.jpg"
        path=f"/home/naruto/Downloads/dogs-vs-cats/train/{name}"
        img=cv2.imread(path)
        arr=np.asarray(img)
        print(count)
