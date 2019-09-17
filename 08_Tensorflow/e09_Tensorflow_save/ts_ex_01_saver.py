import tensorflow as tf
tf.set_random_seed(777)

W = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

X = tf.placeholder(tf.float32, shape=[None], name="input")   #Restore 시 식별할 이름으로 사용될 수 있다.
Y = tf.placeholder(tf.float32, shape=[None], name="output")  #Restore 시 식별할 이름으로 사용될 수 있다.

hypothesis = X * W + b
hypothesis = tf.identity(hypothesis, "hypothesis")   #Restore 시 식별할 이름으로 사용될 수 있다.

cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

trainX = [1, 2, 3]
trainY = [5, 10, 15]

for step in range(1001):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train], feed_dict={X: trainX, Y: trainY})
    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)

saver = tf.train.Saver()
save_path = saver.save(sess, 'data/output_model.ckpt')
