import os
import glob
import numpy as np
import cv2

infolder = r'set12/'
outfolder = r'set12_resize/'

files = glob.glob(os.path.join(infolder, '*.jpg'))
files.sort()
filecount = 0

for i in range(len(files)):
  filename = os.path.basename(files[i])
  in_path = infolder + filename
  out_path = outfolder
  print(in_path)
  img=cv2.imread(in_path)
  resize_img = cv2.resize(img,(424,424),interpolation=cv2.INTER_CUBIC)
  filecount = filecount + 1
  cv2.imwrite(out_path+'test_%04d.jpg'%(filecount), resize_img)








































  

