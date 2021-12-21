#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a min heap with extract_min and insert methods.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume the inputs are ints?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * Extract min of an empty tree
# * Extract min general case
# * Insert into an empty tree
# * Insert general case (left and right insert)
# 
# <pre>
#           _5_
#         /     \
#        20     15
#       / \    /  \
#      22  40 25
#      
# extract_min(): 5
# 
#           _15_
#         /      \
#        20      25
#       / \     /  \
#      22  40 
# 
# insert(2):
# 
#           _2_
#         /     \
#        20      5
#       / \     / \
#      22  40  25  15
# </pre>

# ## Algorithm
# 
# A heap is a complete binary tree where each node is smaller than its children.
# 
# ### extract_min
# 
# <pre>
#           _5_
#         /     \
#        20     15
#       / \    /  \
#      22  40 25
# 
# Save the root as the value to be returned: 5
# Move the right most element to the root: 25
# 
#           _25_
#         /      \
#        20      15
#       / \     /  \
#      22  40 
# 
# Bubble down 25: Swap 25 and 15 (the smaller child)
# 
#           _15_
#         /      \
#        20      25
#       / \     /  \
#      22  40 
# 
# Return 5
# </pre>
# 
# We'll use an array to represent the tree, here are the indices:
# 
# <pre>
#           _0_
#         /     \
#        1       2
#       / \     / \
#      3   4   
# </pre>
# 
# To get to a child, we take 2 * index + 1 (left child) or 2 * index + 2 (right child).
# 
# For example, the right child of index 1 is 2 * 1 + 2 = 4.
# 
# Complexity:
# * Time: O(lg(n))
# * Space: O(lg(n)) for the recursion depth (tree height), or O(1) if using an iterative approach
# 
# ### insert
# 
# <pre>
#           _5_
#         /     \
#        20     15
#       / \    /  \
#      22  40 25
# 
# insert(2):
# Insert at the right-most spot to maintain the heap property.
# 
#           _5_
#         /     \
#        20     15
#       / \    /  \
#      22  40 25   2
# 
# Bubble up 2: Swap 2 and 15
# 
#           _5_
#         /     \
#        20     2
#       / \    / \
#      22  40 25  15
# 
# Bubble up 2: Swap 2 and 5
# 
#           _2_
#         /     \
#        20     5
#       / \    / \
#      22  40 25  15
# </pre>
# 
# We'll use an array to represent the tree, here are the indices:
# 
# <pre>
#           _0_
#         /     \
#        1       2
#       / \     / \
#      3   4   5   6
# </pre>
# 
# To get to a parent, we take (index - 1) // 2.  
# 
# For example, the parent of index 6 is (6 - 1) // 2 = 2.
# 
# Complexity:
# * Time: O(lg(n))
# * Space: O(lg(n)) for the recursion depth (tree height), or O(1) if using an iterative approach

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'min_heap.py', "from __future__ import division\n\nimport sys\n\n\nclass MinHeap(object):\n\n    def __init__(self):\n        self.array = []\n\n    def __len__(self):\n        return len(self.array)\n\n    def extract_min(self):\n        if not self.array:\n            return None\n        if len(self.array) == 1:\n            return self.array.pop(0)\n        minimum = self.array[0]\n        # Move the last element to the root\n        self.array[0] = self.array.pop(-1)\n        self._bubble_down(index=0)\n        return minimum\n\n    def peek_min(self):\n        return self.array[0] if self.array else None\n\n    def insert(self, key):\n        if key is None:\n            raise TypeError('key cannot be None')\n        self.array.append(key)\n        self._bubble_up(index=len(self.array) - 1)\n\n    def _bubble_up(self, index):\n        if index == 0:\n            return\n        index_parent = (index - 1) // 2\n        if self.array[index] < self.array[index_parent]:\n            # Swap the indices and recurse\n            self.array[index], self.array[index_parent] = \\\n                self.array[index_parent], self.array[index]\n            self._bubble_up(index_parent)\n\n    def _bubble_down(self, index):\n        min_child_index = self._find_smaller_child(index)\n        if min_child_index == -1:\n            return\n        if self.array[index] > self.array[min_child_index]:\n            # Swap the indices and recurse\n            self.array[index], self.array[min_child_index] = \\\n                self.array[min_child_index], self.array[index]\n            self._bubble_down(min_child_index)\n\n    def _find_smaller_child(self, index):\n        left_child_index = 2 * index + 1\n        right_child_index = 2 * index + 2\n        # No right child\n        if right_child_index >= len(self.array):\n            # No left child\n            if left_child_index >= len(self.array):\n                return -1\n            # Left child only\n            else:\n                return left_child_index\n        else:\n            # Compare left and right children\n            if self.array[left_child_index] < self.array[right_child_index]:\n                return left_child_index\n            else:\n                return right_child_index")


# In[2]:


get_ipython().run_line_magic('run', 'min_heap.py')


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_min_heap.py', "import unittest\n\n\nclass TestMinHeap(unittest.TestCase):\n\n    def test_min_heap(self):\n        heap = MinHeap()\n        self.assertEqual(heap.peek_min(), None)\n        self.assertEqual(heap.extract_min(), None)\n        heap.insert(20)\n        self.assertEqual(heap.array[0], 20)\n        heap.insert(5)\n        self.assertEqual(heap.array[0], 5)\n        self.assertEqual(heap.array[1], 20)\n        heap.insert(15)\n        self.assertEqual(heap.array[0], 5)\n        self.assertEqual(heap.array[1], 20)\n        self.assertEqual(heap.array[2], 15)\n        heap.insert(22)\n        self.assertEqual(heap.array[0], 5)\n        self.assertEqual(heap.array[1], 20)\n        self.assertEqual(heap.array[2], 15)\n        self.assertEqual(heap.array[3], 22)\n        heap.insert(40)\n        self.assertEqual(heap.array[0], 5)\n        self.assertEqual(heap.array[1], 20)\n        self.assertEqual(heap.array[2], 15)\n        self.assertEqual(heap.array[3], 22)\n        self.assertEqual(heap.array[4], 40)\n        heap.insert(3)\n        self.assertEqual(heap.array[0], 3)\n        self.assertEqual(heap.array[1], 20)\n        self.assertEqual(heap.array[2], 5)\n        self.assertEqual(heap.array[3], 22)\n        self.assertEqual(heap.array[4], 40)\n        self.assertEqual(heap.array[5], 15)\n        mins = []\n        while heap:\n            mins.append(heap.extract_min())\n        self.assertEqual(mins, [3, 5, 15, 20, 22, 40])\n        print('Success: test_min_heap')\n\n        \ndef main():\n    test = TestMinHeap()\n    test.test_min_heap()\n\n    \nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_min_heap.py')

