import matplotlib.pyplot as plt
import itertools
from graph import Graph
from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "/home/onyxia/ensae-prog24/input/"  #j'ai changé ce code parce que la version antérieure avec ..\input\ ne marchait pas 
file_name = data_path + "grid0.in"


g0 = Grid.grid_from_file(file_name)
print(g0)

chgmts=g0.get_solution()
print(chgmts)
print (g0)

g2=Grid.grid_from_file("/home/onyxia/ensae-prog24/input/grid2.in")
print(g2)

g0_unchanged= Grid.grid_from_file(file_name)

gr1=Graph.graph_from_file("/home/onyxia/ensae-prog24/input/graph1.in")
print(gr1)
path12_13=gr1.bfs(12,13)
print(path12_13)

print(g0_unchanged)

print(g0_unchanged.tuple_to_matrix((1,2,3,4)))
A=g0_unchanged.get_graph()
print(A.bfs((2,4,3,1),(1,2,3,4)))

print(g0_unchanged.get_solution2())
g0_unchanged.swap_seq(g0_unchanged.get_solution2())
print(g0_unchanged)

l2c= [[7,5,3],[4,8,6],[1,2,9]]
l2= [[7,5,3],[1,8,6],[4,2,9]]

gridtest=Grid(2,2,[[3,1],[2,4]])

print(g2.find_swap(l2,l2c))

print(gridtest.get_solution2())
print(g2.swap_matrix(l2,((1,0),(2,0))))
print(g2.get_solution_q8())
return([((0, 0), (1, 0)), ((1, 0), (2, 0)), ((1, 1), (2, 1)), ((0, 1), (1, 1))]==print(g2.get_solution_q8()))