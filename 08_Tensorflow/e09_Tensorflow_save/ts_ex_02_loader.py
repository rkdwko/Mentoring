import tensorflow as tf
tf.set_random_seed(777)

sess = tf.InteractiveSession()
new_saver = tf.train.import_meta_graph('data/output_model.ckpt.meta')
new_saver.restore(sess, 'data/output_model.ckpt')

tf.get_default_graph()

x = sess.graph.get_tensor_by_name("input:0")
y = sess.graph.get_tensor_by_name("output:0")
hypothesis = sess.graph.get_tensor_by_name("hypothesis:0")
                                           #"<op_name>:<output_index>"

result = sess.run(hypothesis, feed_dict={x:[1, 2, 3]})
print(result)
#print (sess.run(x))



