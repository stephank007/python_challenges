#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Invert a binary tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * What does it mean to invert a binary tree?
#     * Swap all left and right node pairs
# * Can we assume we already have a Node class?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# Input:
#      5
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 
# Output:
#      5
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# </pre>

# ## Algorithm
# 
# * Base case
#     * If the root is None, return
# * Recursive case
#     * Recurse on the left node
#     * Recurse on the right node
#     * Swap left and right
# * Return the node
# 
# Complexity:
# * Time: O(n)
# * Space: O(h), where h is the height, for the recursion depth

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


class InverseBst(Bst):

    def invert_tree(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        return self._invert_tree(self.root)

    def _invert_tree(self, root):
        if root is None:
            return
        self._invert_tree(root.left)
        self._invert_tree(root.right)
        root.left, root.right = root.right, root.left
        return root


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_invert_tree.py', "import unittest\n\n\nclass TestInvertTree(unittest.TestCase):\n\n    def test_invert_tree(self):\n        root = Node(5)\n        bst = InverseBst(root)\n        node2 = bst.insert(2)\n        node3 = bst.insert(3)\n        node1 = bst.insert(1)\n        node7 = bst.insert(7)\n        node6 = bst.insert(6)\n        node9 = bst.insert(9)\n        result = bst.invert_tree()\n        self.assertEqual(result, root)\n        self.assertEqual(result.left, node7)\n        self.assertEqual(result.right, node2)\n        self.assertEqual(result.left.left, node9)\n        self.assertEqual(result.left.right, node6)\n        self.assertEqual(result.right.left, node3)\n        self.assertEqual(result.right.right, node1)\n        print('Success: test_invert_tree')\n\n\ndef main():\n    test = TestInvertTree()\n    test.test_invert_tree()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_invert_tree.py')

