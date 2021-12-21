#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement depth-first traversals (in-order, pre-order, post-order) on a binary tree.
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
# * What should we do with each node when we process it?
#     * Call an input method `visit_func` on the node
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# ### In-Order Traversal
# 
# * 5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
# * 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
# 
# ### Pre-Order Traversal
# 
# * 5, 2, 8, 1, 3 -> 5, 2, 1, 3, 8
# * 1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
# 
# ### Post-Order Traversal
# 
# * 5, 2, 8, 1, 3 -> 1, 3, 2, 8, 5
# * 1, 2, 3, 4, 5 -> 5, 4, 3, 2, 1

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_dfs/dfs_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../bst/bst.py')
get_ipython().run_line_magic('load', '../bst/bst.py')


# In[ ]:


class BstDfs(Bst):

    def in_order_traversal(self, node, visit_func):
    # TODO: Implement me
    pass

    def pre_order_traversal(self, node, visit_func):
        # TODO: Implement me
        pass

    def post_order_traversal(self,node, visit_func):
        # TODO: Implement me
        pass


# ## Unit Test

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
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[5, 2, 1, 3, 8]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 3, 2, 8, 5]")
        self.results.clear_results()

        bst = BstDfs(Node(1))
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)

        bst.in_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        self.assertEqual(str(self.results), "[5, 4, 3, 2, 1]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_dfs/dfs_solution.ipynb) for a discussion on algorithms and code solutions.
