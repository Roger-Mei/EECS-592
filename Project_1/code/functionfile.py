import mygraph
import math
"""
Define the solution path
"""
def solution(set_origin, input, graph, explored):
    solution_path = []
    solution_cost = 0
    number_of_node_expanded = len(explored)
    while True:
        solution_path.insert(0,input.name)
        if input.name == set_origin:
            break
        else:
            print(input.name)
            path_cost = input.nbr_dict[input.parent.name]
            solution_cost += path_cost
            input = input.parent
    print('#################################')
    print('The solution path is:')
    print(solution_path)
    print('#################################')
    print('The total number of node expanded is:')
    print(number_of_node_expanded)
    print('#################################')
    print('The solution cost is:')
    print(solution_cost)
    return solution_cost,explored
    
"""
Breadth-first-search
"""       
def breadth_first_search(set_origin, set_terminal, graph, flag):
    # Route-planning problem
    if flag == 0:
        # Initialization
        frontier = []
        explored = []
        cur_node = graph.node_dict[set_origin]
        cur_node.depth = 0
        if cur_node.name == set_terminal:
            return solution(set_origin, cur_node, graph, explored)
        frontier.append(cur_node)
        search_depth = 0 # Define the searching depth
        while True:
            # Judge whether the frontier is empty
            if not frontier: 
                return False
            temp_child = [] # Create a temprary list to store the child generated
            for node in frontier:
                if node.depth == search_depth:
                    cur_node = frontier[0]
                    frontier.pop(0)
                    if cur_node.name not in explored:
                        explored.append(cur_node.name)
                        print(explored)
                        # Try to find child
                        for nbr_name in cur_node.nbr_dict.keys():
                            child = graph.node_dict[nbr_name]
                            if child.name not in explored:
                                child.parent = cur_node
                                print('parent:', child.parent.name)
                                print('child:', child.name)
                                child.depth = search_depth + 1 
                                temp_child.append(child)
            for child in temp_child: 
                if child.name == set_terminal: # Check whether the goal state is satisfied
                    return solution(set_origin, child, graph, explored)
                if child.name not in explored and child not in frontier:
                    frontier.append(child)
            search_depth += 1

    # # TSP problem
    # if flag == 1:
    #     explored_city = []
    #     cur_node = graph.node_dict[set_origin]
    #     explored_city.append(cur_node.name)
    #     for target in graph.node_dict.values():
    #         if target.name not in explored_city:
    #             if target.name != set_origin:
    #                 set_terminal = target.name
    #                 path_cost, temp_explored_city = breadth_first_search(cur_node.name, set_terminal, graph, 0)
    #                 cur_node.tsp_cost_list.append(path_cost) # Constructing path cost
    #                 cur_node.tsp_target_list.append(target) # Constructing the city name corresponding to the path cost
    #                 for city in temp_explored_city:
    #                     cur_node.tsp_explored_city[target.name].append(city)
    #     # Now we select out the shortest path:
    #     index = cur_node.tsp_cost_list.index(min(cur_node.tsp_cost_list))
    #     temp_terminal = cur_node.tsp_target_list[index]
    #     # Append the explored city
        

    if len(explored_city) == len(graph.node_dict):
        return solution(set_origin, )
        


"""
Depth-first-search
"""
def depth_first_search(set_origin, set_terminal, graph, flag):
    if flag == 0:
        # Initialization
        frontier = []
        explored = []
        search_path = []

        cur_node = graph.node_dict[set_origin]
        if cur_node.name == set_terminal:
            return solution(set_origin, cur_node, graph, explored)
        frontier.append(cur_node)
        while True:
            # Judge whether the frontier is empty
            if not frontier: 
                return False
            cur_node = frontier[-1]
            print(cur_node.name)
            frontier_ = []
            for node in frontier:
                frontier_.append(node.name)
            print(frontier_)
            frontier.pop(-1)
            explored.append(cur_node.name)
            print(explored)
            # Try to find child
            for nbr_name in cur_node.nbr_dict.keys():
                child = graph.node_dict[nbr_name]
                if child.name == set_terminal:
                    child.parent = cur_node
                    return solution(set_origin, child, graph, explored)
                elif child not in frontier and child.name not in explored:
                    child.parent = cur_node
                    frontier.append(child)

"""
Iterative-deepening search
""" 
# We first define the depth-limited-search function
def depth_limited_search(set_origin, set_terminal, limit, graph):
    # Initialization
    explored = []
    node = graph.node_dict[set_origin]
    return Recursive_DLS (node, set_origin, set_terminal, limit, explored, graph)

