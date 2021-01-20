import numpy as np
for i in range(5):
    print(i)
    
# import numpy as np
# kernel_up = np.identity(5)
# for i in range (1,6):
#     kernel_up = np.insert(kernel_up, 2*i-1, 0, axis = 0)

# print(kernel_up)

# for i in range (1,6):
#     print(i)
# import csv
# from graphviz import Digraph

# dot = Digraph(comment='The Round Table')
# dot.node('A', 'King Arthur')
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')
# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')
# print(dot.source)  
# dot.render('test-output/round-table.gv', view=True)  
# # read the graph.txt file
# f = open("graph.txt", 'r')
# reader = csv.reader(f)
# origin = []
# destination = []
# distance = []
# for row in reader:
#     origin.append(row[0]) 
#     destination.append(row[1])
#     distance.append(row[2])

# # Define a function to remove the empty space in string
# def strip_(obj):
#     temp = []
#     for x in obj:
#         temp.append(x.strip())
#     return temp

# destination = strip_(destination)
# distance = strip_(distance)

# # Remove duplicate elements in origin
# origin_ = []
# for x in origin:
#     if x not in origin_:
#         origin_.append(x)

# # Remove duplicate elements in destination
# destination_ =  []
# for x in destination:
#     if x not in destination_:
#         destination_.append(x)

# # Concatenate origin and destination list
# resulting_list = origin_ + [x for x in destination_ if x not in origin_]

# print('The number of vertices is:', len(resulting_list))
# print('The number of edges is:', len(distance))

