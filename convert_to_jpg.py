import cv2
import numpy as np
import os

data_dir=r'F:\python\iit hackathoon\images'
categories=["door","staircase","switch board"]

for category in categories:
    i=0
    path=os.path.join(data_dir,category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img))
        cv2.imwrite(category+str(i)+".jpg",img_array)
        i=i+1
        print(i)
