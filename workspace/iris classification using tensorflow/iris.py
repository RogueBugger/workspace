import tensorflow as tf
import numpy as np
from random import shuffle
import time,sys,random
import pandas as pd
from matplotlib import pyplot

learning_rate=0.1

dataset=pd.read_csv('dataset.csv')
x1=dataset['x1']
x2=dataset['x2']
x3=dataset['x3']
x4=dataset['x4']
data=[x1,x2,x3,x4]
t=dataset['target']
x=tf.placeholder(tf.float32,shape=(None))
target=tf.placeholder(tf.float32,shape=(None))
#layer0
weightI=tf.Variable(tf.random_normal([4,4]),name='weightsIH')

biasI=tf.Variable(tf.random_normal([4,1]))

layer1=tf.add(tf.matmul(weightI,x),biasI)
yI=tf.nn.sigmoid(layer1)

#input layer>1

weightIH=tf.Variable(tf.random_normal([4,4]),name='weightsIH')

biasIH=tf.Variable(tf.random_normal([4,1]))

layer1=tf.add(tf.matmul(weightIH,yI),biasIH)
yIH=tf.nn.sigmoid(layer1)

#input layer>2

weightHO=tf.Variable(tf.random_normal([1,4]),name='weightsHO')

biasHO=tf.Variable(tf.random_normal([1,1]))
layer2=tf.add(tf.matmul(weightHO,yIH),biasHO)
yHO=tf.nn.sigmoid(layer2)

costHO=tf.reduce_sum(tf.pow(yHO-target,2))
optimizerIO=tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(costHO)
#optimizerIO=tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(costHO)

epochs=10
epo=[]
init=tf.global_variables_initializer()
coost=[]
with tf.Session() as sess:
    sess.run(init)
    for e in range(epochs):
        np.random.shuffle(dataset.values)
        for d in range(len(dataset)):
            xi=[]
            for i in data:
                xi.append(i[d])
            xi=np.array(xi).reshape(4,1)
            tt=np.array(t[d])
            #print(np.shape(xi))
            sess.run(optimizerIO,feed_dict={x:xi,target:tt})
        coost.append(sess.run(costHO,feed_dict={x:xi,target:tt}))
        epo.append(e)
        sys.stdout.write("\r"+str(e))
        #virginica 0
    test1=[6.3,2.5,5.0,1.9]#virginica 0
    test2=[5.2,2.7,3.9,1.4]#virvicolor 1
    test3=[5.1,3.4,1.5,0.2]#virisisetro 0.5
    test1=np.array(test1).reshape(4,1)
    print(sess.run(yHO,feed_dict={x:test1}))
    test2=np.array(test2).reshape(4,1)
    print(sess.run(yHO,feed_dict={x:test2}))
    test3=np.array(test3).reshape(4,1)
    print(sess.run(yHO,feed_dict={x:test3 }))
for c in coost:
    print(c)
