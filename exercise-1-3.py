# Initialize reward matrix
rewards = [
	# from_state = 0
	[
		# S0  S1   S2
		[100, 50, 150],  # action = 0
		[50,  50, 100]   # action = 1
	],
	# from_state = 1
	[
		#S0    S1   S2
		[50,  100, 200],  # action = 0
		[100, 150,  50]   # action = 1
	],
	# from_state = 2
	[
		# S0   S1   S2
		[100, 200,  50],  # action = 0
		[100, 150,  50]   # action = 1
	]
]

# Initialize probability matrix
probabilities = [
	# from_state = 0
	[
		# S0   S1   S2
		[0.2, 0.5, 0.3],  # action = 0
		[0.5, 0.2, 0.3]   # action = 1
	],
	# from_state = 1
	[
		# S0   S1   S2
		[0.3, 0.6, 0.1],  # action = 0
		[0.3, 0.2, 0.5]   # action = 1
	],
	# from_state = 2
	[
		# S0   S1   S2
		[0.2, 0.2, 0.6],  # action = 0
		[0.7, 0.1, 0.2]   # action = 1
	]
]

def optimize(num_periods,
	         beta,
	         num_states = len(rewards)):
	
	# Using nested loops
	stored_results = []
	
	for _ in range(num_states):
		inner_list = [None] * num_periods
		stored_results.append(inner_list)
	
	def V(x_t, t):
		action_1_reward = expected_reward(x_t, 0, t)
		action_2_reward = expected_reward(x_t, 1, t)
		
		stored_results[x_t][t] = max(action_1_reward, action_2_reward)
		
		if(action_1_reward > action_2_reward):
			print("Period:", t + 1, "State:", x_t + 1, "Optimal action: Action 1")
		elif(action_2_reward > action_1_reward):
				print("Period:", t + 1, "State:", x_t + 1, "Optimal action: Action 2")
		else:
			print("Period:", t + 1, "State:", x_t + 1, "Optimal action: Equal")
		return stored_results[x_t][t]
	
	def expected_reward(current_state, action, t):
		sum = 0
		for s in range(num_states):
			sum = (sum +
				probability(s, current_state, action) *
				(reward(current_state, action, s) +
				beta * get_stored_result(s, t+1))
				)
		return sum
	
	def get_stored_result(s, t):
		return_val = 0
		
		try:
			return_val = stored_results[s][t]
		finally:
			return return_val
	
	def reward(from_state, action, to_state):
		return rewards[from_state][action][to_state]

	def probability(to_state, from_state, action):
		return probabilities[from_state][action][to_state]
	
	for t in range(num_periods - 1, -1, -1):
		for s in range(num_states):
			print(V(s, t))

optimize(num_periods=4, beta=0.9)
