# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:26:18 2022

@author: ashwi
"""

from skimage.morphology import skeletonize
from scipy import ndimage
import cv2

import os
import numpy as np
import matplotlib.pyplot as plt

listImg = os.listdir('sampleThickness/');
imgPath = listImg[0];
#imgPath = os.path.join(config.PATH_TO_MASK,imgPath);
img = cv2.imread(os.path.join('sampleThickness/',imgPath));

img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY);
th,img = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
plt.figure(figsize = (8,8))
plt.imshow(img,cmap = 'gray');
plt.show();
dt = ndimage.distance_transform_edt(img)
plt.figure(figsize = (8,8))
plt.imshow(dt,cmap ='gray');
plt.show();
skeleton = skeletonize(img)
plt.figure(figsize = (8,8))
plt.imshow(skeleton,cmap ='gray');
plt.show();
sktthick = dt[skeleton]
thickness = np.mean(sktthick)

print("Average Thickness : ",thickness*2);
   



