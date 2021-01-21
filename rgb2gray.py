import os
#from PIL import Image
import glob
import numpy as np
import cv2

#G:\项目\Change_Architec\data

#infolder = r'train/'
#outfolder = r'train_grew/'
infolder = r'test/'
outfolder = r'test_grew/'
#folddirs = os.listdir(infile)

files = glob.glob(os.path.join(infolder, '*.jpg'))
files.sort()
filecount = 0

for i in range(len(files)):
    #filepath = infile +'/' +foldername
    #print(filepath)
    #img = Image.open(filepath).convert('L')    #origin to gray and change size
    filename = os.path.basename(files[i])
    #print(filename)
    in_path = infolder + filename
    out_path = outfolder
    print(in_path)
    #img = Image.open(path)                  #change original size
    img=cv2.imread(in_path)
    #Img = np.array(img)
    #print(img.shape)
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #shape = Img.shape
    #out = img.resize((424, 424),Image.ANTIALIAS)
    filecount = filecount + 1
    cv2.imwrite(out_path+'test_%04d.jpg'%(filecount), gray_img)
    #print(out)
    '''
    newfilename = outfile + str(filecount) + '.bmp'
    out.save(newfilename)
    '''
