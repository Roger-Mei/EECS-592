class Node:
    def __init__(self,name):
        self.name = name
        self.child = []
        self.parent = None
    
    def add_child(self, struct):
        self.child.append(struct)
    
    def add_parent(self, node):
        self.parent = node
        
class Graph():
    def __init__(self):
        self.node_list = []
        self.edge_dict = {}
        self.parent = None
        self.child = []
        self.name = None

    def add_vertex(self,struct):
        """
        The struct could either be a node or a subtree!
        """
        self.node_list.append(struct)
    def add_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.child.append(child)
        
    def add_edge(self, label, parent, child):
        self.edge_dict[parent.name, child.name] = label
        parent.add_child(child)
        child.add_parent(parent)
    
    