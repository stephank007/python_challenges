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
# * Is the graph directed?
#     * Yes
# * Is the graph weighted?
#     * No
# * Can we assume we already have Graph and Node classes?
#     * Yes
# * Are the inputs two Nodes?
#     * Yes
# * Is the output a list of Node keys that make up the shortest path?
#     * Yes
# * If there is no path, should we return None?
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
# graph.add_edge(0, 1)
# graph.add_edge(0, 4)
# graph.add_edge(0, 5)
# graph.add_edge(1, 3)
# graph.add_edge(1, 4)
# graph.add_edge(2, 1)
# graph.add_edge(3, 2)
# graph.add_edge(3, 4)
# ```
# 
# Result:
# * search_path(start=0, end=2) -> [0, 1, 3, 2]
# * search_path(start=0, end=0) -> [0]
# * search_path(start=4, end=5) -> None

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_path_exists/path_exists_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../graph/graph.py')
get_ipython().run_line_magic('load', '../graph/graph.py')


# In[ ]:


class GraphShortestPath(Graph):

    def shortest_path(self, source_key, dest_key):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_shortest_path.py
import unittest


class TestShortestPath(unittest.TestCase):

    def test_shortest_path(self):
        nodes = []
        graph = GraphShortestPath()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(0, 5)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 1)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)

        self.assertEqual(graph.shortest_path(nodes[0].key, nodes[2].key), [0, 1, 3, 2])
        self.assertEqual(graph.shortest_path(nodes[0].key, nodes[0].key), [0])
        self.assertEqual(graph.shortest_path(nodes[4].key, nodes[5].key), None)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_path_exists/path_exists_solution.ipynb) for a discussion on algorithms and code solutions.
