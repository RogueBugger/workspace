import tensorflow as tf

x=tf.placeholder(dtype=tf.int32,shape=(None),name='x')
w=tf.Variable(1,name='x')
b=tf.Variable(2,name='y')
z=w*x+b

init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(z,feed_dict={x:2}))
