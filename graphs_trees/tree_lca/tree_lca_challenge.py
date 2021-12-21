#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the lowest common ancestor in a binary tree.
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
#     * No
# * Can we assume the two nodes are in the tree?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
#           _10_
#         /      \
#        5        9
#       / \      / \
#      12  3    18  20
#         / \       /
#        1   8     40
# </pre>
# 
# * 0, 5 -> None
# * 5, 0 -> None
# * 1, 8 -> 3
# * 12, 8 -> 5
# * 12, 40 -> 10
# * 9, 20 -> 9
# * 3, 5 -> 5

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.jupyter.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_lca/tree_lca_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Node(object):

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)


# In[ ]:


class BinaryTree(object):

    def lca(self, root, node1, node2):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_lca.py
import unittest


class TestLowestCommonAncestor(unittest.TestCase):

    def test_lca(self):
        node10 = Node(10)
        node5 = Node(5)
        node12 = Node(12)
        node3 = Node(3)
        node1 = Node(1)
        node8 = Node(8)
        node9 = Node(9)
        node18 = Node(18)
        node20 = Node(20)
        node40 = Node(40)
        node3.left = node1
        node3.right = node8
        node5.left = node12
        node5.right = node3
        node20.left = node40
        node9.left = node18
        node9.right = node20
        node10.left = node5
        node10.right = node9
        root = node10
        node0 = Node(0)
        binary_tree = BinaryTree()
        self.assertEqual(binary_tree.lca(root, node0, node5), None)
        self.assertEqual(binary_tree.lca(root, node5, node0), None)
        self.assertEqual(binary_tree.lca(root, node1, node8), node3)
        self.assertEqual(binary_tree.lca(root, node12, node8), node5)
        self.assertEqual(binary_tree.lca(root, node12, node40), node10)
        self.assertEqual(binary_tree.lca(root, node9, node20), node9)
        self.assertEqual(binary_tree.lca(root, node3, node5), node5)
        print('Success: test_lca')


def main():
    test = TestLowestCommonAncestor()
    test.test_lca()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
