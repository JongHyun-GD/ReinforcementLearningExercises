import gym
import numpy as np
import random
import time

env = gym.make('FrozenLake-v1') # FronzenLake 환경을 구성한다.
num_of_episodes = 20 # 훈련을 위해 수행할 에피소드의 수
goal_steps = 100 # 한 에피소드당 최대 취할 수 있는 행동의 개수
variety_of_action = 4	# 취할 수 있는 액션의 가지 수
						# 좌=0,하=1,우=2,상=3 

for i_episode in range(num_of_episodes):
	# Reset environment
	observation = env.reset()

	for i in range(goal_steps):
		if i == 0:
			action = np.random.randint(variety_of_action)
		else:

		
		observation, reward, done, info = env.step(action)
		if done:
			print("Episode", i_episode, "finished after", i ,"timesteps")
			break


env.close()
