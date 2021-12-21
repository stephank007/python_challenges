#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a priority queue backed by an array.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

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
# Refer to the [Solution Notebook](priority_queue_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        # TODO: Implement me
        pass

    def extract_min(self):
        # TODO: Implement me
        pass

    def decrease_key(self, obj, new_key):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_priority_queue.py
import unittest


class TestPriorityQueue(unittest.TestCase):

    def test_priority_queue(self):
        priority_queue = PriorityQueue()
        self.assertEqual(priority_queue.extract_min(), None)
        priority_queue.insert(PriorityQueueNode('a', 20))
        priority_queue.insert(PriorityQueueNode('b', 5))
        priority_queue.insert(PriorityQueueNode('c', 15))
        priority_queue.insert(PriorityQueueNode('d', 22))
        priority_queue.insert(PriorityQueueNode('e', 40))
        priority_queue.insert(PriorityQueueNode('f', 3))
        priority_queue.decrease_key('f', 2)
        priority_queue.decrease_key('a', 19)
        mins = []
        while priority_queue.array:
            mins.append(priority_queue.extract_min().key)
        self.assertEqual(mins, [2, 5, 15, 19, 22, 40])
        print('Success: test_min_heap')


def main():
    test = TestPriorityQueue()
    test.test_priority_queue()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](priority_queue_solution.ipynb) for a discussion on algorithms and code solutions.
