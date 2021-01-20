import csv
import math

class Problem:
    def __init__(self, set_problem):
        self.initial_state = set_problem[0][0]
        self.goal = set_problem[1][0]
        self.search_type = set_problem[2][0]
        self.solution = []
        distance_list = self.read_csv('transition_set.txt')
        self.my_graph = Problem.Graph()
        for edge in distance_list:
            self.my_graph.add_edge(edge[0], edge[1], edge[2])
        coords_list = self.read_csv('latlon_coords.txt')
        R = 3959
        self.ECEF_coords = {}
        for i in range(0, len(coords_list)):
            phi = float(coords_list[i][1]) * 2 * math.pi / 360
            theta = coords_list[i][2] * 2 * math.pi / 360
            x = math.cos(phi) * math.cos(theta) * R
            y = math.cos(phi) * math.sin(theta) * R
            z = math.sin(phi) * R
            self.ECEF_coords[coords_list[i][0]] = [x, y, z]

    class Vertex:
        def __init__(self, key):
            self.key = key
            self.connections = {}

        def add_neighbor(self, nbr, weight=0):
            self.connections[nbr] = weight

        def get_connections(self):
            return self.connections.keys()

    class Graph:
        def __init__(self):
            self.adjalist = {}
            self.num_vertices = 0
            self.num_edges = 0

        def add_vertex(self, key):
            self.adjalist[key] = Problem.Vertex(key)
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

    def successor_fn(self, state):
        action_result_list = []
        for neighbor in self.my_graph.adjalist[state].connections:
            action_result = [neighbor, neighbor.key]
            action_result_list.append(action_result)
        return action_result_list

    def step_cost(self, state, action):
        return self.my_graph.adjalist[state].connections[action]

    def heuristic_cost(self, result):
        x_goal = self.ECEF_coords[self.goal][0]
        y_goal = self.ECEF_coords[self.goal][1]
        z_goal = self.ECEF_coords[self.goal][2]
        x_result = self.ECEF_coords[result][0]
        y_result = self.ECEF_coords[result][1]
        z_result = self.ECEF_coords[result][2]
        return math.sqrt((x_goal - x_result)**2 + (y_goal - y_result)**2 + (z_goal - z_result)**2)

    def goal_test(self, state):
        return state == self.goal

    def get_solution(self, node):
        if node.depth != 0:
            self.get_solution(node.parent)
        self.solution.append(node.state)
        return self.solution

    def print_solution(self):
        print('Solution:', '->'.join(self.solution))

    def read_csv(self, filename):
        """
        Read CSV file from input file path
        """
        table = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
            for row in reader:
                line = []
                line.append(row[0])
                line.append(row[1])
                line.append(float(row[2]))
                table.append(line)
        return table
