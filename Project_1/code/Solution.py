# This is an output printer function
def printer(solution_path, explored):
    print('#################################')
    print('The solution path is:')
    print(solution_path)
    print('#################################')
    print('The searching path is:')
    print(explored)
    print('#################################')

# This function could trace back the history and generate the searched path
def solution(set_terminal, set_origin, child, parent,solution_path, explored, mode = [], search_path = []):
    if mode == 'I':
        for i in range(len(child)):
            if set_terminal == set_origin:
                solution_path.append(set_terminal)
                solution_path.reverse()
                return printer(solution_path, search_path)
            if set_terminal == child[i]:
                solution_path.append(set_terminal)
                set_terminal = parent[i]
                return solution(set_terminal, set_origin, child, parent,solution_path, explored, 'I', search_path)
    elif mode == 'D' or 'B':
        for i in range(len(child)):
            if set_terminal == set_origin:
                solution_path.append(set_terminal)
                solution_path.reverse()
                explored.append(solution_path[-1])
                return printer(solution_path, explored)
            if set_terminal == child[i]:
                solution_path.append(set_terminal)
                set_terminal = parent[i]
                return solution(set_terminal, set_origin, child, parent,solution_path, explored)
   