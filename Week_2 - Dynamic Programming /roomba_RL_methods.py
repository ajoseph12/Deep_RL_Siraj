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

Learnings
---------
- The value iteration algo keeps improving the state values at each 
iteration, until it converges. An explicit policy isn't built at every
step we are simply working value space. Whereas in policy iteration,
at every step we create a value function which is was the value function 
for a particular policy. So policy iteration should be the way to go.


"""
import numpy as np 
import gym
import random
import time



class roomba_brute(object):


	def __init__(self, environment, action_list, num_of_policies):

		self.env = gym.make(environment)
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
			start = self.env.reset()

			for steps in range(iterations):

				action = policy[start]
				start, reward, done, info = self.env.step(action)
				total_reward += reward

				if done: break
				
		return total_reward/episodes

	
	def _random_policy(self):
		
		return np.random.choice(self.action_list, size = 16)



class roomba_value_iter(roomba_brute):


	def __init__(self, environment, theta, gamma):

		self.env = gym.make(environment)
		self.theta = theta
		#self.state_value = np.zeros((grid_h,grid_w))
		self.gamma = gamma
		self.optimal_value = self._value_iteration()
		self.optimal_policy = self._calculate_policy()
		#self.policy_score = self._evaluate_policy()

	
	def _value_iteration(self, check = 100000):

		delta = 1000
		check = 0
		value = np.zeros(self.env.env.nS)
		

		while  self.theta < delta:

			delta = 0
			prev_value = np.copy(value)

			for s in range(self.env.env.nS):
				
				q_sa = [sum([p * (r + self.gamma*prev_value[s_]) for p, s_, r, _ in 
					self.env.env.P[s][a]]) for a in range(self.env.env.nA)]
				
				value[s] = max(q_sa)
				delta = max(delta, value[s])

			check += 1 
			if check == 100000: break

		return value


	def _calculate_policy(self):

		policy = np.zeros(self.env.env.nS)
		
		for s in range(self.env.env.nS):
			action_values = np.zeros(self.env.env.nA)

			for a in range(self.env.env.nA):
				for p, s_, r, _ in self.env.env.P[s][a]:
					action_values[a] += p*(r + self.gamma*self.optimal_value[s_])

			policy[s] = np.argmax(action_values)

		return policy


	def _evaluate_policy(self, episodes = 100, iterations = 1000):

		total_reward = 0
		for episode in range(episodes):
			start = self.env.reset()

			for state in range(iterations):

				action = self.policy[start]
				start, reward, done = self.env.step(action)
				total_reward += reward

				if done: break

		return total_reward/iterations








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
	r_vi = roomba_value_iter(environment, theta, gamma)
	optimal_value = r_vi.optimal_value
	optimal_policy = r_vi.optimal_policy
	policy_score = r_vi._iterations(optimal_policy)
	endTime = time.time()
	total_time = endTime - startTime
	print("----------------- Value Iteration Method ---------------------")
	print("Policy score is %0.2f and time take is %4.2fs" %(policy_score,total_time))
	print("The optimal policy is : " + str(optimal_policy) + '\n')





                               

if __name__ == '__main__':


	environment = 'FrozenLake-v0'
	no_of_actions = 4
	action_list = [i for i in range(no_of_actions)]
	num_of_policies = 1000


	## Value Iteration
	theta = 0.00001
	gamma = 1
	main()

