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
	node = Node.Node(0, manhattan(ini_state), ini_state)


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

	print(ini_state)
	print(goal_state)


if __name__ == "__main__":
	main()
