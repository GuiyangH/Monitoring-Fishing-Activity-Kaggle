#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:44:20 2017

@author: guiyang
"""

##First step, import pictures

#get the path and labels
import glob
import matplotlib as plt

def import_images():
  image_filenames = glob.glob("./train/*/*.jpg")
  
  #example of 1 path
  print image_filenames[0]# This is the label of a certain file

  #example of 1 image with its label
  img1 = plt.image.imread(image_filenames[0])
  label1 = image_filenames[0][8:-14]
  print label1
  
  return plt.image.imread(image_filenames[0]) image_filenames[:][8:-14]
  
  

## show what is like of a image
#plt.pyplot.imshow(img1[:,:,:])

#print img1[:,0,0]
#print img1[0,:,0]


## Real Training Process


############################################################################ Try to do amax_pooling
#import numpy as np
#import tensorflow as tf
#
#height,width,channels = 720,1280,3
#
#dataset =[np.array(img1,dtype = np.float32)]
#
#X = tf.placeholder(tf.float32,shape = (None,height,width,channels))
#max_pool = tf.nn.max_pool(X,ksize=[1,2,2,1],strides=[1,1,1,1],padding='VALID')
#with tf.Session() as sess:
#    output=sess.run(max_pool, feed_dict = {X:dataset})
#    
#plt.pyplot.imshow(output[0].astype(np.int8))

##############################################################################################################################
########################################################################### Try to do a convolutional layer
#import numpy as np
#import tensorflow as tf
#
#height,width,channels = 720,1280,3
#
#dataset =[np.array(img1,dtype = np.float32)]
#
#filter_test = np.zeros(shape=(15,15,channels,2),dtype=np.float32)#2 filters are involved here. patch_size =15*15
#filter_test[:,3,:,0] = 1
#filter_test[3,:,:,1] = 1
#
#X = tf.placeholder(tf.float32,shape=(None,height,width,channels))
#convolution = tf.nn.conv2d(X,filter_test,strides=[1,1,1,1],padding="SAME")
#
#with tf.Session() as sess:
#    output = sess.run(convolution,feed_dict={X:dataset})
#    
#    
#plt.pyplot.imshow(output[0,:,:,1])#pot the first image's 2nd filter output

###############################################################################################################################

### Put things together:!
