class Node:
	def __init__(self, depth=0, path_cost=0, state=None):
		if state is None:
			state = []
		self.depth = depth
		self.path_cost = path_cost
		self.state = state
