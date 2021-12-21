#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a priority queue backed by an array.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Do we expect the methods to be insert, extract_min, and decrease_key?
#     * Yes
# * Can we assume there aren't any duplicate keys?
#     * Yes
# * Do we need to validate inputs?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# ### insert
# 
# * `insert` general case -> inserted node
# 
# ### extract_min
# 
# * `extract_min` from an empty list -> None
# * `extract_min` general case -> min node
# 
# ### decrease_key
# 
# * `decrease_key` an invalid key -> None
# * `decrease_key` general case -> updated node

# ## Algorithm
# 
# ### insert
# 
# * Append to the internal array.
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### extract_min
# 
# * Loop through each item in the internal array
#     * Update the min value as needed
# * Remove the min element from the array and return it
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)
# 
# ### decrease_key
# 
# * Loop through each item in the internal array to find the matching input
#     * Update the matching element's key
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'priority_queue.py', "import sys\n\n\nclass PriorityQueueNode(object):\n\n    def __init__(self, obj, key):\n        self.obj = obj\n        self.key = key\n\n    def __repr__(self):\n        return str(self.obj) + ': ' + str(self.key)\n\n\nclass PriorityQueue(object):\n\n    def __init__(self):\n        self.array = []\n\n    def __len__(self):\n        return len(self.array)\n\n    def insert(self, node):\n        self.array.append(node)\n        return self.array[-1]\n\n    def extract_min(self):\n        if not self.array:\n            return None\n        minimum = sys.maxsize\n        for index, node in enumerate(self.array):\n            if node.key < minimum:\n                minimum = node.key\n                minimum_index = index\n        return self.array.pop(minimum_index)\n\n    def decrease_key(self, obj, new_key):\n        for node in self.array:\n            if node.obj is obj:\n                node.key = new_key\n                return node\n        return None")


# In[2]:


get_ipython().run_line_magic('run', 'priority_queue.py')


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_priority_queue.py', "import unittest\n\n\nclass TestPriorityQueue(unittest.TestCase):\n\n    def test_priority_queue(self):\n        priority_queue = PriorityQueue()\n        self.assertEqual(priority_queue.extract_min(), None)\n        priority_queue.insert(PriorityQueueNode('a', 20))\n        priority_queue.insert(PriorityQueueNode('b', 5))\n        priority_queue.insert(PriorityQueueNode('c', 15))\n        priority_queue.insert(PriorityQueueNode('d', 22))\n        priority_queue.insert(PriorityQueueNode('e', 40))\n        priority_queue.insert(PriorityQueueNode('f', 3))\n        priority_queue.decrease_key('f', 2)\n        priority_queue.decrease_key('a', 19)\n        mins = []\n        while priority_queue.array:\n            mins.append(priority_queue.extract_min().key)\n        self.assertEqual(mins, [2, 5, 15, 19, 22, 40])\n        print('Success: test_min_heap')\n\n\ndef main():\n    test = TestPriorityQueue()\n    test.test_priority_queue()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_priority_queue.py')

