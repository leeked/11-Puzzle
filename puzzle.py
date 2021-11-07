# Standard Libraries
import sys	
from heapq import heapify, heappush, heappop	# Heap data structure for priority queue			

# Third-Party Libraries
import Node										# Node data structure


# Heuristic
def manhattan(state):
	pass


# Expand
def expand():
	pass


# Search
def search(ini_state, goal_state):
	# Initialize Root Node
	node = Node.Node(0, manhattan(ini_state), ini_state)

	# Initialize frontier
	frontier = [node]
	heapify(frontier)

	# Initialize Visited Hash Map
	visited = {}

	# Start Search from Frontier
	while len(frontier) > 0:
		next_node = frontier.pop()

		# If Goal Node is Found
		if next_node.state == goal_state:
			return next_node

		# Expand Children
		for child in expand(next_node):
			s = child.state

			if s not in visited or child.path_cost < visited[s].path_cost:
				visited[s] = child
				heappush(frontier, (child.path_cost, child))


# Main
def main():

	# Grab filename and w from stdin
	filename = sys.argv[1]
	w = sys.argv[2]

	# Open File and Parse Input
	f = open(filename)
	lines = f.readlines()

	# Grab States
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
	search(ini_state, goal_state)


if __name__ == "__main__":
	main()
