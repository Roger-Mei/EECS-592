import csv

# Node Construction
class Node:
    def __init__(self, name):
        self.name = name
        self.parent = []
        self.child = []
        self.evidence = {}
        self.value = ['T', 'F']
        self.specific_value = None

# Graph Construction
class Graph:
    def __init__(self):
        self.node_dict = {}
        self.edges_lib = {}
        self.Var = []

    def add_node(self, node):
        if isinstance(node, Node) and node.name not in self.node_dict:
            self.node_dict[node.name] = node 
    
    def add_Var(self):
        for key in self.node_dict:
            self.Var.append(self.node_dict[key])
