#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a min heap with extract_min and insert methods.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

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
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/min_heap/min_heap_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class MinHeap(object):

    def __init__(self):
        # TODO: Implement me
        pass

    def extract_min(self):
        # TODO: Implement me
        pass    

    def peek_min(self):
        # TODO: Implement me
        pass

    def insert(self, data):
        # TODO: Implement me
        pass

    def _bubble_up(self, index):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_min_heap.py
import unittest


class TestMinHeap(unittest.TestCase):

    def test_min_heap(self):
        heap = MinHeap()
        self.assertEqual(heap.peek_min(), None)
        self.assertEqual(heap.extract_min(), None)
        heap.insert(20)
        self.assertEqual(heap.peek_min(), 20)
        heap.insert(5)
        self.assertEqual(heap.peek_min(), 5)
        heap.insert(15)
        heap.insert(22)
        heap.insert(40)
        heap.insert(5)
        self.assertEqual(heap.peek_min(), 5)
        heap.insert(3)
        self.assertEqual(heap.peek_min(), 3)
        self.assertEqual(heap.extract_min(), 3)
        self.assertEqual(heap.peek_min(), 5)
        print('Success: test_min_heap')

        
def main():
    test = TestMinHeap()
    test.test_min_heap()

    
if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/min_heap/min_heap_solution.ipynb) for a discussion on algorithms and code solutions.
