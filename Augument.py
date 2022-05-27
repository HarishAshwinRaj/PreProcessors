import albumentations as A
import cv2
import config
import os
import matplotlib.pyplot as plt 

transformA = A.Compose([A.HorizontalFlip(p=1), A.GaussianBlur(),A.RandomBrightnessContrast(p = 0.5)])
transformB = A.Compose([A.VerticalFlip(p = 1),A.GaussianBlur(),A.RandomBrightnessContrast(p = 0.5)])
transformD = A.Compose([A.RandomBrightnessContrast(p = 0.5), A.GaussianBlur(), A.ChannelShuffle( p = 1)])

transforms = [transformA, transformB, transformD]
AugLabel = ['horizontalFlip','verticalFilp', 'channelShuffle']

def augument(PATH_TO_SAVE_IMAGE = config.PATH_TO_SAVE_IMAGE,
             PATH_TO_SAVE_MASK = config.PATH_TO_SAVE_MASK,
             PATH_TO_SAVE_AUG_IMAGES = config.PATH_TO_SAVE_AUG_IMAGES,
             PATH_TO_SAVE_AUG_MASKS = config.PATH_TO_SAVE_AUG_IMAGES
            ):
    files = os.listdir(PATH_TO_SAVE_IMAGE);

    for file in files:
        fullpath = os.path.join(PATH_TO_SAVE_IMAGE,file);
        imageArray = cv2.imread(fullpath);
        imageArray = cv2.cvtColor(imageArray, cv2.COLOR_BGR2RGB);

        fullpathmask = os.path.join(PATH_TO_SAVE_MASK,file);
        maskArray = cv2.imread(fullpathmask)

        for label ,transform in zip(AugLabel,transforms):
            transformed= transform(image= imageArray, mask = maskArray);
            transformed_image = transformed['image'];
            transformed_mask = transformed['mask'];

            # plt.imshow(imageArray);
            # plt.show();
            # plt.imshow(transformed_image);
            # plt.show();

            # plt.imshow(maskArray);
            # plt.show();
            # plt.imshow(transformed_mask);
            # plt.show();

            filename = file;
            filename = filename.split('.');
            filename[0] = filename[0] + "_AUG_" + label;
            filename = '.'.join(filename)
            print(filename)

            cv2.imwrite(os.path.join(PATH_TO_SAVE_AUG_IMAGES, filename),transformed_image);
            cv2.imwrite(os.path.join(PATH_TO_SAVE_AUG_MASKS, filename), transformed_mask );

if(__name__ == '__main__'):
    augument();


    
    