# We then define the Recursive-DLS function
def Recursive_DLS(node, set_origin, set_terminal, limit, explored, graph):
    if node.name == set_terminal:
        return solution(set_origin, node, graph, explored)
    elif limit == 0:
        return 'Cutoff'
    else:
        cutoff_occurred = False
        explored.append(node.name)
        for nbr_name in node.nbr_dict.keys():
            if nbr_name not in explored:
                child = graph.node_dict[nbr_name]
                child.parent = node
                result = Recursive_DLS(child, set_origin, set_terminal, limit-1, explored, graph)
                if result == 'Cutoff':
                    cutoff_occurred = True
                elif result != False:
                    return result
        if cutoff_occurred:
            return 'Cutoff'
        else:
            return False

# At last we define interative-deepening-search
def iterative_deepening_search(set_origin, set_terminal, graph, flag):
    if flag == 0:
        for limit in range(0,20):
            result = depth_limited_search(set_origin, set_terminal, limit, graph)
            if result != False and result != 'Cutoff':
                return result

"""
Uniform-cost Search
"""
# Define a recursive sorting function
def sort(target_list, graph, n):
    if n == 1:
        return target_list
    for i in range(0,n):
        for j in range(i+1,n):
            if target_list[j].f < target_list[i].f:
                target_list[i],target_list[j] = target_list[j], target_list[i]
    return target_list

# Define a comparision function
def compare(child, frontier, graph):
    for node in frontier:
        if child.name == node.name: 
            if child.f < node.f:
                return True

def uniform_cost_search(set_origin, set_terminal, graph, flag):
    if flag == 0:
        # Initialization
        frontier = []
        explored = []
        node = graph.node_dict[set_origin]

        frontier.append(node)
        while True:
            if not frontier:
                return False
            frontier = sort(frontier, graph, len(frontier)) # Sort the frontier based on its cost value
            cur_node = frontier.pop(0) # Choose the lowest-cost node in frontier
            if cur_node.name == set_terminal:
                return solution(set_origin, cur_node, graph, explored)
            explored.append(cur_node.name)
            for nbr_name in cur_node.nbr_dict.keys():
                child = graph.node_dict[nbr_name]
                compare_result = compare(child, frontier, graph)
                if child not in frontier and child.name not in explored:
                    frontier.append(child)
                    child.parent = cur_node
                    child.f = cur_node.f + cur_node.nbr_dict[child.name]
                elif compare_result == True: # if the node is in frontier with higher cost, replace the node with child
                    for node in frontier:
                        if child.name == node.name:
                                node = child

"""
A-star search
"""
# We first define a distance calculator
def distance(init_point, goal, graph):
    x1 = init_point.x_coordinate
    y1 = init_point.y_coordinate
    z1 = init_point.z_coordinate
    x2 = goal.x_coordinate
    y2 = goal.y_coordinate
    z2 = goal.z_coordinate
    dist = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2) + math.pow(z1-z2,2))
    return dist

def a_star_search(set_origin, set_terminal, graph, flag):
    if flag == 0:
        # Initialization
        frontier = []
        explored = []
        goal = graph.node_dict[set_terminal]
        node  = graph.node_dict[set_origin]
        node.f = distance(node, goal, graph)

        frontier.append(node)
        while True:
            if not frontier:
                return False
            frontier = sort(frontier, graph, len(frontier)) # Sort the frontier based on its cost value
            #### Debug ####
            frontier_ = []
            total_cost = []
            for node in frontier:
                frontier_.append(node.name)
                total_cost.append(node.f)
            print(frontier_)
            print(total_cost)
            ###############
            cur_node = frontier.pop(0) # Choose the lowest-cost node in frontier
            print(cur_node.name)
            if cur_node.name == set_terminal:
                return solution(set_origin, cur_node, graph, explored)
            explored.append(cur_node.name) # Note that explored store name, not node!
            #### Debug ####
            print(explored)
            ###############
            for nbr_name in cur_node.nbr_dict.keys():
                child = graph.node_dict[nbr_name]
                compare_result = compare(child, frontier, graph)
                print(compare_result)
                if child not in frontier and child.name not in explored:
                    frontier.append(child)
                    child.parent = cur_node
                    child.g = cur_node.g + cur_node.nbr_dict[child.name]
                    child.h = distance(child, goal,graph)
                    child.f = child.g + child.h
                    #### Debug ####
                    print(child.name)
                    print(child.parent.name)
                    print(child.g)
                    print(child.h)
                    print(child.f)
                    print(compare_result)
                    ################
                elif compare_result == True: # if the node is in frontier with higher cost, replace the node with child
                    for node in frontier:
                        if child.name == node.name:
                                node = child





