# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

class Test_q8(unittest.TestCase):
    def test_g2q8(self):
        gr1=Graph.graph_from_file("/home/onyxia/ensae-prog24/input/graph1.in")
        path12_13=gr1.bfs(12,13)
        path1_18=gr1.bfs(1,18)
        path1_17=gr1.bfs(1,17)
        self.assertEqual(path12_13, [12, 17, 1, 13])
        self.assertEqual(path1_18, [1,18])
        self.assertEqual(path1_17, [1,17])


if _name_ == '_main_' : 
    unittest.main()