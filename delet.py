# Import packages
import os
import argparse
import cv2
import numpy as np
import sys
import glob
import importlib.util
import time
import shutil

# Define and parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--imagedir', help='Name of the folder containing images to perform detection on. Folder must contain only images.',
                    default=None)
parser.add_argument('--failimagedir', help='Name of the folder containing images to perform fail detection on.',
                    default=None)
parser.add_argument('--successdir', help='Name of the xml folder containing images xml.',
                    default=None)

args = parser.parse_args()

# Parse input image name and directory. 
IM_DIR = args.imagedir
FA_DIR = args.failimagedir
SU_DIR = args.successdir

CWD_PATH = os.getcwd()

if IM_DIR:
    PATH_TO_IMAGES = os.path.join(CWD_PATH,IM_DIR)
    images = glob.glob(PATH_TO_IMAGES + '/*')

if FA_DIR:
    PATH_TO_FAIMAGES = os.path.join(CWD_PATH,FA_DIR)
    failimages = glob.glob(PATH_TO_FAIMAGES)[0]
    
if SU_DIR:
    PATH_TO_SUCCESS = os.path.join(CWD_PATH,SU_DIR)
    successfolder = glob.glob(PATH_TO_SUCCESS)[0]

# Loop over every image and perform detection
for image_path in images:
    start_time = time.time()
    # Load image and resize to expected shape [1xHxWx3]
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imH, imW, _ = image.shape 
    image_resized = cv2.resize(image_rgb, (300, 300))
    input_data = np.expand_dims(image_resized, axis=0)
    
    filename = image_path.split('\\')[-1]
    filename2 = str(filename.split('.')[0])
    filename3 = filename2 + '.xml'
    print('---------------------------------start--------------------------------------------------')
    print('image file name',filename)
    print('image file name',filename2)
    print('image file name',filename3)
    #os.remove(image_path)
    #os.remove(image_path)
    print('delete',filename3)