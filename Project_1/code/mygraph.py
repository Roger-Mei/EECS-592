import numpy as np
import math

"""
Define Node class
"""
class Node:
    def __init__(self,name):
        self.name = name
        self.nbr_dict = {} # neighbour dictionary
        self.f = 0 # total cost
        self.g = 0 # path cost
        self.h = 0 # heuristic cost 
        self.parent = None
        self.depth = None
        self.tsp_explored_city = {} # This is set for TSP problem
        self.tsp_target_child = None
        self.tsp_cost_list = []
        self.tsp_target_list = []

    def add_nbr(self, nbr, distance):
        self.nbr_dict[nbr.name] = distance

    def add_coordinate(self, x, y, z):
        self.x_coordinate = x
        self.y_coordinate = y
        self.z_coordinate = z

"""
Define Graph class
"""
class Graph:
    def __init__(self):
        self.node_dict = {}
        self.edges_lib = {}
        self.num_nodes = 0
        self.num_edges = 0

    def add_node(self, node):
        if isinstance(node, Node) and node.name not in self.node_dict:
            self.num_nodes += 1
            self.node_dict[node.name] = node # Note that the value of the key is a Node!

    def add_edge(self, node1, node2, distance):
        if node1.name in self.node_dict and node2.name in self.node_dict:
            self.num_edges += 1
            for key, value in self.node_dict.items():
                if key == node1.name:
                    value.add_nbr(node2,distance)
                if key == node2.name:
                    value.add_nbr(node1,distance)
            return True
        else:
            return False

    def graph_printer(self):
        print('The numbr of edges:', self.num_edges)
        print('The number of nodes:', self.num_nodes)
    