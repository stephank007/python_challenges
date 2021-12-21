#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a queue with enqueue and dequeue methods using a linked list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Pythonic-Code](#Pythonic-Code)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * If there is one item in the list, do you expect the first and last pointers to both point to it?
#     * Yes
# * If there are no items on the list, do you expect the first and last pointers to be None?
#     * Yes
# * If you dequeue on an empty queue, does that return None?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# ### Enqueue
# 
# * Enqueue to an empty queue
# * Enqueue to a non-empty queue
# 
# ### Dequeue
# 
# * Dequeue an empty queue -> None
# * Dequeue a queue with one element
# * Dequeue a queue with more than one element

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_list/queue_list_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Node(object):

    def __init__(self, data):
        # TODO: Implement me
        pass


class Queue(object):

    def __init__(self):
        # TODO: Implement me
        pass

    def enqueue(self, data):
        # TODO: Implement me
        pass

    def dequeue(self):
        # TODO: Implement me
        pass


# ## Unit Test
# 
# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_queue_list.py
import unittest


class TestQueue(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Dequeue an empty queue')
        queue = Queue()
        self.assertEqual(queue.dequeue(), None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)

        print('Test: Dequeue a queue with one element')
        self.assertEqual(queue.dequeue(), 1)

        print('Test: Enqueue to a non-empty queue')
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        print('Test: Dequeue a queue with more than one element')
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

        print('Success: test_end_to_end')


def main():
    test = TestQueue()
    test.test_end_to_end()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_list/queue_list_solution.ipynb) for a discussion on algorithms and code solutions.
