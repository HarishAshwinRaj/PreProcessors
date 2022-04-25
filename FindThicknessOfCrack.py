from skimage.morphology import skeletonize
from scipy import ndimage
import cv2

import os
import numpy as np
import matplotlib.pyplot as plt
import config

def plot(img):
    plt.figure(figsize = (8,8))
    plt.imshow(img,cmap = 'gray');
    plt.show();

def findThickness(imgPath):

    img = cv2.imread(os.path.join(imgPath));
    img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY);
    th,img = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
    plot(img);

    dt = ndimage.distance_transform_edt(img)
    plot(dt);

    skeleton = skeletonize(img)
    plot(skeleton);

    sktthick = dt[skeleton]
    thickness = np.mean(sktthick)
    print("Average Thickness : ",thickness*2);

DirectoryPath  = "sampleThickness/";
listImg = os.listdir(DirectoryPath);
ImgFileName =  listImg[0];
imgPath = os.path.join(DirectoryPath,ImgFileName);
findThickness(imgPath);
#imgPath = os.path.join(confi
g.PATH_TO_MASK,imgPath);

   



