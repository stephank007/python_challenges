#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a graph.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the graph directed?
#     * Implement both
# * Do the edges have weights?
#     * Yes
# * Can the graph have cycles?
#     * Yes
# * If we try to add a node that already exists, do we just do nothing?
#     * Yes
# * If we try to delete a node that doesn't exist, do we just do nothing?
#     * Yes
# * Can we assume this is a connected graph?
#     * Yes
# * Can we assume the inputs are valid?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# Input:
# * `add_edge(source, destination, weight)`
# 
# ```
# graph.add_edge(0, 1, 5)
# graph.add_edge(0, 5, 2)
# graph.add_edge(1, 2, 3)
# graph.add_edge(2, 3, 4)
# graph.add_edge(3, 4, 5)
# graph.add_edge(3, 5, 6)
# graph.add_edge(4, 0, 7)
# graph.add_edge(5, 4, 8)
# graph.add_edge(5, 2, 9)
# ```
# 
# Result:
# * `source` and `destination` nodes within `graph` are connected with specified `weight`.
# 
# Note: 
# * The Graph class will be used as a building block for more complex graph challenges.

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph/graph_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


from enum import Enum  # Python 2 users: Run pip install enum34


class State(Enum):

    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        # TODO: Implement me
        pass

    def remove_neighbor(self, neighbor):
        # TODO: Implement me
        pass


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, id):
        # TODO: Implement me
        pass

    def add_edge(self, source, dest, weight=0):
        # TODO: Implement me
        pass

    def add_undirected_edge(self, source, dest, weight=0):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_graph.py
import unittest


class TestGraph(unittest.TestCase):

    def create_graph(self):
        graph = Graph()
        for key in range(0, 6):
            graph.add_node(key)
        return graph

    def test_graph(self):
        graph = self.create_graph()
        graph.add_edge(0, 1, weight=5)
        graph.add_edge(0, 5, weight=2)
        graph.add_edge(1, 2, weight=3)
        graph.add_edge(2, 3, weight=4)
        graph.add_edge(3, 4, weight=5)
        graph.add_edge(3, 5, weight=6)
        graph.add_edge(4, 0, weight=7)
        graph.add_edge(5, 4, weight=8)
        graph.add_edge(5, 2, weight=9)

        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)
        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)
        self.assertEqual(graph.nodes[2].adj_weights[graph.nodes[3].key], 4)
        self.assertEqual(graph.nodes[3].adj_weights[graph.nodes[4].key], 5)
        self.assertEqual(graph.nodes[3].adj_weights[graph.nodes[5].key], 6)
        self.assertEqual(graph.nodes[4].adj_weights[graph.nodes[0].key], 7)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[4].key], 8)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[2].key], 9)

        self.assertEqual(graph.nodes[0].incoming_edges, 1)
        self.assertEqual(graph.nodes[1].incoming_edges, 1)
        self.assertEqual(graph.nodes[2].incoming_edges, 2)
        self.assertEqual(graph.nodes[3].incoming_edges, 1)
        self.assertEqual(graph.nodes[4].incoming_edges, 2)
        self.assertEqual(graph.nodes[5].incoming_edges, 2)

        graph.nodes[0].remove_neighbor(graph.nodes[1])
        self.assertEqual(graph.nodes[1].incoming_edges, 0)
        graph.nodes[3].remove_neighbor(graph.nodes[4])
        self.assertEqual(graph.nodes[4].incoming_edges, 1)

        self.assertEqual(graph.nodes[0] < graph.nodes[1], True)

        print('Success: test_graph')

    def test_graph_undirected(self):
        graph = self.create_graph()
        graph.add_undirected_edge(0, 1, weight=5)
        graph.add_undirected_edge(0, 5, weight=2)
        graph.add_undirected_edge(1, 2, weight=3)

        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[0].key], 5)
        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[0].key], 2)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)
        self.assertEqual(graph.nodes[2].adj_weights[graph.nodes[1].key], 3)

        print('Success: test_graph_undirected')


def main():
    test = TestGraph()
    test.test_graph()
    test.test_graph_undirected()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](https://github.com/donnemartin/interactive-coding-challenges/graphs_trees/graphs/graph_solution.ipynb) for a discussion on algorithms and code solutions.
