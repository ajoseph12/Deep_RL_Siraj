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
- Value Iteration


To - Do
--------
- Value iterations

MSC information 
---------------

Actions:
	LEFT = 0
	DOWN = 1
	RIGHT = 2
	UP = 3

Policy : a list of length 16 indicating the action to be taken when on a 
given position on the grid.



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



class roomba_value_iter(object):


	def __init__(self, environment, theta, gamma):

		self.env = gym.make(environment)
		self.theta = theta
		self.state_value = np.zeros((grid_h,grid_w))
		self.gamma = gamma
		#self.optimalvalue = self._value_iteration()


	@property
	def value_iteration(self):

		delta = 1000
		check = 0
		value = np.zeros(self.env.env.nS)

		while  self.theta < delta:

			delta = 0
			prev_value = np.copy(value)

			for s in range(self.env.env.nS):
				
				q_sa = [sum([p*(r + prev_value[s_]) for p, s_, r, _ in 
					self.env.env.P[s][a]] for a in range(env.env.nA))]
				value[s] = max(q_sa)
				delta = max(delta, value[s])

		return value


	@staticmethod
	def calculate_policy(value):

		policy = np.zeros(self.env)


			
			


		for i in range(episodes):
			start = self.environment.reset()







	def _bellman_optimality_equation(self,)





def main():

	
	startTime = time.time()
	r = roomba_brute(environment, action_list, num_of_policies)
	max_reward, best_policy = r.brute
	endTime = time.time()
	total_time = endTime - startTime
	print("----------------- Brute Force Method ---------------------")
	print("Best score is %0.2f and time take is %4.2fs" %(max_reward,total_time))
	print("Best policy is : " + str(best_policy) + '\n')

	
	startTime = time.time()
	r_vi = roomba_value_iter(environment, theta, grid_h, grid_w, gamma)
	optimalvalue = r_vi.value_iteration
	policy = r_vi.





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








