class Node:
	def __init__(self, depth=0, path_cost=0, total_cost=0, state=None, parent=None, action=None):
		if state is None:
			state = []
		self.total_cost = total_cost
		self.action = action
		self.parent = parent
		self.depth = depth
		self.path_cost = path_cost
		self.state = state

	def __lt__(self, other):
		return self.path_cost < other.path_cost
