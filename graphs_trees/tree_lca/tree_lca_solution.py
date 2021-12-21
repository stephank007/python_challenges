#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the lowest common ancestor of two nodes in a binary tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# * Verify both nodes are in the tree
# * Base cases
#     * If the root is None, return None
#     * If the root is either node, return the root
# * Recursively search left and right
# * If the left and right are both nodes
#     * The return the root
# * Else, left or right, whichever is valid
# 
# Complexity:
# * Time: O(h), where h is the height of the tree
# * Space: O(h), where h is the recursion depth

# ## Code

# In[1]:


class Node(object):

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)


# In[2]:


class BinaryTree(object):

    def lca(self, root, node1, node2):
        if None in (root, node1, node2):
            return None
        if (not self._node_in_tree(root, node1) or
                not self._node_in_tree(root, node2)):
            return None
        return self._lca(root, node1, node2)

    def _node_in_tree(self, root, node):
        if root is None:
            return False
        if root is node:
            return True
        left = self._node_in_tree(root.left, node)
        right = self._node_in_tree(root.right, node)
        return left or right

    def _lca(self, root, node1, node2):
        if root is None:
            return None
        if root is node1 or root is node2:
            return root
        left_node = self._lca(root.left, node1, node2)
        right_node = self._lca(root.right, node1, node2)
        if left_node is not None and right_node is not None:
            return root
        else:
            return left_node if left_node is not None else right_node


# In[3]:


class LcaResult(object):

    def __init__(self, node, is_ancestor):
        self.node = node
        self.is_ancestor = is_ancestor


class BinaryTreeOptimized(object):

    def lca(self, root, node1, node2):
        if root is None:
            raise TypeError('root cannot be None')
        result = self._lca(root, node1, node2)
        if result.is_ancestor:
            return result.node
        return None

    def _lca(self, curr_node, node1, node2):
        if curr_node is None:
            return LcaResult(None, is_ancestor=False)
        if curr_node is node1 and curr_node is node2:
            return LcaResult(curr_node, is_ancestor=True)
        left_result = self._lca(curr_node.left, node1, node2)
        if left_result.is_ancestor:
            return left_result
        right_result = self._lca(curr_node.right, node1, node2)
        if right_result.is_ancestor:
            return right_result
        if left_result.node is not None and right_result.node is not None:
            return LcaResult(curr_node, is_ancestor=True)
        elif curr_node is node1 or curr_node is node2:
            is_ancestor = left_result.node is not None or                 right_result.node is not None
            return LcaResult(curr_node, is_ancestor)
        else:
            return LcaResult(left_result.node if left_result.node is not None                                  else right_result.node, is_ancestor=False)


# ## Unit Test

# In[4]:


get_ipython().run_cell_magic('writefile', 'test_lca.py', "import unittest\n\n\nclass TestLowestCommonAncestor(unittest.TestCase):\n\n    def test_lca(self):\n        node10 = Node(10)\n        node5 = Node(5)\n        node12 = Node(12)\n        node3 = Node(3)\n        node1 = Node(1)\n        node8 = Node(8)\n        node9 = Node(9)\n        node18 = Node(18)\n        node20 = Node(20)\n        node40 = Node(40)\n        node3.left = node1\n        node3.right = node8\n        node5.left = node12\n        node5.right = node3\n        node20.left = node40\n        node9.left = node18\n        node9.right = node20\n        node10.left = node5\n        node10.right = node9\n        root = node10\n        node0 = Node(0)\n        binary_tree = BinaryTree()\n        self.assertEqual(binary_tree.lca(root, node0, node5), None)\n        self.assertEqual(binary_tree.lca(root, node5, node0), None)\n        self.assertEqual(binary_tree.lca(root, node1, node8), node3)\n        self.assertEqual(binary_tree.lca(root, node12, node8), node5)\n        self.assertEqual(binary_tree.lca(root, node12, node40), node10)\n        self.assertEqual(binary_tree.lca(root, node9, node20), node9)\n        self.assertEqual(binary_tree.lca(root, node3, node5), node5)\n        print('Success: test_lca')\n\n\ndef main():\n    test = TestLowestCommonAncestor()\n    test.test_lca()\n\n\nif __name__ == '__main__':\n    main()")


# In[5]:


get_ipython().run_line_magic('run', '-i test_lca.py')

