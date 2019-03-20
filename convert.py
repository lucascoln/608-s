'''import json
import os
import pandas as pd


img_dir=['./ReCTS_part1/img',
         './ReCTS_part2/img',
         './ReCTS_part3/img',
         './ReCTS_part4/img']
label_dir='./ReCTS_part1/gt'
filenames=os.listdir(label_dir)
after = []
for filename in filenames:
    filepath = label_dir + '/' + filename
    with open(filepath, 'rb') as f:
        data = json.load(f) #dict

    year_str_lst = data["chars"].keys()
    print(year_str_lst)'''
import json
import pandas as pd
import os
import csv
import cv2
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np

label_dir='./ReCTS_part1/gt'
filenames=os.listdir(label_dir)
df = pd.DataFrame()
set_width = 3500
set_height = 4500
img_dir=['./ReCTS_part1/img',
         './ReCTS_part2/img',
         './ReCTS_part3/img',
         './ReCTS_part4/img']
img_names=os.listdir(img_dir[0])
'''
from PIL import Image
def getmaxpixel():   #获取所有图像中最大像素值
    rootdir = './ReCTS_part1/img'
    list = os.listdir(rootdir)
    h=0
    w=0
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isfile(path):
            img = Image.open(path)
            imgSize = img.size #图片的长和宽
            if(imgSize[0]>w):
                w = imgSize[0]
            if (imgSize[1] > h):
                h = imgSize[1]
    print (w,h)
    return w,h
getmaxpixel()


def conver_pix():
    for img_name in img_names:
        c_array = np.zeros(((set_width, set_height, 3)))
        imgs = cv2.imread(img_dir[0]+'/'+img_name)
      #  plt.imshow(imgs)
        img_width = imgs.shape[1]
        img_height = imgs.shape[0]
        c_array[0:img_height,0:img_width,:]=imgs
        cv2.imwrite('./converted_imgs/'+img_name+'.jpg',c_array)
        #print(img_width.head())
conver_pix()
'''

def get_location():
    for filename in filenames:
        filepath = label_dir + '/' + filename
        with open(filepath, 'r',encoding="utf-8") as f:
            data = json.load(f) #dict
            for i in data['chars']:
                x = pd.Series(data=i)
            print(len(data['chars']))

    print(s1[0])
get_location()
    #    with open('./mycsv.csv','w',newline='') as w:
    #      csv_writer=csv.writer(w, quoting=csv.QUOTE_ALL)
           ##print(test)
            #test.to_csv('converted7.csv', index=True,index_label=filename,encoding="utf_8_sig",mode='a')
