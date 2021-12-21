#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the shortest path between two nodes in a graph.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is this a directional graph?
#     * Yes
# * Could the graph have cycles?
#     * Yes
#     * Note: If the answer were no, this would be a DAG.  
#         * DAGs can be solved with a [topological sort](http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/)
# * Are the edges weighted?
#     * Yes
#     * Note: If the edges were not weighted, we could do a BFS
# * Are the edges all non-negative numbers?
#     * Yes
#     * Note: Graphs with negative edges can be done with Bellman-Ford
#         * Graphs with negative cost cycles do not have a defined shortest path
# * Do we have to check for non-negative edges?
#     * No
# * Can we assume this is a connected graph?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume we already have a graph class?
#     * Yes
# * Can we assume we already have a priority queue class?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# The constraints state we don't have to check for negative edges, so we test with the general case.
# 
# <pre>
# graph.add_edge('a', 'b', weight=5)
# graph.add_edge('a', 'c', weight=3)
# graph.add_edge('a', 'e', weight=2)
# graph.add_edge('b', 'd', weight=2)
# graph.add_edge('c', 'b', weight=1)
# graph.add_edge('c', 'd', weight=1)
# graph.add_edge('d', 'a', weight=1)
# graph.add_edge('d', 'g', weight=2)
# graph.add_edge('d', 'h', weight=1)
# graph.add_edge('e', 'a', weight=1)
# graph.add_edge('e', 'h', weight=4)
# graph.add_edge('e', 'i', weight=7)
# graph.add_edge('f', 'b', weight=3)
# graph.add_edge('f', 'g', weight=1)
# graph.add_edge('g', 'c', weight=3)
# graph.add_edge('g', 'i', weight=2)
# graph.add_edge('h', 'c', weight=2)
# graph.add_edge('h', 'f', weight=2)
# graph.add_edge('h', 'g', weight=2)
# shortest_path = ShortestPath(graph)
# result = shortest_path.find_shortest_path('a', 'i')
# self.assertEqual(result, ['a', 'c', 'd', 'g', 'i'])
# self.assertEqual(shortest_path.path_weight['i'], 8)
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_shortest_path/graph_shortest_path_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../../arrays_strings/priority_queue/priority_queue.py')
get_ipython().run_line_magic('load', '../../arrays_strings/priority_queue/priority_queue.py')


# In[ ]:


get_ipython().run_line_magic('run', '../graph/graph.py')
get_ipython().run_line_magic('load', '../graph/graph.py')


# In[ ]:


class ShortestPath(object):

    def __init__(self, graph):
        # TODO: Implement me
        pass

    def find_shortest_path(self, start_node_key, end_node_key):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_shortest_path.py
import unittest


class TestShortestPath(unittest.TestCase):

    def test_shortest_path(self):
        graph = Graph()
        graph.add_edge('a', 'b', weight=5)
        graph.add_edge('a', 'c', weight=3)
        graph.add_edge('a', 'e', weight=2)
        graph.add_edge('b', 'd', weight=2)
        graph.add_edge('c', 'b', weight=1)
        graph.add_edge('c', 'd', weight=1)
        graph.add_edge('d', 'a', weight=1)
        graph.add_edge('d', 'g', weight=2)
        graph.add_edge('d', 'h', weight=1)
        graph.add_edge('e', 'a', weight=1)
        graph.add_edge('e', 'h', weight=4)
        graph.add_edge('e', 'i', weight=7)
        graph.add_edge('f', 'b', weight=3)
        graph.add_edge('f', 'g', weight=1)
        graph.add_edge('g', 'c', weight=3)
        graph.add_edge('g', 'i', weight=2)
        graph.add_edge('h', 'c', weight=2)
        graph.add_edge('h', 'f', weight=2)
        graph.add_edge('h', 'g', weight=2)
        shortest_path = ShortestPath(graph)
        result = shortest_path.find_shortest_path('a', 'i')
        self.assertEqual(result, ['a', 'c', 'd', 'g', 'i'])
        self.assertEqual(shortest_path.path_weight['i'], 8)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](https://github.com/donnemartin/interactive-coding-challenges/graphs_trees/graph_shortest_path/graph_shortest_path_solution.ipynb) for a discussion on algorithms and code solutions.
