# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

from grid import Grid

"""
Test is-sorted
"""
g = Grid.grid_from_file("/home/onyxia/work/ensae-prog24/input/grid5.in")
h= Grid.grid_from_file("/home/onyxia/work/ensae-prog24/input/grid4.in")

print(g.is_sorted()==True)
print(h.is_sorted()==False)

"""
Test swap
"""
h= Grid.grid_from_file("/home/onyxia/work/ensae-prog24/input/grid4.in")
print(h)
h.swap((3,3),(0,3))
print(h)


"""
Test swap-seq
"""
h= Grid.grid_from_file("/home/onyxia/work/ensae-prog24/input/grid4.in")
print(h)
h.swap_seq([((3,3),(0,3)),((3,1),(3,2)),((1,2),(1,3)),((0,2),(1,2))])
print(h)

"""
Tests solver
"""
h= Grid.grid_from_file("/home/onyxia/work/ensae-prog24/input/grid4.in")
S=h.get_solution()
print(S)
h.swap_seq(S)

h= Grid.grid_from_file("/home/onyxia/work/ensae-prog24/input/grid4.in")
for i in S:
    h.swap(i)
    print(h)