"""
CS-UY 4613
Project 1: 11-Puzzle Problem

Author: Kevin Lee (KL3642)

Description: 	Implement the A* search algorithm
				with graph search for solving the 11-puzzle problem.
"""


# Standard Libraries
import sys
from heapq import heapify, heappush, heappop    # Heap data structure for priority queue

# Third-Party Libraries
import Node										# Node data structure


# Heuristic
def manhattan(curr_state, goal_state):
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

	return mdist


# Create and return a list of possible actions from given state
def expand_actions(state):
	poss_actions = []




# Expand
def expand(node):
	s = node.state




# Search
def search(ini_state, goal_state):
	# Initialize Root Node
	node = Node.Node(0, manhattan(ini_state, goal_state), ini_state)

	# Initialize frontier
	frontier = [node]
	heapify(frontier)

	# Initialize visited Hash Map
	visited = {}

	# Start Search from Frontier
	while len(frontier) > 0:
		next_node = frontier.pop()

		# If Goal Node is found
		if next_node.state == goal_state:
			return next_node

		# Expand children
		for child in expand(next_node):
			s = child.state

			# Check if already visited
			if s not in visited or child.path_cost < visited[s].path_cost:
				visited[s] = child
				heappush(frontier, child)

	return None


# Main
def main():

	# Grab filename and w from stdin
	filename = sys.argv[1]
	w = sys.argv[2]

	# Open File and parse input
	f = open(filename)
	lines = f.readlines()

	# Grab states
	ini_state = []
	goal_state = []
	count_line = 0

	for line in lines:
		if count_line >= 3:
			if count_line == 3:
				pass
			else:
				goal_state.extend([int(n) for n in line.split(' ')])
		else:
			ini_state.extend([int(n) for n in line.split(' ')])
		count_line += 1

	# Start Search
	# search(ini_state, goal_state)


if __name__ == "__main__":
	main()
