import tensorflow as tf

a = tf.constant(100, name="a")
b = tf.constant(200, name="b")
c = tf.constant(300, name="c")
v = tf.Variable(tf.float32, name="v")

calc_op = a + b * c
assign_op = tf.assign(v, calc_op)

sess= tf.Session()
sess.run(tf.global_variables_initializer())

#TODO 

sess.run(assign_op)
print( sess.run( v ) )