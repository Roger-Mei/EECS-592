import csv
import math

class Problem:
    def __init__(self, set_problem):
        distance_list = self.read_csv('transition_set.txt')
        self.my_graph = Problem.Graph()
        for edge in distance_list:
            self.my_graph.add_edge(edge[0], edge[1], edge[2])
        initial_visited = {}
        for city in self.my_graph.adjalist.keys():
            initial_visited[city] = 0
        initial_visited[set_problem[0][0]] = 1
        self.initial_state = [set_problem[0][0], initial_visited]
        self.goal = {}
        for city in self.my_graph.adjalist.keys():
            self.goal[city] = 1
        self.search_type = set_problem[1][0]
        self.solution = []

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
            self.min_weight = float('inf')

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
            if weight < self.min_weight:
                self.min_weight = weight

        def get_vertices(self):
            return self.adjalist.keys()

    def successor_fn(self, state):
        action_result_list = []
        for neighbor in self.my_graph.adjalist[state[0]].connections:
            current_visited = state[1].copy()
            current_visited[neighbor.key] = 1
            action_result = [neighbor, [neighbor.key, current_visited]]
            action_result_list.append(action_result)
        return action_result_list

    def step_cost(self, state, action):
        return self.my_graph.adjalist[state[0]].connections[action]

    def heuristic_cost(self, result):
        num_unvisited = 0
        for city in result[1].keys():
            if result[1][city] == 0:
                num_unvisited += 1
        return num_unvisited * self.my_graph.min_weight

    def goal_test(self, state):
        return state[1] == self.goal

    def get_solution(self, node):
        if node.depth != 0:
            self.get_solution(node.parent)
        self.solution.append(node.state[0])
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

