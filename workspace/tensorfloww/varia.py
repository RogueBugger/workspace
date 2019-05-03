import tensorflow as tf
print("heello")
x=5
a=tf.Variable(tf.random_normal([x,6]))
init=tf.global_variables_initializer ()
sess=tf.Session()
sess.run(init)
print(sess.run(a))
print(x)
