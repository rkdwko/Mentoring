import gym
from gym.envs.registration import register
import numpy as np
import matplotlib.pyplot as plt
import time
import tensorflow as tf

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False}
)  

env = gym.make('FrozenLake-v3')

input_size = env.observation_space.n  #상태 총 개수 - 16개
output_size = env.action_space.n #action 총 수 - 4개(상하좌우)
learning_rate = 0.1

X = tf.placeholder(shape=[1, input_size], dtype=tf.float32) # state input
W = tf.Variable(tf.random_uniform([input_size, output_size], 0, 0.01))   # weight

Qpred = tf.matmul(X, W)       # Out Q prediction  1행16열 * 16행4열 --->  1행 4열
Y = tf.placeholder(shape=[1, output_size], dtype=tf.float32)    # Y label

loss = tf.reduce_sum(tf.square(Y-Qpred))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

# Set Q-learning parameters
dis = .99
num_episodes = 2000

# create lists to contain total rewards and steps per episode
rList = []

def one_hot(x):  #X 값을 one hot 인코딩합니다.
    return np.identity(16)[x:x+1]

start_time = time.time()

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(num_episodes):
        s = env.reset()
        e = 1. / ((i / 50) + 10)
        rAll = 0
        done = False
        local_loss = []

        while not done:
            Qs = sess.run(Qpred, feed_dict={X: one_hot(s)})
            if np.random.rand(1) < e:
                a = env.action_space.sample()
            else:
                a = np.argmax(Qs)

            s1, reward, done, _ = env.step(a)
            if done:
                Qs[0, a] = reward
            else:
                Qs1 = sess.run(Qpred, feed_dict={X: one_hot(s1)})
                # Update Q
                Qs[0, a] = reward + dis * np.max(Qs1)

            sess.run(train, feed_dict={X: one_hot(s), Y: Qs})

            rAll += reward
            s = s1

        rList.append(rAll)

print("--- %s seconds ---" % (time.time() - start_time))
print("Success rate: " + str(sum(rList) / num_episodes))
plt.bar(range(len(rList)), rList, color='b', alpha=0.4)
plt.show()