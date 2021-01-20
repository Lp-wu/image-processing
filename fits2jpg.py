import argparse
import numpy as np
import cv2
import math
import random
from scipy.stats import norm
import matplotlib.pyplot as plt
import os
import pyfits
import glob
from IPython import embed
# mode : 0 training : 1 testing

def adjust(origin):
    img = origin.copy()
    img[img>4] = 4
    img[img < -0.1] = -0.1
    MIN = np.min(img)
    MAX = np.max(img)
    img = np.arcsinh(10*(img - MIN)/(MAX-MIN))/3
    return img

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--fwhm", default="1.4")
  parser.add_argument("--sig", default="1.2")
  parser.add_argument("--input", default="/home/ubuntu/GalaxyGAN_python/fits_train")   #./fits_0.01_0.02
  parser.add_argument("--figure", default="figures")       #./figures/test
  #parser.add_argument("--gpu", default = "1")
  parser.add_argument("--model", default = "models")
  parser.add_argument("--mode", default="0")
  args = parser.parse_args()

  input =  args.input
  figure = args.figure
  mode = int(args.mode)

  train_folder = '%s/train'%(args.figure) #figures/train
  test_folder = '%s/test'%(args.figure)   #figures/test

  if not os.path.exists('./' + args.figure):
    os.makedirs("./" + args.figure)
  if not os.path.exists("./" + train_folder):
    os.makedirs("./" + train_folder)
  if not os.path.exists("./" + test_folder):
    os.makedirs("./" + test_folder)
  
  fits = '%s/*/*-g.fits'%(input)  #GalaxyGAN_python/fits_train/*/*-g.fits
  files = glob.iglob(fits)

  is_demo = 0

  for i in files:
      file_name = os.path.basename(i)

      filename = file_name.replace("-g.fits", '')
      print(filename)
      filename_g = '%s/%s/%s-g.fits'%(input,filename,filename)
      filename_r = '%s/%s/%s-r.fits'%(input,filename,filename)
      filename_i = '%s/%s/%s-i.fits'%(input,filename,filename)

      gfits = pyfits.open(filename_g)
      rfits = pyfits.open(filename_r)
      ifits = pyfits.open(filename_i)
      data_g = gfits[0].data
      data_r = rfits[0].data
      data_i = ifits[0].data
      
      figure_original = np.ones((data_g.shape[0],data_g.shape[1],3))
      figure_original[:,:,0] = data_g
      figure_original[:,:,1] = data_r
      figure_original[:,:,2] = data_i

      if is_demo:
        cv2.imshow("img", adjust(figure_original))
        cv2.waitKey(0)
    
      # thresold阈值
      MAX = 4
      MIN = -0.1

      figure_original[figure_original<MIN]=MIN
      figure_original[figure_original>MAX]=MAX

      # normalize figures
      figure_original = (figure_original-MIN)/(MAX-MIN)

      # asinh scaling
      figure_original = np.arcsinh(10*figure_original)/3

      '''
      # output result to pix2pix format
      figure_combined = np.zeros((data_g.shape[0], data_g.shape[1]*2,3))
      figure_combined[:,: data_g.shape[1],:] = figure_original[:,:,:]
      figure_combined[:, data_g.shape[1]:2*data_g.shape[1],:] = figure_blurred[:,:,:]
      '''

      if mode:
        jpg_path = '%s/test/%s.jpg'% (figure,filename)
      else:
        jpg_path = '%s/train/%s.jpg'% (figure,filename)


      if mode == 0 or mode == 1:
        image = (figure_original*256).astype(np.int)
        cv2.imwrite(jpg_path, image)
        































