import cv2
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import config

PathToImag = config.PATH_TO_EXTRACT_IMAGE;#"sampleDataset/";
PathToSaveImg = config.PATH_TO_SAVE_IMAGE;
PathToAnnotation = config.PATH_TO_ANNOTATIONS;
TotalClasses = config.TOTAL_CLASSES;
PathToSave = config.PATH_TO_SAVE_MASK;

f = open(PathToAnnotation)
dict_t= json.load(f);
print("total no of files ",len(dict_t));
for x in dict_t:
    filename = dict_t[x]["filename"]
    OriginalImage =cv2.imread(os.path.join(PathToImag,filename)) 
    print(filename);
    Canvas_size = OriginalImage.shape[:2];
    #print(Canvas_size)
    Canvas = np.zeros(Canvas_size);
    #print(filename);
    for reg in dict_t[x]["regions"]:
        xPoints = np.array(reg["shape_attributes"]["all_points_x"])
        yPoints = np.array(reg["shape_attributes"]["all_points_y"])
        classReg = list(reg["region_attributes"]["DEFECTS"].keys() )[0];
        points = np.stack([xPoints,yPoints], axis = -1);
        #print()
        classNo = int(classReg.strip());
        color = int(round((classNo * 255)/TotalClasses));
        #print(color)
        cv2.fillPoly(Canvas,pts = [points], color = (color));
        #print(type(classReg), type(classNo));
    # plt.imshow(OriginalImage)
    # plt.show()
    # plt.imshow(Canvas)
    # plt.show()
    cv2.imwrite(os.path.join(PathToSaveImg,filename),OriginalImage);
    cv2.imwrite(os.path.join(PathToSave,filename),Canvas);
    #xPoint = dict_t[x]["shape_attributes"]["all_points_x"]







