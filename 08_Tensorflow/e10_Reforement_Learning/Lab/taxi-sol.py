import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("Taxi-v2")
observation = env.reset()

print (env.observation_space.n ) #총 상태 수
print (env.action_space.n )      #action 수

# Q를 모두 0으로 초기화.  Q[16,4]
Q = np.zeros([env.observation_space.n, env.action_space.n])

#  learning parameters
num_episodes = 4000

# create lists to contain total rewards and steps per episode
rList = []
env.render()
for i in range(num_episodes): # 여러번 반복 학습
    state = env.reset()   # 환경 reset 후, 첫번째 상태 얻음
    rAll = 0
    done = False

    # The Q-Table learning algorithm
    while not done:
        #현재 state의 Q중 최대 reward를 얻을 수 있는 action을 구함.
        #단, 알려진 길로만 가지 않기 위해서 random 값 add.
        # 학습 후반 부로 갈 수로 random 값의 영향을 적게 하기위해   random/(i+1)
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n)/(i+1))

         # 환경에서 action 후, new_state와 reward를 얻음
        new_state, reward, done, _ = env.step(action)

        # Update Q-Table with new knowledge using decay rate
        Q[state, action] = reward +  np.max(Q[new_state, :])

        rAll += reward
        state = new_state
        env.render()
        print( "action",  action, "reward", reward)
    rList.append(rAll)

print("Success rate: " + str(sum(rList) / num_episodes))
print("Final Q-Table Values")
print("LEFT DOWN RIGHT UP")
#print(Q)
plt.bar(range(len(rList)), rList, color='b', alpha=0.4)
plt.show()

"""
env.render()

for _ in range(10):
           #아무 action이나 수행하는 함수. (this takes random actions)
  action = env.action_space.sample() # your agent here

  observation, reward, done, info = env.step(action)
  print( "action",  action, "reward", reward)
  env.render()
"""
