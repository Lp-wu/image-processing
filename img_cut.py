import os
import glob
import numpy as np
import cv2
from PIL import Image
from collections import Counter
from matplotlib import pyplot

infolder = r"train_grew/"
#infolder = r"test_grew2expanded/"
outfolder_expanded = r"expanded_sorce/"
outfolder_point = r"point_sorce/"

if not os.path.exists(outfolder_expanded):
  os.makedirs(outfolder_expanded)
if not os.path.exists(outfolder_point):
  os.makedirs(outfolder_point)

files = glob.glob(os.path.join(infolder,'*.png'))
files.sort()
filecount=0

for num in range(len(files)):
  #print(files[num])
  filename = os.path.basename(files[num])
  name, ext = os.path.splitext(filename)
  #print(filename)
  inpath = infolder + filename
  outpath_expanded = outfolder_expanded + name
  outpath_point = outfolder_point + name
  img = cv2.imread(inpath).astype(np.float32)#(w,h,c)
  
  img_expanded = img[123:-123, 123:-123, :].copy()
  img_expanded = cv2.resize(img_expanded,(126,126),interpolation=cv2.INTER_LANCZOS4)
  img_expanded = img_expanded[:,:,0]#(w,h)
  img_expanded = np.pad(img_expanded,((1,1),(1,1)),'constant' )
  img_expanded = (0.01/255.)*img_expanded #归一化到0~0.1
  #print(img_expanded.max())
  np.save(outpath_expanded,img_expanded)
  #value = np.load(outpath_expanded+'.npy')
  #print(value.max())
  
  #pyplot.imsave(outpath_expanded,img_expanded)
  #value = cv2.imread(outpath_expanded).astype(np.float32)
  #print("\n",value[:,:,0],value[:,:,0].shape,value[:,:,0].max(),"\n")

  img_point = img.copy()
  #img_point = img_point[:,:,0]
  img_point[123:-123, 123:-123] = 0
  #print(img_point[123:-123, 123:-123],img_point[123:-123, 123:-123].max(),img_point[123:-123, 123:-123].min())
  #img_point = cv2.resize(img,(180,180),interpolation=cv2.INTER_LANCZOS4)
  img_point = img_point - 70 #10，30(x)，50，70，100
  #print(img_point.min())
  img_point[img_point < 0] = 0
  img_point = cv2.resize(img,(128,128),interpolation=cv2.INTER_LANCZOS4)
  #print(img_point,img_point.shape)
  img_point = img_point[:,:,0]
  img_point = (0.01/255.)*img_point #归一化到0~0.1
  #print(img_point.max())
  
  np.save(outpath_point,img_point)
  #value = np.load(outpath_point+'.npy')
  #print(value.max())

print('finish')












  
