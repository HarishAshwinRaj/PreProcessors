import cv2
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import config
import sys

def detect(PathToImag = config.PATH_TO_EXTRACT_IMAGE,
            PathToSaveImg = config.PATH_TO_SAVE_IMAGE,
            PathToAnnotation = config.PATH_TO_ANNOTATIONS,
            TotalClasses = config.TOTAL_CLASSES,
            PathToSave = config.PATH_TO_SAVE_MASK,
            ImageSize = config.IMG_DIM,
            printSample = config.PRINT_SAMPLE_COUNT
            ):
        print(PathToAnnotation)
        f = open(PathToAnnotation)
        dict_t= json.load(f);
        print("total no of files ",len(dict_t));
        print("No of Classes ",TotalClasses);
        notFoundCount = 0
        sampleCount = 0
        noLabelCount = 0;
        for x in dict_t:
            filename = dict_t[x]["filename"]
            OriginalImage =cv2.imread(os.path.join(PathToImag,filename)) 
            print(filename);
            if( not isinstance(OriginalImage, np.ndarray)):
                print("IMAGE NOT FOUND");
                notFoundCount += 1;
                continue;
            Canvas_size = OriginalImage.shape[:2];
            #print(Canvas_size)
            Canvas = np.zeros(Canvas_size);
            interval = int((255/TotalClasses));
            #print(filename);
            for reg in dict_t[x]["regions"]:
                xPoints = np.array(reg["shape_attributes"]["all_points_x"])
                yPoints = np.array(reg["shape_attributes"]["all_points_y"])
                color = 0;

                if "region_attributes" in reg  and "DEFECTS" in reg["region_attributes"].keys():
                    classReg = reg["region_attributes"]["DEFECTS"] #radio
                    if(isinstance(classReg,dict) ):
                        ObtainedLabels = reg["region_attributes"]["DEFECTS"]; #if checkbox
                        print(ObtainedLabels);
                        if len(ObtainedLabels) == 0:
                            continue;
                        else:
                            
                            ObtainedLabels = list(k  for k,v in reg["region_attributes"]["DEFECTS"].items() if(bool(v) == True) )
                            classReg = ObtainedLabels[0]
                        print("cls No",classReg)
                        
                    points = np.stack([xPoints,yPoints], axis = -1);
                    #print()
                    classNo = int(classReg.strip());
                    color = int(classNo * interval);
                    
                    #print(color)
                    cv2.fillPoly(Canvas,pts = [points], color = (color));
                    #print(type(classReg), type(classNo)); 
                else :
                    print("NO LABEL PRESENT IN THE IMAGE", color);
                    noLabelCount  += 1
                
                        
            if (sampleCount < printSample):
                plt.imshow(OriginalImage)
                plt.show()
                plt.imshow(Canvas)
                plt.show()
                sampleCount += 1
            filename  = filename.split(".")[0]+".png"
            print(filename);
            cv2.imwrite(os.path.join(PathToSaveImg,filename),cv2.resize(OriginalImage,ImageSize));
            cv2.imwrite(os.path.join(PathToSave,filename), cv2.resize(Canvas,ImageSize, 0, 0, interpolation = cv2.INTER_NEAREST));#cv2.resize(Canvas, ImageSize));
           

            savedMask = cv2.imread( os.path.join(PathToSave,filename))
            print(np.unique(savedMask))
            #print("resized image",np.unique(cv2.resize(Canvas,ImageSize, 0, 0, interpolation = cv2.INTER_NEAREST)).shape);

            #xPoint = dict_t[x]["shape_attributes"]["all_points_x"]
        print("Images Not Found :", notFoundCount)
        print("NOT LABELED REGIONS : ", noLabelCount)

if(__name__ == '__main__'):
    if(len(sys.argv)  > 1) :
        detect(TotalClasses = int(sys.argv[1]));
    else :
        detect();





