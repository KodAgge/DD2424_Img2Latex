import inkml2img
import os
# inkml2img.inkml2img('2013ALL_inkml_data/200923-1556-49.inkml','./2013ALL_inkml_data_image/200923-1556-49.png')

mode = 'TRAIN' # EK) If we're transforming training, test or validation images.
out_folder_suffix = '_transformed/' # EK) Folder name for transformed images. I changed this to "_transformed/" so that your data wouldn't be overwritten/duplicated when I did some tests.  

if mode == 'TRAIN':
    img_folder = r'./data/CROHME DATA/TRAIN_CROHME_8836'
elif mode == 'VALIDATION':
    img_folder = r'./data/CROHME DATA/VAL_CROHME_671'
elif mode == 'TEST':
    img_folder = r'./data/CROHME DATA/TEST_CROHME_2133'
else:
    raise ValueError('Value of variable "mode" not recognized, check spelling :)') 


# img_folder = directory + '\TEST_CROHME_2133'
i = 0
for entry in os.scandir(img_folder):
    if (entry.path.endswith(".inkml") or entry.path.endswith(".inmkl")) and entry.is_file():
        print(entry.path)

        img_name = 'Image' + str(i) +'.png'
        inkml2img.inkml2img(entry.path, r'./data/CROHME DATA/' + mode + out_folder_suffix + img_name)
        
        # Joar, här kan du skriva create_label_csv() funktionen. 

        i+= 1
        input('Done')