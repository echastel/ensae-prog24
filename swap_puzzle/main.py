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
g2sort=g2.get_solution()

print(g2sort)
print(g2)
