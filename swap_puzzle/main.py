print("Hello world")

n=5
m=4
print([list(range(i*n+1, (i+1)*n+1)) for i in range(m)])

from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)