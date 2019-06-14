import numpy as np
import cv2
path='/home/naruto/workspace/open cv/601862.jpg'
img=cv2.imread(path,0)

a=np.asarray(img)
'''
for i in img:
    for j in i:
        print(j)
'''
print(a)
