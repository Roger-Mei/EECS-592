class vertex(object):
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def add_neighbor(self, nbr, weight=0):
        self.connections[nbr] = weight

    def get_connections(self):
        return self.connections.keys()

class graph(object):
    def __init__(self):
        self.adjalist = {}
        self.num_vertices = 0
        self.num_edges = 0

    def add_vertex(self, key):
        self.adjalist[key] = vertex(key)
        self.num_vertices += 1

    def add_edge(self, key1, key2, weight=0):
        if key1 not in self.adjalist:
            self.add_vertex(key1)
        if key2 not in self.adjalist:
            self.add_vertex(key2)
        self.adjalist[key1].add_neighbor(self.adjalist[key2], weight)
        self.adjalist[key2].add_neighbor(self.adjalist[key1], weight)
        self.num_edges += 1

    def get_vertices(self):
        return self.adjalist.keys()

    #show neighbors of each vertex in iteration
    def __iter__(self):
        return iter(self.adjalist.values())

my_list = []
f = open('graph.txt')
while True:
    lines = f.readlines(10000)
    if not lines:
        break
    for line in lines:
        myline = line.split(', ')
        my_list.append(myline)
f.close()

my_graph = graph()
for edge in my_list:
    edge[2] = int(edge[2])
    my_graph.add_edge(edge[0], edge[1], edge[2])

print('The number of vertices =', my_graph.num_vertices)
print('The number of edges =', my_graph.num_edges)
