import matplotlib.pyplot as plt
import itertools
from graph import Graph

print("Hello world")

n=5
m=4
print([list(range(i*n+1, (i+1)*n+1)) for i in range(m)])

from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "/home/onyxia/ensae-prog24/input/"  #j'ai changé ce code parce que la version antérieure avec ..\input\ ne marchait pas 
file_name = data_path + "grid0.in"

print(file_name)

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

print(g0_unchanged.tuple_to_Grid((1,2,3,4)))
A=g0_unchanged.get_graph()
print(A.bfs((2,4,3,1),(1,2,3,4)))

print(g0_unchanged.get_solution2())
g0_unchanged.swap_seq(g0_unchanged.get_solution2())
print(g0_unchanged)

