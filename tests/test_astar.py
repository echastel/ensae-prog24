# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

class Test_ast(unittest.TestCase):
    def test_a_star(self):
        mygrid=Grid(4,3,l2)
        self.assertEqual(mygrid.a_star, [((1, 1), (2, 1)), ((0, 0), (1, 0)), ((1, 0), (2, 0)), ((0, 1), (1, 1))])
        

if _name_ == '_main_' : 
    unittest.main()