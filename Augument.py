import albumentations as A
import cv2
import config
import os
import matplotlib.pyplot as plt 

transform = A.Compose([
    
    A.HorizontalFlip(p=1),
    A.VerticalFlip(p = 1),
    A.RandomBrightnessContrast(p=0.2),
])

files = os.listdir(config.PATH_TO_IMAGE);

for file in files:
    fullpath = os.path.join(config.PATH_TO_IMAGE,file);
    imageArray = cv2.imread(fullpath);
    imageArray = cv2.cvtColor(imageArray, cv2.COLOR_BGR2RGB);

    fullpathmask = os.path.join(config.PATH_TO_MASK,file);
    maskArray = cv2.imread(fullpathmask)

    transformed= transform(image= imageArray, mask = maskArray);
    transformed_image = transformed['image'];
    transformed_mask = transformed['mask'];

    plt.imshow(imageArray);
    plt.show();
    plt.imshow(transformed_image);
    plt.show();

    plt.imshow(maskArray);
    plt.show();
    plt.imshow(transformed_mask);
    plt.show();

    cv2.imwrite(os.path.join(config.PATH_TO_SAVE_IMAGES,file),transformed_image);
    cv2.imwrite(os.path.join(config.PATH_TO_SAVE_MASKS,file), transformed_mask );



    
    

