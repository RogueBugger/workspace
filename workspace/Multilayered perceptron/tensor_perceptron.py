import tensorflow as tf
from random import shuffle
import random,numpy as np





def guess(inputs):



dataset=[[[1,0],1],
         [[0,0],0],
         [[0,1],1],
         [[1,1],1]
]
x=tf.placeholder(dtype=tf.int32)

for _ in range(1):
    shuffle(dataset)
    for data in dataset:
        #data=np.array([data])
        guess(data[0])
