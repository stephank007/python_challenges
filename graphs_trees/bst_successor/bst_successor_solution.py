#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the in-order successor of a given node in a binary search tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * If there is no successor, do we return None?
#     * Yes
# * If the input is None, should we throw an exception?
#     * Yes
# * Can we assume we already have a Node class that keeps track of parents?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
#           _5_
#         /     \
#        3       8
#       / \    /   \
#      2   4  6    12
#     /        \   / \
#    1          7 10  15
#                /
#               9
# 
# In: None  Out: Exception
# In: 4     Out: 5
# In: 5     Out: 6
# In: 8     Out: 9
# In: 15    Out: None
# </pre>

# ## Algorithm
# 
# * If the node has a right subtree, return the left-most node in the right subtree
# * Else, go up until you find a node that is its parent's left node
#     * If you get to the root (ie node.parent is None), return None
#         * The original input node must be the largest in the tree
#     * Else, return the parent
#     
# Complexity:
# * Time: O(h), where h is the height of the tree
# * Space: O(h), where h is the recursion depth (tree height), or O(1) if using an iterative approach

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


class BstSuccessor(object):

    def get_next(self, node):
        if node is None:
            raise TypeError('node cannot be None')
        if node.right is not None:
            return self._left_most(node.right)
        else:
            return self._next_ancestor(node)

    def _left_most(self, node):
        if node.left is not None:
            return self._left_most(node.left)
        else:
            return node.data

    def _next_ancestor(self, node):
        if node.parent is not None:
            if node.parent.data > node.data:
                return node.parent.data
            else:
                return self._next_ancestor(node.parent)
        # We reached the root, the original input node
        # must be the largest element in the tree.
        return None


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_bst_successor.py', "import unittest\n\n\nclass TestBstSuccessor(unittest.TestCase):\n\n    def test_bst_successor_empty(self):\n        bst_successor = BstSuccessor()\n        bst_successor.get_next(None)\n\n    def test_bst_successor(self):\n        nodes = {}\n        node = Node(5)\n        nodes[5] = node\n        bst = Bst(nodes[5])\n        nodes[3] = bst.insert(3)\n        nodes[8] = bst.insert(8)\n        nodes[2] = bst.insert(2)\n        nodes[4] = bst.insert(4)\n        nodes[6] = bst.insert(6)\n        nodes[12] = bst.insert(12)\n        nodes[1] = bst.insert(1)\n        nodes[7] = bst.insert(7)\n        nodes[10] = bst.insert(10)\n        nodes[15] = bst.insert(15)\n        nodes[9] = bst.insert(9)\n\n        bst_successor = BstSuccessor()\n        self.assertEqual(bst_successor.get_next(nodes[4]), 5)\n        self.assertEqual(bst_successor.get_next(nodes[5]), 6)\n        self.assertEqual(bst_successor.get_next(nodes[8]), 9)\n        self.assertEqual(bst_successor.get_next(nodes[15]), None)\n\n        print('Success: test_bst_successor')\n\n\ndef main():\n    test = TestBstSuccessor()\n    test.test_bst_successor()\n    test.assertRaises(TypeError, test.test_bst_successor_empty)\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_bst_successor.py')

