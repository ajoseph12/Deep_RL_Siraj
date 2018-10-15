"""
Topic -- Guiding Roomba through grid world 
Link -- https://www.theschool.ai/wp-content/uploads/2018/09/policy_and_value_iteration.pdf
Gym environment -- https://gym.openai.com/envs/FrozenLake-v0/

Summary
-------
In this programming exercie we are going to help 'Roomba' get across the grid
keeping in mind the rewards - maximum reward - and time - minimum time. Following
would be the methods employed to perform the same:
- Brute Force
- 


To - Do
--------
- Define environment
- Define many policies 
- Each policy ought to be tested for 'e' episodes to get avg success
- 

MSC information 
---------------

Actions:
	LEFT = 0
	DOWN = 1
	RIGHT = 2
	UP = 3

Policy : a list of length 16 indicating the action to be taken when on a 
given position on the grid.







	main()
"""
import numpy as np 
import gym
import random
import time

class roomba_brute(object):


	def __init__(self, environment, action_list, num_of_policies):

		self.environment = gym.make(environment)
		self.action_list = action_list
		self.policies = [list(self._random_policy()) for i in range(num_of_policies)]
		self.avg_rewards = list()
	
	@property
	def brute(self):

		total_reward = 0

		for policy in self.policies:
			self.avg_rewards.append(self._iterations(policy))

		return max(self.avg_rewards), self.policies[self.avg_rewards.index(max(self.avg_rewards))]


	def _iterations(self, policy, episodes = 100, iterations = 100):

		total_reward = 0
		for i in range(episodes):
			start = self.environment.reset()

			for steps in range(iterations):

				action = policy[start]
				start, reward, done, info = self.environment.step(action)
				total_reward += reward

				if done: break
				
		return total_reward/episodes

	
	def _random_policy(self):
		
		return np.random.choice(self.action_list, size = 16)





def main():

	r = roomba_brute(environment, action_list, num_of_policies)
	max_reward, best_policy = r.brute
	print(max_reward, best_policy)
	



if __name__ == '__main__':

	environment = 'FrozenLake-v0'
	no_of_actions = 4
	action_list = [i for i in range(no_of_actions)]
	num_of_policies = 1000

	main()

"""

env = gym.make('FrozenLake-v0')
policy = np.random.choice([0,1,2,3], size = 16)
print(policy)
total_reward = 0
for e in range(10000):

	obs = env.reset()
	
	for p in policy:
		action = p
		obs, reward, done, info = env.step(action)

		if done: break

	total_reward += reward

print(total_reward, e) 


totalReward = 0

env = gym.make('FrozenLake-v0')


policies = [list(np.random.choice(4, size = 16)) for i in range(1000)]
totalReward = list()
for policy in policies:
	
	total_reward = 0 

	for e in range(100):
		start = env.reset()

		for t in range(100):
			#print(start)
			action = policy[start]
			start, reward, done, _ = env.step(action)
			total_reward += reward

			if done:break

	totalReward.append(total_reward)
		#print(totalReward, policy, t)

print(max(totalReward))

"""








