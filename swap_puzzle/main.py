import matplotlib.pyplot as plt
import itertools

print("Hello world")

n=5
m=4
print([list(range(i*n+1, (i+1)*n+1)) for i in range(m)])

from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "/home/onyxia/work/ensae-prog24/input/"  #j'ai changé ce code parce que la version antérieure avec ..\input\ ne marchait pas 
file_name = data_path + "grid0.in"

print(file_name)

g0 = Grid.grid_from_file(file_name)
print(g0)

chgmts=g0.get_solution()
print(chgmts)
print (g0)

g2=Grid.grid_from_file("/home/onyxia/work/ensae-prog24/input/grid2.in")
print(g2)
g2sort=g2.get_solution()

print(g2sort)
print(g2)

g0_unchanged= Grid.grid_from_file(file_name)

print(g0.Grid_as_tuple())
print(g2.Grid_as_tuple())


print()

A=[[1,2],[3,4]]
Dots=[i  for j in A for i in j]
print(list(itertools.permutations(Dots)))