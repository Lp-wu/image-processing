import os
import glob
import numpy as np
import cv2
from PIL import Image
from astropy.io import fits
from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import imageio
import scipy 

def imsave(arr,path):
  return imageio.imwrite(path,arr)


inputf = 'imaging_psf_0.fits'
exinf = 'expanded_sorce'
poinf = 'point_sorce'
exout = 'expanded_dirty'
pout = 'point_dirty'

hdulist = fits.open( inputf )
psf = hdulist[0].data
#print(psf.shape)
psf = psf[0,0,:,:]#2-D

exfiles = glob.glob(os.path.join(exinf,'*.npy'))
exfiles.sort()

for num in range(len(exfiles)):
  exfilename = os.path.basename(exfiles[num])
  print(exfilename)
  exname, ext = os.path.splitext(exfilename)
  exinpath = exinf + exfilename
  outpath_expanded = exout + '/' + exname + '.npy'
  ex_img=np.load(exfiles[num])#（h,w）
  ex_img = ex_img.reshape(1,1,128,128)#(1,1,h,w)
  print(ex_img.shape)
  np.save('expanded_sorce_4D/'+exname+'.npy', ex_img)
  ex_img = ex_img[0,0,:,:]
  ex_img = ex_img.flatten()
  noise = np.random.normal(0, 0.01*0.005, ex_img.shape[0])
  ex_dirty_noise = ex_img + noise
  ex_dirty_noise = ex_dirty_noise.reshape(128,128)
  ex_dirty = scipy.signal.fftconvolve(ex_dirty_noise, psf, mode='same', axes=None)#2-D
  ex_dirty = ex_dirty.reshape(1,1,128,128)
  #print(ex_dirty.max())
  np.save(outpath_expanded, ex_dirty)
  #value = np.load(outpath_expanded)
  #print(value.max())
  #ex_dirty_psf = np.expand_dims(ex_dirty_psf,0)
  #ex_dirty_psf = np.expand_dims(ex_dirty_psf,1)

pofiles = glob.glob(os.path.join(poinf, '*.npy'))
pofiles.sort()

for acount in range(len(pofiles)):
  pofilename = os.path.basename(pofiles[acount])
  print(pofilename)
  poname, ext = os.path.splitext(pofilename)
  poinpath = poinf + pofilename
  outpath_point = pout + '/' + poname + '.npy'
  po_img = np.load(pofiles[acount])#(h,w)
  po_img = po_img.reshape(1,1,128,128)
  print(po_img.shape)
  np.save('point_sorce_4D/'+poname+'.npy', po_img)
  po_img = po_img[0,0,:,:]
  po_img = po_img.flatten()
  noise = np.random.normal(0, 0.01*0.005, po_img.shape[0])
  po_dirty_noise = po_img + noise
  po_dirty_noise = po_dirty_noise.reshape(128,128)
  po_dirty = scipy.signal.fftconvolve(po_dirty_noise, psf, mode='same', axes=None)#2-D
  po_dirty = po_dirty.reshape(1,1,128,128)
  print(po_dirty.shape)
  np.save(outpath_point, po_dirty)
  
'''
img=cv2.imread('train_0001.png')
resize_img = cv2.resize(img,(128,128),interpolation=cv2.INTER_CUBIC)
resize_img = resize_img[:,:,0]


#grad=signal.convolve2d(img,data,boundary='symm',mode='same')

#dirty = np.expand_dims(grad,0)
#dirty = np.expand_dims(dirty,1)
dirty_psf = dirty_psf.flatten()
print(dirty_psf.shape)
noise = np.random.normal(0, 200, dirty_psf.shape[0])
print(noise.shape)
dirty = dirty_psf + noise
dirty = dirty.reshape(128,128)

im = imsave(dirty, 'dirty.png')
'''



















