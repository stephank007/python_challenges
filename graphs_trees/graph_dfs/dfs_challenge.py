#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement depth-first search on a graph.
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
# * Order of nodes visited: [0, 1, 3, 2, 4, 5]

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_dfs/dfs_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../graph/graph.py')
get_ipython().run_line_magic('load', '../graph/graph.py')


# In[ ]:


class GraphDfs(Graph):

    def dfs(self, root, visit_func):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[ ]:


# %load test_dfs.py
import unittest


class TestDfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDfs, self).__init__()
        self.results = Results()

    def test_dfs(self):
        nodes = []
        graph = GraphDfs()
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
        graph.dfs(nodes[0], self.results.add_result)
        self.assertEqual(str(self.results), "[0, 1, 3, 2, 4, 5]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_dfs/dfs_solution.ipynb) for a discussion on algorithms and code solutions.
