"""
Topic -- Testing Cart-Pole environment using the OpenAI gym
github -- https://github.com/kvfrans/openai-cartpole


Summary
-------
Testing the CartPole enviroment using two methods : random and hillclimb

To - Do
--------
- comment code
- complete summary and learnings
"""

import numpy as np 
import gym

def run_episode(env, param):

	obs = env.reset()
	tot_reward = 0

	for i in range(200):
		action = 0 if np.matmul(param, obs) < 0 else 1
		obs, reward, done, info = env.step(action)
		tot_reward += reward

		if done:
			#print("Survived {} number of steps".format(i+1))
			return tot_reward


def main(mode, episodes_per_update):

	env = gym.make('CartPole-v0')

	if mode == 'random':

		best_param = 0
		best_reward = 0
		
		for i in range(1000):
			param = np.random.rand(4)*2 - 1
			reward = 0  
			
			for _ in range(episodes_per_update):  
				run = run_episode(env,param)
				reward += run
			reward = reward/10
			
			if reward > best_reward:
				best_param = param
				best_reward = reward
				if reward == 200: break

	elif mode == 'hillclimb':

		noise_scaling = 0.1 
		best_param = 0
		best_reward = 0
		param = (np.random.rand(4)*2 - 1)*noise_scaling
		
		for i in range(10000):
			param = param + (np.random.rand(4)*2 - 1)*noise_scaling
			reward = 0  
			
			for _ in range(episodes_per_update):  
				run = run_episode(env,param)
				reward += run
			reward = reward/10
			
			if reward > best_reward:
				best_param = param
				best_reward = reward
				if reward == 200: break



	print(best_param, best_reward,i)


if __name__ == '__main__':
	mode = 'hillclimb'
	episodes_per_update = 100
	main(mode, episodes_per_update)
