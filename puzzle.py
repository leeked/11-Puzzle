"""
CS-UY 4613
Project 1: 11-Puzzle Problem

Author: Kevin Lee (KL3642)

Description: 	Implement the A* search algorithm
				with graph search for solving the 11-puzzle problem.
"""


# Standard Libraries
import sys
import copy
from heapq import heapify, heappush, heappop    # Heap data structure for priority queue

# Custom Libraries
import Node										# Node data structure


# Heuristic
def manhattan(curr_state, goal_state, w):
	mdist = 0

	# Iterate through curr_state
	for i in range(len(curr_state)):

		# Iterate through goal_state to find match
		for j in range(len(goal_state)):

			# When match is found, calculate Manhattan Distance
			if curr_state[i] == goal_state[j]:
				x1 = i // 4
				y1 = i % 4

				x2 = j // 4
				y2 = j % 4

				# Add to total mdist
				mdist += abs(x2 - x1) + abs(y2 - y1)

	return mdist * w


# Create and return a list of possible actions from given state
def expand_actions(state):
	poss_actions = []

	# Find index of blank
	ind = 0

	for i in range(len(state)):
		if state[i] == 0:
			ind = i

	# Determine possible actions
	if ind % 4 != 0:
		poss_actions.append('L')

	if ind % 4 != 3:
		poss_actions.append('R')

	if ind > 3:
		poss_actions.append('U')

	if ind < 8:
		poss_actions.append('D')

	return poss_actions


# Create new state based on action
def result(state, action):
	new_s = copy.deepcopy(state)

	# Find index of blank
	ind = 0

	for i in range(len(state)):
		if state[i] == 0:
			ind = i

	# Perform action
	if action == 'L':
		new_s[ind] = new_s[ind - 1]
		new_s[ind - 1] = 0

	elif action == 'R':
		new_s[ind] = new_s[ind + 1]
		new_s[ind + 1] = 0

	elif action == 'U':
		new_s[ind] = new_s[ind - 4]
		new_s[ind - 4] = 0

	elif action == 'D':
		new_s[ind] = new_s[ind + 4]
		new_s[ind + 4] = 0

	return new_s


# Returns all possible children of given node
def expand(parent, goal_state, w):
	s = parent.state

	# Create nodes from all possible actions
	for action in expand_actions(s):

		# Determine the attributes of each child
		new_depth = parent.depth + 1
		gn = parent.path_cost + 1
		new_s = result(s, action)
		fn = gn + manhattan(new_s, goal_state, w)

		yield Node.Node(new_depth, gn, fn, new_s, parent, action)


# Search
def search(ini_state, goal_state, w):
	# Initialize Root Node
	node = Node.Node(0, 0, manhattan(ini_state, goal_state, w), ini_state)
	total_num_nodes = 1

	# Initialize frontier
	frontier = [node]
	heapify(frontier)

	# Initialize visited Hash Map
	visited = {}

	# Start Search from Frontier
	while len(frontier) > 0:
		next_node = heappop(frontier)

		# If Goal Node is found
		if next_node.state == goal_state:
			return next_node, total_num_nodes

		# Expand children
		for child in expand(next_node, goal_state, w):
			s = child.state

			# Check if already visited
			if tuple(s) not in visited or child.total_cost < visited[tuple(s)].total_cost:
				visited[tuple(s)] = child
				heappush(frontier, child)

			total_num_nodes += 1

	return None, total_num_nodes


# Explore solution path and return actions and f(n) along the path
def find_path(node):
	sol_path = []
	fn_vals = []

	# Go up solution path while appending action to sol_path and f(n) to fn_vals until root
	curr = node
	while curr.depth != 0:
		sol_path.append(curr.action)
		fn_vals.append(str(curr.total_cost))
		curr = curr.parent

	# Include root node f(n)
	fn_vals.append(str(curr.total_cost))

	sol_path.reverse()
	fn_vals.reverse()
	return sol_path, fn_vals


# Create and write to output file
def output(ini_state, w, goal_node, num_nodes):
	f = open("output.txt", 'a')

	# Write initial state
	for i in range(len(ini_state)):
		f.write(str(ini_state[i]))
		if i % 4 != 3:
			f.write(' ')
		else:
			f.write('\n')

	f.write('\n')

	# Write goal state
	for i in range(len(goal_node.state)):
		f.write(str(goal_node.state[i]))
		if i % 4 != 3:
			f.write(' ')
		else:
			f.write('\n')

	f.write('\n')

	# Write w
	f.write(str(w) + '\n')

	# Write depth of shallowest goal node
	if goal_node is None:
		f.write("FAIL\n")
	else:
		f.write(str(goal_node.depth) + '\n')

	# Write the total number of nodes generated
	f.write(str(num_nodes) + '\n')

	# Write the solution (sequence of actions and f(n) values)
	if goal_node is None:
		f.write("FAIL\nFAIL")
	else:
		sol_path, fn_vals = find_path(goal_node)
		for i in range(len(sol_path)):
			f.write(sol_path[i])
			if i < len(sol_path) - 1:
				f.write(' ')

		f.write('\n')

		for i in range(len(fn_vals)):
			f.write(fn_vals[i])
			if i < len(fn_vals) - 1:
				f.write(' ')

	f.close()


# Main
def main():

	# Grab filename and w from stdin
	filename = sys.argv[1]
	w = float(sys.argv[2])

	# Open File and parse input
	f = open(filename)
	lines = f.readlines()

	# Grab states
	ini_state = []
	goal_state = []
	count_line = 0

	for line in lines:
		if count_line >= 3:
			goal_state.extend([int(n) for n in line.split(' ') if n != '\n'])
		else:
			ini_state.extend([int(n) for n in line.split(' ') if n != '\n'])
		count_line += 1

	f.close()
	
	# Start Search
	res, num_nodes = search(ini_state, goal_state, w)

	# Create and write to output
	output(ini_state, w, res, num_nodes)


if __name__ == "__main__":
	main()
