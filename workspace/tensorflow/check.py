import tensorflow as tf

with tf.Session():
    x=tf.constant([[1.00,5.3],[96.7,8.7]])
    z=tf.linalg.matmul(x,x)+tf.matmul(x,[[277,863],[86366,6367]])
    result=z.eval()
    #result=sess.run(z)
    print(result)
