#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement breadth-first traversal on a binary tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume we already have a Node class with an insert method?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes
# * What should we do with each node when we process it?
#     * Call an input method `visit_func` on the node

# ## Test Cases
# 
# ### Breadth-First Traversal
# * 5, 2, 8, 1, 3 -> 5, 2, 8, 1, 3

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_bfs/bfs_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../bst/bst.py')
get_ipython().run_line_magic('load', '../bst/bst.py')


# In[ ]:


class BstBfs(Bst):

    def bfs(self, visit_func):
        # TODO: Implement me
        pass


# ## Unit Test

# In[ ]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[ ]:


# %load test_bfs.py
import unittest


class TestBfs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBfs, self).__init__()
        self.results = Results()

    def test_bfs(self):
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        self.assertEqual(str(self.results), '[5, 2, 8, 1, 3]')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_bfs/bfs_solution.ipynb) for a discussion on algorithms and code solutions.
