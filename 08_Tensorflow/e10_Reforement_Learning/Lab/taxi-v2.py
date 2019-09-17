import gym
env = gym.make("Taxi-v2")
observation = env.reset()

print (env.observation_space.n ) #총 상태 수
print (env.action_space.n )      #action 수
env.render()

for _ in range(10):
           #아무 action이나 수행하는 함수. (this takes random actions)
  action = env.action_space.sample() # your agent here

  observation, reward, done, info = env.step(action)
  print( "action",  action, "reward", reward)
  env.render()
