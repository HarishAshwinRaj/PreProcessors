import cv2
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import config


def detect(PathToImag = config.PATH_TO_EXTRACT_IMAGE,
            PathToSaveImg = config.PATH_TO_SAVE_IMAGE,
            PathToAnnotation = config.PATH_TO_ANNOTATIONS,
            TotalClasses = config.TOTAL_CLASSES,
            PathToSave = config.PATH_TO_SAVE_MASK,
            printSample = config.PRINT_SAMPLE_COUNT
            ):
        f = open(PathToAnnotation)
        dict_t= json.load(f);
        print("total no of files ",len(dict_t));
        notFoundCount = 0
        sampleCount = 0
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
            #print(filename);
            for reg in dict_t[x]["regions"]:
                xPoints = np.array(reg["shape_attributes"]["all_points_x"])
                yPoints = np.array(reg["shape_attributes"]["all_points_y"])
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
                color = int(round((classNo * 255)/TotalClasses));
                #print(color)
                cv2.fillPoly(Canvas,pts = [points], color = (color));
                #print(type(classReg), type(classNo));
            if (sampleCount < printSample):
                plt.imshow(OriginalImage)
                plt.show()
                plt.imshow(Canvas)
                plt.show()
                sampleCount += 1
            
            cv2.imwrite(os.path.join(PathToSaveImg,filename),OriginalImage);
            cv2.imwrite(os.path.join(PathToSave,filename),Canvas);
         
            #xPoint = dict_t[x]["shape_attributes"]["all_points_x"]
        print("Images Not Found :",notFoundCount)

if(__name__ == '__main__'):
    detect();






