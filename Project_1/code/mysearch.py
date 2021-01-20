import csv
import math
import mygraph
from functionfile import *

"""
Define Main function
"""
def mysearch(obj):

    """
    Read the CSV files
    """
    f = open('route_planning.txt', 'r')
    reader1 = csv.reader(f)
    g = open('coordinate_map.txt', 'r')
    reader2 = csv.reader(g)

    """
    Construct Graph and Node
    """
    graph = mygraph.Graph()

    for row in reader1:
        node1 = mygraph.Node(row[0])
        node2 = mygraph.Node(row[1])
        dist = float(row[2])
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_edge(node1, node2, dist)

    R = 3959 # Radious of earth
    for row in reader2:
        temp_city = graph.node_dict[row[0]] # Note that temp_city is now a node!
        phi = math.radians(float(row[1]))
        theta = math.radians(float(row[2]))
        x = math.cos(phi) * math.cos(theta) * R
        y = math.cos(phi) * math.sin(theta) * R
        z = math.sin(phi) * R
        temp_city.add_coordinate(x,y,z)

    """
    Problem Construction
    """
    if obj == 'route.txt':
        flag = 0 # Indicator: if flag is 0, we are solving route_planning problem
        h = open(obj, 'r')
        reader3 = csv.reader(h)
        command_list = []
        for row in reader3:
            command_list.append(row[0])
        set_origin = str(command_list[0])
        set_terminal = str(command_list[1])
        search_mode = str(command_list[2])
        return mysearch_route(set_origin, set_terminal, graph, search_mode, flag)
    if obj == 'tsp.txt':
        print(222)
        flag = 1 # Indicator: if flag is 1, we are solving TSP problem
        h = open(obj, 'r')
        reader4 = csv.reader(h)
        command_list = []
        for row in reader4:
            command_list.append(row[0])
        set_origin = str(command_list[0])
        search_mode = str(command_list[1])
        set_terminal = str(None)
        return mysearch_route(set_origin, set_terminal, graph, search_mode, flag)

"""
Define route search function
"""
def mysearch_route(set_origin, set_terminal, graph, search_mode, flag):
    if search_mode == 'B':
        return breadth_first_search(set_origin, set_terminal, graph, flag)
    if search_mode == 'D':
        return depth_first_search(set_origin, set_terminal, graph, flag)
    if search_mode == 'I':
        return iterative_deepening_search(set_origin, set_terminal, graph, flag)
    if search_mode == 'U':
        return uniform_cost_search(set_origin, set_terminal, graph, flag)
    if search_mode == 'A':
        return a_star_search(set_origin, set_terminal, graph, flag)
        
"""
Run main function
"""
# Within this part, you should manually adjust the input as 'tsp.txt' or 'route.txt'
# mysearch('route.txt')
mysearch('route.txt')
