import os;
PATH_TO_IMAGE = "sampleDataset/";
PATH_TO_MASK = "sampleMask/";
PATH_TO_SAVE_IMAGES = "sampleAugumentation/images";
PATH_TO_SAVE_MASKS = "sampleAugumentation/masks";
if (not os.path.exists(PATH_TO_SAVE_IMAGES)):
    os.makedirs(PATH_TO_SAVE_IMAGES)
    
if (not os.path.exists(PATH_TO_SAVE_MASKS)):
    os.makedirs(PATH_TO_SAVE_MASKS)