import matplotlib.pyplot as plt
import itertools
from graph import Graph
from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "/home/onyxia/ensae-prog24/input/"  #j'ai changé ce code parce que la version antérieure avec ..\input\ ne marchait pas 
file_name = data_path + "grid0.in"



g2=Grid.grid_from_file("/home/onyxia/ensae-prog24/input/grid2.in")
print(g2)

g0_unchanged= Grid.grid_from_file(file_name)


l2= [[7,5,3],[1,8,6],[4,2,9],[10,11,12]]

#gridtest=Grid(2,2,[[3,1],[2,4]])
#print(gridtest)
#print(g2.find_swap(l2,l2c))

#print(gridtest.get_solution2())
#print(g2.swap_matrix(l2,((1,0),(2,0))))
#print(g2.get_solution_q8())

#return([((0, 0), (1, 0)), ((1, 0), (2, 0)), ((1, 1), (2, 1)), ((0, 1), (1, 1))]==print(g2.get_solution_q8()))
#print(gridtest.a_star())
#print(gridtest.heuristic(gridtest.state))

l2c= [[5,1,3],[2,4,6]]
testa=Grid(2,3,l2c)


#print(g2.find_swap(l2,l2c))
#print(gridtest.get_solution2())
#print(g2.swap_matrix(l2,((1,0),(2,0))))
#print(g2.get_solution_q8())
#return([((0, 0), (1, 0)), ((1, 0), (2, 0)), ((1, 1), (2, 1)), ((0, 1), (1, 1))]==print(g2.get_solution_q8()))
#print(gridtest.a_star())

#print(testa.a_star())


mygrid=Grid(4,3,l2)
print("le chemin de swaps avec l2 c'est ", mygrid.a_star())