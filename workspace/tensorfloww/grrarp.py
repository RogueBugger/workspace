import tensorflow as tf
import time
'''
g=tf.Graph()
with g.as_default():'''
start=time.time()
x=tf.placeholder(dtype=tf.float32,shape=(None),name='x')
w=tf.Variable(2.0,name='weight')
b=tf.Variable(0.7,name='bias')
z=w*x+b
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for t in [1.0,2.3,3.5]:
        print(f"{t}->{sess.run(z,feed_dict={x:t})}")

with tf.Session() as sess:
    sess.run(init)
    for t in [2.0,4.3,6.5]:
        print(f"{t}->{sess.run(z,feed_dict={x:t})}")
end=time.time()
print(end-start)
