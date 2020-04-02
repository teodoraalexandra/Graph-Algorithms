from graphController import GraphController

import unittest


class Graph_test_init:
    '''
    5 3
    0 1 7
    2 3 2
    4 1 5
    '''
    def __init__(self):
        self.dcosts = {
            "origin": [0, 2, 4],
            "target": [1, 3, 1],
            "edge": [7, 2, 5]
        }
        self.din = {0: [], 1: [0, 4], 2: [], 3: [2], 4: []}
        self.dout = {0: [1], 1: [], 2: [3], 3: [], 4: [1]}
        self.vertices = 5
        self.edges = 3


class Test(unittest.TestCase):
    def setUp(self):
        self.repo = Graph_test_init()
        self.controller = GraphController(self.repo)
        self.initial_number_of_edges = self.repo.edges
        self.initial_number_of_vertices = self.repo.vertices

    def test_add_edge(self):
        self.controller.addEdge(0, 3, 4)
        self.assertEqual(self.repo.edges, self.initial_number_of_edges + 1)
        self.assertEqual(self.repo.dout[0], [1, 3])
        self.assertEqual(self.repo.din[3], [2, 0])

    def test_remove_edge(self):
        self.controller.removeEdge(0, 3, 4)
        self.assertEqual(self.repo.edges, self.initial_number_of_edges)
        self.assertEqual(self.repo.dout[0], [1])
        self.assertEqual(self.repo.din[3], [2])

    def test_add_vertex(self):
        self.controller.addVertex(5)
        self.assertEqual(self.repo.vertices, self.initial_number_of_vertices + 1)
        self.assertEqual(self.repo.dout[5], [])
        self.assertEqual(self.repo.din[5], [])

    def test_remove_vertex(self):
        self.controller.removeVertex(4)
        self.assertEqual(self.repo.vertices, self.initial_number_of_vertices - 1)
        self.assertEqual(self.repo.dout, {0: [1], 1: [], 2: [3], 3: []})
        self.assertEqual(self.repo.din, {0: [], 1: [0, 4], 2: [], 3: [2]})

    def test_update_cost(self):
        self.controller.updateCost(0, 1, 10)
        self.assertEqual(self.repo.dcosts, {"origin": [0, 2, 4], "target": [1, 3, 1], "edge": [10, 2, 5]})


