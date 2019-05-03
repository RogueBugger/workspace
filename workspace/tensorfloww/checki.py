import tensorflow as tf
import numpy as np
from random import shuffle
import time,sys,random


x=tf.Variable(tf.random_normal([2,2]))
sess=tf.Session()
sess.run(tf.global_variables_initializer())
print(x)
print(sess.run(x))
