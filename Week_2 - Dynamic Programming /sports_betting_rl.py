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


gamma = 1 # discount factor
ph = 0.4 # probability of home team winning
num_states = 100 # number of available states
reward = [0]*101 # list for storing reward value
reward[100] = 1
theta = 0.000000001 # threshold for comparing the difference"
temp = []
value = [0]*101 # list to store value function 
policy = [0]*101 # List to store the amount of bet that gives the max reward


def reinforcement_learning():

	delta = 1
	
	while delta > theta:

		delta = 0

		for state in range(1, num_states): # Looping over all the states i.e the money in hand for a current episode

			old_val = value[state]
			bellman_equation(state)
			diff = abs(old_val - value[state])
			delta = max(diff,delta)

	
	print(value)
	print(policy)
	

def bellman_equation(state):

	optimal_action_val = 0

	for bet in range(0, min(state, 100-state)+1):

		win = state + bet
		lose = state - bet
		# action value is the sum of immediate reward + gamma(summation(prob(ss',a) * value(s')))
		# here the immediate reward depends on the end state, hence its expected value is taken
		expected_reward = ph*reward[win] + (1-ph)*reward[lose]
		expected_value = ph*value[win] + (1-ph)*value[lose]
		action_val = expected_reward + gamma * expected_value
		
		if action_val > optimal_action_val:
			
			optimal_action_val = action_val
			value[state] = action_val
			policy[state] = bet

reinforcement_learning()


# Value Plot 
plt.plot(value[:100])
plt.ylabel('State-value')
plt.xlabel('States / Capital')
plt.show()


# Policy Plot 
plt.plot(policy[:100])
plt.ylabel('Policy / Bets')
plt.xlabel('States / Capital')
plt.show()





















