import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian(initalgaussimg,i,j,sigma):
  h_x = initalgaussimg.shape[0]
  w_y = initalgaussimg.shape[1]
  center_x = h_x/2
  center_y = w_y/2
  out_xy = np.exp(-((i-center_x)**2 + (j-center_y)**2)/(2.*sigma*sigma))

  return out_xy

if __name__ == "__main__":
  print("生成高斯模糊核的图像...")
  IMG_WIDTH = 180
  IMG_HEIGHT = 180
  Gauss_map = np.zeros((IMG_HEIGHT,IMG_WIDTH))

  sigma_list = [0.1,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]

  for num in range(len(sigma_list)):
    for i in range(IMG_HEIGHT):
      for j in range(IMG_WIDTH):
        Gauss_map[i,j] = gaussian(Gauss_map,i,j,sigma_list[num])
      
    # 显示和保存生成的图像
    plt.figure()
    plt.imshow(Gauss_map, plt.cm.gray)
    plt.imsave('Gauss_map_%d.png'%(num+1), Gauss_map, cmap=plt.cm.gray)
    plt.show()
