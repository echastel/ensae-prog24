# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

g=Grid(3,2,[[6,4],[2,1],[3,5]])

class Test_Naive(unittest.TestCase):
    def test_naive(self):
        g=Grid(3,2,[[6,4],[2,1],[3,5]])
        self.assertEqual(g.is_sorted(), False)
        L=g.get_solution()
        self.assertEqual(g.is_sorted(), True)
        self.assertEqual(L, [((1, 1), (1, 0)), ((1, 0), (0, 0)), ((1, 1), (0, 1)), ((2, 0), (1, 0)), ((2, 1), (2, 0))])

if __name__ == '__main__':
    unittest.main()