# Initialize reward matrix
rewards = [
	# from_state = 0
	[
		# S0   S1
		[100, 150],  # action = 0
		[120, 100]   # action = 1
	],
	# from_state = 1
	[
		# S0   S1
		[200,  50],  # action = 0
		[120,  80]   # action = 1
	],
]

# Initialize probability matrix
probabilities = [
	# from_state = 0
	[
		# S0   S1
		[0.8, 0.2],  # action = 0
		[0.2, 0.8]   # action = 1
	],
	# from_state = 1
	[
		# S0   S1
		[0.7, 0.3],  # action = 0
		[0.6, 0.4]   # action = 1
	],
]

num_states  = len(rewards)
num_actions = len(rewards[0][0])
p = [0] * num_states
beta = 0.9

def calc_r():
	r = [0] * num_states

	for i in range(num_states):
		for s in range(num_states):
			r[i] = r[i] + rewards[i][p[i]][s] * probabilities[i][p[i]][s]

	return r

def calc_v(r):
	v = [0, 0]

	v0_temp = r[0] / (1 - beta * probabilities[0][p[0]][0])
	v1_temp1 = r[1] * (1 - beta * probabilities[0][p[0]][0]) + beta * probabilities[1][p[1]][0] * r[0]
	v1_temp2 = (1 - beta * probabilities[0][p[0]][0]) * (1 - beta * probabilities[1][p[1]][1])
	v1_temp2 = v1_temp2 - beta * beta * probabilities[1][p[1]][0] * probabilities[0][p[0]][1]

	v[1] = v1_temp1 / v1_temp2
	v[0] = v0_temp + (beta * probabilities[0][p[0]][1]/(1-beta*probabilities[0][p[0]][0])) * v[1]

	return v

def calc_p():
	r = calc_r()
	v = calc_v(r)

	max_v = v.copy()
	max_p = p.copy()

	for from_state in range(num_states):
		for a in range(num_actions):
			_sum = 0
			for to_state in range(num_states):
				_prod = probabilities[from_state][a][to_state]
				_prod2 = rewards[from_state][a][to_state]
				_prod2 = _prod2 + beta * v[to_state]
				_prod = _prod * _prod2
				_sum = _sum + _prod
			if(_sum > max_v[from_state]):
				max_v[from_state] = _sum
				max_p[from_state] = a
	
	for s in range(num_states):
		if(v[s] >= max_v[s]):
			max_p[s] = p[s]

	return max_p

while(True):
	temp = calc_p()
	all_match = True

	for i in range(len(p)):
		all_match = all_match and (p[i] == temp[i])
	
	p = temp
	
	if(all_match):
		break

print('final:')
print('p:', p)
print('v:', calc_v(calc_r()))
