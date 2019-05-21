import cv2
import numpy as np


img=cv2.imread('601862.jpg',0)
img=cv2.resize(img,dsize=(1080,720),interpolation=cv2.INTER_NEAREST)
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
a=np.asarray(img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
for i in a:
    for j in i:
        print(j)
    print('\n')
