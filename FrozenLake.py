import gym
import numpy as np
import random
import time

env = gym.make('FrozenLake-v1')
num_of_episodes = 20
goal_steps = 100

for i_episode in range(num_of_episodes):
	observation = env.reset()
	for i in range(goal_steps):
		env.render()
		print(observation)
		action = env.action_space.sample()
		observation, reward, done, info = env.step(action)
		if done:
			print("Episode", i_episode, "finished after", i ,"timesteps")
			break
		time.sleep(1)
env.close()
