"""
CS-UY 4613
Source Code for Project 1: 11-Puzzle Problem

Author: Kevin Lee (KL3642)

Description: This is the Node data structure used in the project.
"""


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
        return self.total_cost < other.total_cost

    def __repr__(self):
        return "depth = % s , path_cost = % s , total_cost = % s , state = % s , action = % s" % (
            self.depth, self.path_cost,
            self.total_cost, self.state, self.action)
