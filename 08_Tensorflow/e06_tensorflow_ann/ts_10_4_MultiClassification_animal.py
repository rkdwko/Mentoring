import tensorflow as tf
import numpy as np
tf.set_random_seed(777)  # for reproducibility

xy = np.loadtxt('data-04-zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

nb_classes = 7  # 0 ~ 6

X = tf.placeholder(tf.float32, [None, 16])  # 0 ~ 6  shape[?,1]
Y = tf.placeholder(tf.int32, [None, 1])  # 0 ~ 6  shape[?,1]

Y_one_hot = #TODO                       # one hot.   shape[?, 1 ,7]
print("one_hot", Y_one_hot)

# One-Hot 이후에는 한차원이 더 늘어나므로 원래의 차원대로, ReShape 필요  
Y_one_hot = #TODO                       #ReShap 후 shape[?, 7]

print("reshape", Y_one_hot)

W = #TODO
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = #TODO
hypothesis = #TODO

# Cross entropy cost/loss
cost_i = tf.nn.softmax_cross_entropy_with_logits(#TODO ,

cost = #TODO

optimizer = #TODO
prediction = #TODO


correct_prediction = #TODO
accuracy =  #TODO

with tf.Session() as sess:
    # TODO

    for step in range(2000):
        # TODO
        if step % 100 == 0:
            loss, acc = sess.run([cost, accuracy], feed_dict={
                                 X: x_data, Y: y_data})
            print("Step: {:5}\t Loss: {:.3f}\t Acc: {:.2%}".format(
                step, loss, acc))


    pred = # TODO

    for p, y in zip(pred, y_data.flatten()):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))
        
