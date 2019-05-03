import os,time
import cv2
#from PLT  import Image as PImage
a=os.listdir('c:\\Workspace\\Test programs\\images\\')
for image in a:
    time.sleep(1)
    #img=cv2.imread(image,0)
    #cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
    #cv2.imshow('image',f"{image}.jpg")
    #cv2.destroyAllWindows()
    print(image)
