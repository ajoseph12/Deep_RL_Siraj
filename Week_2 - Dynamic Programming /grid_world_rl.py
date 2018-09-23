"""
Topic -- Grid World simulation using RL
Video -- https://www.youtube.com/watch?v=aAkFtRxeP7c
github -- https://github.com/colinskow/move37/tree/master/dynamic_programming

Summary
-------


To - Do
--------
- command line call
- add grid output instead of matrix
- ouput action and reward grid too
- complete summary and learnings


"""
import numpy as np 

rows, columns = (2,3)
state = np.zeros((rows+1,columns+1))
state_values = np.zeros((rows+1,columns+1))
action_values = np.zeros((rows+1,columns+1))
reward = np.zeros((rows+1,columns+1))
actions = ['L','R','U','D']
reward[0,3] = +1
reward[1,3] = -1
deny = [(0,3),(1,3),(1,1)]
gamma = 0.9


# Action_value calculation

def action_value(state, action, p_action = 0.5, p_mistake = 0.25):

	row, column = state
	up = (row, column) if (row + 1, column) == (1,1) else (min(row + 1,rows), column)
	left = (row, column) if (row, column - 1) == (1,1) else (row, max(column - 1,0))
	right = (row, column) if (row, column + 1) == (1,1) else (row, min(column + 1, columns))
	down = (row, column) if (row - 1, column) == (1,1) else (max(row - 1,0), column)

	navigation_dict = dict()
	navigation_dict['U'] = (up, left, right)
	navigation_dict['D'] = (down, left, right)
	navigation_dict['L'] = (left, up, down)
	navigation_dict['R'] = (right, up, down)

	
	temp_1, temp_2, temp_3 = navigation_dict[action]
	expected_reward = p_action*reward[temp_1] + p_mistake*reward[temp_2] + p_mistake*reward[temp_3]
	next_state_value = p_action*state_values[temp_1] + p_mistake*state_values[temp_2] + p_mistake*state_values[temp_3]
	action_value = expected_reward + gamma * next_state_value
	return action_value


# State-value calculation
theta = 0.001
delta = 1
while delta > theta:
	delta = 0 

	for i in range(rows,-1,-1):
		for j in range(columns,-1,-1):
			
			original_value = state_values[i,j]
			if (i,j) not in deny:
				
				action_values_list = list()
				for action in actions:
					state = (i,j)
					action_values_list.append((action_value(state, action),0))

				state_values[i,j], action_values[i,j] = max(action_values_list)
				diff = abs(state_values[i,j] - original_value)
				delta = max(delta, diff)

print(state_values)







