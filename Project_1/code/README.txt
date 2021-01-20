In this homework, please refer to mysearch.py to test the result. I failed to finish the TSP problem due to the misconstruction 
of the graph, but I finished the route-planning problem. When you are trying to play around with this code, please go to the 
very bottom of the mysearch.py. run the mysearch('route.txt').

Although I failed to finish the TSP, I could still explain the heuristic of the A-star in TSP: we should choose the product of the shortest path
and the number of cities unexplored as our heuristic, so that the admissibility could be guaranteed.