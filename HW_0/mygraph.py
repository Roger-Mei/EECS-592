import csv

# read the graph.txt file
f = open("graph.txt", 'r')
reader = csv.reader(f)
origin = []
destination = []
distance = []
for row in reader:
    origin.append(row[0]) 
    destination.append(row[1])
    distance.append(row[2])

# Define a function to remove the empty space in string
def strip_(obj):
    temp = []
    for x in obj:
        temp.append(x.strip())
    return temp

destination = strip_(destination)
distance = strip_(distance)

# Remove duplicate elements in origin
origin_ = []
for x in origin:
    if x not in origin_:
        origin_.append(x)

# Remove duplicate elements in destination
destination_ =  []
for x in destination:
    if x not in destination_:
        destination_.append(x)

# Concatenate origin and destination list
resulting_list = origin_ + [x for x in destination_ if x not in origin_]

print('The number of vertices is:', len(resulting_list))
print('The number of edges is:', len(distance))

