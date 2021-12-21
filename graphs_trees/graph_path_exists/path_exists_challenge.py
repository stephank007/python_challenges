#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Determine whether there is a path between two nodes in a graph.
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
# * Can we assume we already have Graph and Node classes?
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
# graph.add_edge(0, 4, 3)
# graph.add_edge(0, 5, 2)
# graph.add_edge(1, 3, 5)
# graph.add_edge(1, 4, 4)
# graph.add_edge(2, 1, 6)
# graph.add_edge(3, 2, 7)
# graph.add_edge(3, 4, 8)
# ```
# 
# Result:
# * search_path(start=0, end=2) -> True
# * search_path(start=0, end=0) -> True
# * search_path(start=4, end=5) -> False

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_path_exists/path_exists_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../graph/graph.py')
get_ipython().run_line_magic('load', '../graph/graph.py')


# In[ ]:


class GraphPathExists(Graph):

    def path_exists(self, start, end):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_path_exists.py
import unittest


class TestPathExists(unittest.TestCase):

    def test_path_exists(self):
        nodes = []
        graph = GraphPathExists()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)

        self.assertEqual(graph.path_exists(nodes[0], nodes[2]), True)
        self.assertEqual(graph.path_exists(nodes[0], nodes[0]), True)
        self.assertEqual(graph.path_exists(nodes[4], nodes[5]), False)

        print('Success: test_path_exists')


def main():
    test = TestPathExists()
    test.test_path_exists()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_path_exists/path_exists_solution.ipynb) for a discussion on algorithms and code solutions.
