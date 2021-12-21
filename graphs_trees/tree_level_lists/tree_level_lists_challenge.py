#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Create a list for each level of a binary tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is this a binary search tree?
#     * Yes
# * Should each level be a list of nodes?
#     * Yes
# * Can we assume we already have a Node class with an insert method?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * 5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11 -> [[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]
# 
# Note: Each number in the result is actually a node containing the number

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_level_lists/tree_level_lists_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../bst/bst.py')
get_ipython().run_line_magic('load', '../bst/bst.py')


# In[ ]:


class BstLevelLists(Bst):

    def create_level_lists(self):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[ ]:


# %load test_tree_level_lists.py
import unittest


class TestTreeLevelLists(unittest.TestCase):

    def test_tree_level_lists(self):
        bst = BstLevelLists(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(2)
        bst.insert(4)
        bst.insert(1)
        bst.insert(7)
        bst.insert(6)
        bst.insert(9)
        bst.insert(10)
        bst.insert(11)

        levels = bst.create_level_lists()
        results_list = []
        for level in levels:
            results = Results()
            for node in level:
                results.add_result(node)
            results_list.append(results)

        self.assertEqual(str(results_list[0]), '[5]')
        self.assertEqual(str(results_list[1]), '[3, 8]')
        self.assertEqual(str(results_list[2]), '[2, 4, 7, 9]')
        self.assertEqual(str(results_list[3]), '[1, 6, 10]')
        self.assertEqual(str(results_list[4]), '[11]')

        print('Success: test_tree_level_lists')


def main():
    test = TestTreeLevelLists()
    test.test_tree_level_lists()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_level_lists/tree_level_lists_solution.ipynb) for a discussion on algorithms and code solutions.
