#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

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
# * Initialize queue with root
# * While queue is not empty
#     * Dequeue and print the node
#     * Queue the left child
#     * Queue the right child
# 
# Complexity:
# * Time: O(n)
# * Space: O(n), extra space for the queue

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../bst/bst.py')


# In[2]:


from collections import deque


class BstBfs(Bst):

    def bfs(self, visit_func):
        if self.root is None:
            raise TypeError('root is None')
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            visit_func(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


# ## Unit Test

# In[3]:


get_ipython().run_line_magic('run', '../utils/results.py')


# In[4]:


get_ipython().run_cell_magic('writefile', 'test_bfs.py', "import unittest\n\n\nclass TestBfs(unittest.TestCase):\n\n    def __init__(self, *args, **kwargs):\n        super(TestBfs, self).__init__()\n        self.results = Results()\n\n    def test_bfs(self):\n        bst = BstBfs(Node(5))\n        bst.insert(2)\n        bst.insert(8)\n        bst.insert(1)\n        bst.insert(3)\n        bst.bfs(self.results.add_result)\n        self.assertEqual(str(self.results), '[5, 2, 8, 1, 3]')\n\n        print('Success: test_bfs')\n\n\ndef main():\n    test = TestBfs()\n    test.test_bfs()\n\n\nif __name__ == '__main__':\n    main()")


# In[5]:


get_ipython().run_line_magic('run', '-i test_bfs.py')

