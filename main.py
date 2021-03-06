# Import fish image as RBG scale.
from import_image import import_images
x_in,y_in = import_images()

#start a session
import tensorflow as tf
sess = tf.InteractiveSession()

#placeholder
x= tf.placeholder(tf.float32,shape=(None,720,128,3)) # height,width,channel
y_= tf.placeholder(tf.float32,shape=(None,8))

#Weight/filter &Bias function

def weight_variable(shape):
    initial = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial=tf.constant(0.1,shape=shape)
    return tf.Variable(initial)
    

#Convolution and Pooling

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
    
def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    

#firstConvolution layer including ReLU
W_conv1 =weight_variable([5,5,3,32])#5x5 patch dimension,3 input channel,32 output channels
b_conv1= bias_variable([32])

h_conv1 = tf.nn.relu(conv2d(x,W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

#second C layer

W_conv2 =weight_variable([5,5,32,64])
b_conv2= bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

#fully connected Layer
W_fcl = weight_variable([7*7*64,1024])
b_fcl = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
h_fcl = tf.nn.relu(tf.matmul(h_pool2_flat,W_fcl) + b_fcl)

# Implement a drop out(good way to protect overfitting)
keep_prob = tf.placeholder(tf.float32)
h_fcl_drop = tf.nn.dropout(h_fcl,keep_prob)

#Readout layer
W_fc2 = weight_variable([1024,8])
b_fc2 = bias_variable([8])

y_conv = tf.nn.softmax(tf.matmul(h_fcl_drop,W_fc2)+b_fc2)


import numpy as np
#Train and evaluate the Model
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))  #loss func
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)  #optimizer

correct_prediction = tf.equal(tf.argmax(y_conv,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

sess.run(tf.initialize_all_variables()) #initial variables

for i in range(len(y_in)/500):
    x_train = x_in[i*500:(i+1)*500]
    y_train = y_in[i*500:(i+1)*500]
    if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict={
                x:x_train, y_:batch[1], keep_prob: 1.0})
        print('step %d, training accuracy %g'%(i,train_accuracy))
    train_step.run(feed_dict={x:x_train,y_:batch[1],keep_prob:0.5})
    
# the test set is not yet defined.   
print("test accuracy %g"%accuracy.eval(feed_dict={x:x_test,y_:y_test,keep_prob:1.0}))

