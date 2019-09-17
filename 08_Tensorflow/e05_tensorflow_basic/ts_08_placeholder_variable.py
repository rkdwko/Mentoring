import tensorflow as tf

X=tf.placeholder(tf.float32, [None,3]) #행?, 3열
print( X )

x_data = [ [1,2,3], [4,5,6] ]

W = tf.Variable( tf.random_normal([3,2]))
#W = tf.Variable( [[2,2],[2,2],[2,2] ] )
b = tf.Variable( tf.random_normal([2,1]))

#TODO 

sess = tf.Session()
#TODO 

print ("=== x data === ")
print (x_data)
print("=== W === ")
print(sess.run(W))
print("=== b === ")
print(sess.run(b))

#TODO 
sess.close()