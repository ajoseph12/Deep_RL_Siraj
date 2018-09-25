"""
Topic -- Sports Betting using Reinforcement Learning
Video -- https://www.youtube.com/watch?time_continue=193&v=mEIePvxdbkQ
github -- https://github.com/llSourcell/sports_betting_with_reinforcement_learning

Summary
-------
A gambler has the opportunity to win bets based on the outcome of a sequence of coin flips. If the coin comes up head he wins the
amount he staked, else he loses it. The game ends when either the gambler wins a total of 100$ or loses all of his capital.
On each flip, the gambler must decide as to what portion of his capital must he stake. The problem can be formulated as an undiscounted 
(gamma = 1) episodic finite MDP. The state s is the gambler's capital (s = (1,2,...,99)) and the action are stakes, 
a = (1,2,..,min(s,100-s)). 

- The reward is 0 on all transitions, except when the gambler reaches his goal when it's +1. 
- The stat-value function gives the probability of winning from each state. 
- A policy is a mapping from levels of capital to stakes.
- The optimal policy maximises the probability of reaching the goal (100$).

Let ph be the probability of a coin coming up heads, If ph is known, then the entire problem is known and it can be solved, 
for instance, by Value Iteration. Here, Value Iteration will be used for Sports Betting. It helps generate v* (optimal value function) 
and pi* (optimal policy function)

Learnings
---------
While the Value Iteration (Dynamic Programming Algorithm) does help one arrive at an optimal policy, one can't use it
with events having numerous states - it could prove to be computationally expensive - or an imperfect environment model . 
Neverthless a useful thought exercise.

"""

import matplotlib.pyplot as plt


class sports_bet(object):


	def __init__(self, gamma, num_states, theta, ph, plot = False):

		self.gamma = gamma # discount factor
		self.num_states = num_states # number of available states
		self.theta = theta # threshold for comparing the difference of state values calculated"
		self.ph = ph # probability of home team winning
		
		self.reward = [0]*(self.num_states+1) # list for storing reward value
		self.reward[100] = 1

		self.value = [0]*(self.num_states+1) # list to store value function 
		self.policy = [0]*(self.num_states+1) # List to store the amount of bet that gives the max reward

		self._reinforcement_learning()

		if plot == True : self._plot()

	

	def _reinforcement_learning(self):

		delta = 1
		
		while delta > self.theta:

			delta = 0

			for state in range(1, self.num_states): # Looping over all the states i.e the money in hand for a current episode

				old_val = self.value[state]
				self._bellman_equation(state)
				diff = abs(old_val - self.value[state])
				delta = max(diff,delta)

		
		print(self.value)
		print(self.policy)
		

	
	def _bellman_equation(self, state):

		optimal_action_val = 0

		for bet in range(0, min(state, 100-state)+1):

			win = state + bet
			lose = state - bet
			# action value is the sum of immediate reward + gamma(summation(prob(ss',a) * value(s')))
			# here the immediate reward depends on the end state, hence its expected value is taken
			expected_reward = self.ph*self.reward[win] + (1-self.ph)*self.reward[lose]
			expected_value = self.ph*self.value[win] + (1-self.ph)*self.value[lose]
			action_val = expected_reward + gamma * expected_value
			
			if action_val > optimal_action_val:
				
				optimal_action_val = action_val
				self.value[state] = action_val
				self.policy[state] = bet

	

	def _plot(self):

		# Value Plot 
		plt.plot(self.value[:100])
		plt.ylabel('State-value')
		plt.xlabel('States / Capital')
		plt.show()


		# Policy Plot 
		plt.plot(self.policy[:100])
		plt.ylabel('Policy / Bets')
		plt.xlabel('States / Capital')
		plt.show()




def main(gamma, num_states, theta, ph, plot):

	bet = sports_bet(gamma, num_states, theta, ph, plot)


if __name__ == '__main__':

	gamma = 1 # discount factor
	num_states = 100 # number of available states
	theta = 0.000000001 # threshold for comparing the difference of state values calculated"
	ph = 0.4 # probability of home team winning
	plot = True
	
	main(gamma, num_states, theta, ph, plot)













