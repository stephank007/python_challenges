#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

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
# ## Test Cases
# 
# Note:
# 
# * This following are all forms of depth-first traversals
# 
# ### In-Order Traversal
# 
# * Recursively call in-order traversal on the left child
# * Visit the current node
# * Recursively call in-order traversal on the right child
# 
# Complexity:
# * Time: O(n)
# * Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach
# 
# ### Pre-Order Traversal
# 
# * Visit the current node
# * Recursively call pre-order traversal on the left child
# * Recursively call pre-order traversal on the right child
# 
# Complexity:
# * Time: O(n)
# * Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach
# 
# ### Post-Order Traversal
# 
# * Recursively call post-order traversal on the left child
# * Recursively call post-order traversal on the right child
# * Visit the current node
# 
# Complexity:
# * Time: O(n)
# * Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


class BstDfs(Bst):

    def in_order_traversal(self, node, visit_func):
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        if node is not None:
            visit_func(node)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self, node, visit_func):
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node)


# ## Unit Test

# In[3]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[4]:


get_ipython().run_cell_magic('writefile', 'test_dfs.py', 'import unittest\n\n\nclass TestDfs(unittest.TestCase):\n\n    def __init__(self, *args, **kwargs):\n        super(TestDfs, self).__init__()\n        self.results = Results()\n\n    def test_dfs(self):\n        bst = BstDfs(Node(5))\n        bst.insert(2)\n        bst.insert(8)\n        bst.insert(1)\n        bst.insert(3)\n\n        bst.in_order_traversal(bst.root, self.results.add_result)\n        self.assertEqual(str(self.results), "[1, 2, 3, 5, 8]")\n        self.results.clear_results()\n\n        bst.pre_order_traversal(bst.root, self.results.add_result)\n        self.assertEqual(str(self.results), "[5, 2, 1, 3, 8]")\n        self.results.clear_results()\n\n        bst.post_order_traversal(bst.root, self.results.add_result)\n        self.assertEqual(str(self.results), "[1, 3, 2, 8, 5]")\n        self.results.clear_results()\n\n        bst = BstDfs(Node(1))\n        bst.insert(2)\n        bst.insert(3)\n        bst.insert(4)\n        bst.insert(5)\n\n        bst.in_order_traversal(bst.root, self.results.add_result)\n        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")\n        self.results.clear_results()\n\n        bst.pre_order_traversal(bst.root, self.results.add_result)\n        self.assertEqual(str(self.results), "[1, 2, 3, 4, 5]")\n        self.results.clear_results()\n\n        bst.post_order_traversal(bst.root, self.results.add_result)\n        self.assertEqual(str(self.results), "[5, 4, 3, 2, 1]")\n\n        print(\'Success: test_dfs\')\n\n\ndef main():\n    test = TestDfs()\n    test.test_dfs()\n\n\nif __name__ == \'__main__\':\n    main()')


# In[5]:


get_ipython().run_line_magic('run', '-i test_dfs.py')

