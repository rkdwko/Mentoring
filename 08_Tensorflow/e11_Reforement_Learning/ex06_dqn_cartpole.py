import numpy as np
import tensorflow as tf
import random
from collections import deque
from dqn import dqn
import gym
from gym import wrappers

env = gym.make('CartPole-v0')

input_size = env.observation_space.shape[0]
output_size = env.action_space.n

dis = 0.9
REPLAY_MEMORY = 5000

def simple_replay_train(DQN, train_batch):
    x_stack = np.empty(0).reshape(0, DQN.input_size)
    y_stack = np.empty(0).reshape(0, DQN.output_size)

    # Get stored information from the buffer
    for state, action, reward, next_state, done in train_batch:
        Q = DQN.predict(state) 

        # terminal?
        if done:
            Q[0, action]   #TODO
        else:
            # Obtain the Q' values by feeding the new state through our network
            Q[0, action]   #TODO

        y_stack = np.vstack([y_stack, Q])     #학습 결과를 버퍼 스택에 쌓는다.  
        x_stack = np.vstack( [x_stack, state])

    # Train our network using target and predicted Q values on each episode
    return #TODO

def bot_play(mainDQN, env=env):
    # See our trained network in action
    state = env.reset()
    reward_sum = 0
    while True:
        env.render()
        action = np.argmax(mainDQN.predict(state))
        state, reward, done, _ = env.step(action)
        reward_sum += reward
        if done:
            print("Total score: {}".format(reward_sum))
            break

def main():
    max_episodes = 2000
    # store the previous observations in replay memory
    replay_buffer = deque()  

    with tf.Session() as sess:
        mainDQN = dqn.DQN(sess, input_size, output_size)
        tf.global_variables_initializer().run()

        for episode in range(max_episodes):
            e = 1. / ((episode / 10) + 1)
            done = False
            step_count = 0
            state = env.reset()

            while not done:
                if np.random.rand(1) < e:
                    action = env.action_space.sample()
                else:
                    # Choose an action by greedily from the Q-network
                    action = #TODO

                # Get new state and reward from environment
                next_state, reward, done, _ = env.step(action)
                if done: # Penalty
                    reward = #TODO

                # Save the experience to our buffer
                replay_buffer.append((state, action, reward, next_state, done))
                if len(replay_buffer) > REPLAY_MEMORY:
                      replay_buffer.popleft()   #버퍼에 너무 많이 쌓이면 최상단 것을 제거. 

                state = next_state
                step_count += 1
                if step_count > 10000:   # Good enough. Let's move on
                    break

            print("Episode: {} steps: {}".format(episode, step_count))

            if episode % 10 == 1: # train every 10 episode
                # Get a random batch of experiences
                for _ in range(50):
                    # Minibatch works better    # 버퍼에 있는 데이터를 랜덤하게 선택 
                    minibatch = random.sample(replay_buffer, 10)  
                    loss, _ =  #TODO

                print("Loss: ", loss)

        bot_play(mainDQN)

if __name__ == "__main__":
    main()





