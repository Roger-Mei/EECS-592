import sys
import csv
import math
import collections
from tsp_domain import Problem

global num_nodes
num_nodes = 0

class Node:
    """
    Definition of node structure
    """
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        if parent == None:
            self.depth = 0
        else:
            self.depth = parent.depth + 1

class Queue(collections.deque):
    def insert_all(self, node_set):
        self.extend(node_set)

    def remove_first(self):
        return self.popleft()

    def check_empty(self):
        return len(self) == 0

class Stack(collections.deque):
    def insert_all(self, node_set):
        node_set.reverse()
        self.extend(node_set)

    def remove_first(self):
        return self.pop()

    def check_empty(self):
        return len(self) == 0

class PriorityQueue(collections.deque):
    def insert_all(self, node_set):
        self.extend(node_set)
        quicksort(self, 0, len(self)-1)

    def remove_first(self):
        return self.popleft()

    def check_empty(self):
        return len(self) == 0

def expand(specific_problem, parent):
    successors = []
    for [action, result] in specific_problem.successor_fn(parent.state):
        if specific_problem.search_type == 'A':
            child_cost = parent.path_cost + specific_problem.step_cost(parent.state, action) + specific_problem.heuristic_cost(result)
            if parent.parent != None:
                child_cost -= specific_problem.heuristic_cost(parent.state)
        else:
            child_cost = parent.path_cost + specific_problem.step_cost(parent.state, action)
        child = Node(result, parent, action, child_cost)
        successors.append(child)
    return successors

def BDUA_search(specific_problem):
    global num_nodes
    closed_list = []
    if specific_problem.search_type == 'B':
        frontier = Queue()
    if specific_problem.search_type == 'D':
        frontier = Stack()
    else:
        frontier = PriorityQueue()
    root_node = Node(specific_problem.initial_state, None, None, 0)
    frontier.append(root_node)
    while True:
        if frontier.check_empty():
            return ['failure', num_nodes]
        new_node = frontier.remove_first()
        if specific_problem.goal_test(new_node.state):
            return [specific_problem.get_solution(new_node), num_nodes, new_node.path_cost]
        if new_node.depth > 15:
            print('The depth limit value reached!')
            return ['failure', num_nodes]
        if new_node.state not in closed_list:
            closed_list.append(new_node.state)
            frontier.insert_all(expand(specific_problem, new_node))
            num_nodes += 1

def depth_limited_search(specific_problem, depth_limit):
    root_node = Node(specific_problem.initial_state, None, None, 0)
    return recursive_DLS(root_node, specific_problem, depth_limit)

def recursive_DLS(node, specific_problem, depth_limit):
    global num_nodes
    cutoff_occurred = False
    if specific_problem.goal_test(node.state):
        return node
    if node.depth == depth_limit:
        return 'cutoff'
    num_nodes += 1
    for successor in expand(specific_problem, node):
        result = recursive_DLS(successor, specific_problem, depth_limit)
        if result == 'cutoff':
            cutoff_occurred = True
        elif result != 'failure':
            return result
    if cutoff_occurred:
        return 'cutoff'
    else:
        return 'failure'

def iterative_deepening_search(specific_problem):
    global num_nodes
    for depth_limit in range(0, 16):
        result = depth_limited_search(specific_problem, depth_limit)
        if result != 'cutoff':
            if result == 'failure':
                return [result, num_nodes]
            else:
                return [specific_problem.get_solution(result), num_nodes, result.path_cost]
    print('The depth limit value reached!')
    return ['failure', num_nodes]

def quicksort(my_list, start, end):
    if start >= end:
        return
    p = partition(my_list, start, end)
    quicksort(my_list, start, p-1)
    quicksort(my_list, p+1, end)

def partition(my_list, start, end):
    pivot = my_list[end]
    i = start
    for j in range(start, end):
        if my_list[j].path_cost < pivot.path_cost:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            i += 1
    my_list[i], my_list[end] = my_list[end], my_list[i]
    return i

def read_specific_problem(filename):
    """
    Read CSV file from input file path
    """
    table = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
        for row in reader:
            table.append(row)
    return table

def main():
    set_problem = read_specific_problem('tsp.txt')
    specific_problem = Problem(set_problem)
    if specific_problem.search_type == 'I':
        search_result = iterative_deepening_search(specific_problem)
    else:
        search_result = BDUA_search(specific_problem)
    print('Total number of nodes expanded:', search_result[1])
    if search_result[0] != 'failure':
        specific_problem.print_solution()
        print('Total solution cost:', search_result[2])
    else:
        print('Failure! No solution found!')

main()
