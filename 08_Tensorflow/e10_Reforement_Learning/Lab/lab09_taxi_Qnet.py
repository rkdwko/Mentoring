import gym
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import time

env = gym.make("Taxi-v2")
Q = np.zeros([env.observation_space.n, env.action_space.n])

input_size = env.observation_space.n
output_size = env.action_space.n
learning_rate = 0.1

X = tf.placeholder(shape=[1, input_size], dtype=tf.float32)
W = tf.Variable(tf.random_uniform([input_size, output_size], 0, 0.01))

Qpred = tf.matmul(X, W)
Y = tf.placeholder(shape=[1, output_size], dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y - Qpred))
train = tf.train.ProximalGradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

dis = .99
num_episodes = 2000

rList = []

start_time = time.time()

init = tf.global_variables_initializer()

with

for episode in range(1000 ):
	done = False
	G, reward = 0, 0
	state = env.reset()

	while done != True:
		action = np.argmax(Q[state])
		state2, reward, done, info = env.step(action)
		#Q[state, action] += dis * (reward + np.max(Q[state2]) - Q[state, action])
		Q[state, action] = dis * (reward + np.max(Q[state2])  )

		G += reward
		state = state2
		#env.render()

	if episode % 50 == 0:
		print('Episode {} Total Reward: {}'.format(episode, G))