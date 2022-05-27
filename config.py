import os;
TOTAL_CLASSES = 1;
PATH_TO_SET = "set3";
PATH_TO_EXTRACT_IMAGE = PATH_TO_SET+"/RawData/Images";
PATH_TO_SAVE_IMAGE = PATH_TO_SET+"/ProcessedData/Images";
PATH_TO_SAVE_MASK = PATH_TO_SET+"/ProcessedData/Masks";
PATH_TO_ANNOTATIONS = PATH_TO_SET+"/RawData/via_region_data.json";
PATH_TO_SAVE_AUG_IMAGES = PATH_TO_SET+"/ProcessedData/AugumentedImages";
PATH_TO_SAVE_AUG_MASKS = PATH_TO_SET+"/ProcessedData/AugumentedMasks";

#combining all the images in same path;
PATH_TO_SAVE_AUG_IMAGES = PATH_TO_SAVE_IMAGE
PATH_TO_SAVE_AUG_MASKS = PATH_TO_SAVE_MASK

if (not os.path.exists(PATH_TO_SAVE_IMAGE)):
    os.makedirs(PATH_TO_SAVE_IMAGE)
    
if (not os.path.exists(PATH_TO_SAVE_MASK)):
    os.makedirs(PATH_TO_SAVE_MASK)

if (not os.path.exists(PATH_TO_SAVE_AUG_IMAGES)):
    os.makedirs(PATH_TO_SAVE_AUG_IMAGES)
    
if (not os.path.exists(PATH_TO_SAVE_AUG_MASKS)):
    os.makedirs(PATH_TO_SAVE_AUG_MASKS)