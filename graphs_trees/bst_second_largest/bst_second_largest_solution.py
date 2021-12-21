#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the second largest node in a binary search tree.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * If this is called on a None input or a single node, should we raise an exception?
#     * Yes
#         * None -> TypeError
#         * Single node -> ValueError
# * Can we assume we already have a Node class with an insert method?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None or single node -> Exception
# 
# <pre>
# Input:
#                 _10_
#               _/    \_          
#              5        15
#             / \       / \
#            3   8     12  20
#           /     \         \
#          2       4        30
# 
# Output: 20
# 
# Input:
#                  10
#                  /  
#                 5
#                / \
#               3   7
# Output: 7
# </pre>

# ## Algorithm
# 
# <pre>
# 
# If there is no right node, the second largest is the right most left subtree:
# 
#                  10
#                  /  
#                 5
#                / \
#               3   7
# 
# If there is a right node and the right node has children, recurse to that right child:
# 
#                 _10_
#               _/    \_          
#              5        15
#             / \       / \
#            3   8     12  20
#           /     \         \
#          2       4        30
# 
# Eventually we'll get to the following scenario:
# 
#                  20
#                   \
#                    30
# 
# If the right node has no children, the second largest is the current node.
# 
# </pre>
# 
# Complexity:
# * Time: O(h)
# * Space: O(h), where h is the height of the tree

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


class Solution(Bst):

    def _find_second_largest(self, node):
        if node.right is not None:
            if node.right.left is not None or node.right.right is not None:
                return self._find_second_largest(node.right)
            else:
                return node
        else:
            return self._find_right_most_node(node.left)

    def _find_right_most_node(self, node):
        if node.right is not None:
            return self._find_right_most_node(node.right)
        else:
            return node

    def find_second_largest(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        if self.root.right is None and self.root.left is None:
            raise ValueError('root must have at least one child')
        return self._find_second_largest(self.root)


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_bst_second_largest.py', "import unittest\n\n\nclass TestBstSecondLargest(unittest.TestCase):\n\n    def test_bst_second_largest(self):\n        bst = Solution(None)\n        self.assertRaises(TypeError, bst.find_second_largest)\n        root = Node(10)\n        bst = Solution(root)\n        node5 = bst.insert(5)\n        node15 = bst.insert(15)\n        node3 = bst.insert(3)\n        node8 = bst.insert(8)\n        node12 = bst.insert(12)\n        node20 = bst.insert(20)\n        node2 = bst.insert(2)\n        node4 = bst.insert(4)\n        node30 = bst.insert(30)\n        self.assertEqual(bst.find_second_largest(), node20)\n        root = Node(10)\n        bst = Solution(root)\n        node5 = bst.insert(5)\n        node3 = bst.insert(3)\n        node7 = bst.insert(7)\n        self.assertEqual(bst.find_second_largest(), node7)\n        print('Success: test_bst_second_largest')\n\n\ndef main():\n    test = TestBstSecondLargest()\n    test.test_bst_second_largest()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_bst_second_largest.py')

