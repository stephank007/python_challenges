#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a queue using two stacks.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Do we expect the methods to be enqueue and dequeue?
#     * Yes
# * Can we assume we already have a stack class that can be used for this problem?
#     * Yes
# * Can we push a None value to the Stack?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * Enqueue and dequeue on empty stack
# * Enqueue and dequeue on non-empty stack
# * Multiple enqueue in a row
# * Multiple dequeue in a row
# * Enqueue after a dequeue
# * Dequeue after an enqueue

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_from_stacks/queue_from_stacks_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../stack/stack.py')
get_ipython().run_line_magic('load', '../stack/stack.py')


# In[ ]:


class QueueFromStacks(object):

    def __init__(self):
        # TODO: Implement me
        pass

    def shift_stacks(self, source, destination):
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

# In[ ]:


# %load test_queue_from_stacks.py
import unittest


class TestQueueFromStacks(unittest.TestCase):

    def test_queue_from_stacks(self):
        print('Test: Dequeue on empty stack')
        queue = QueueFromStacks()
        self.assertEqual(queue.dequeue(), None)

        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        num_items = 3
        for i in range(0, num_items):
            queue.enqueue(i)

        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        self.assertEqual(queue.dequeue(), 0)

        print('Test: Multiple dequeue in a row')
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

        print('Test: Enqueue after a dequeue')
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)

        print('Success: test_queue_from_stacks')


def main():
    test = TestQueueFromStacks()
    test.test_queue_from_stacks()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_from_stacks/queue_from_stacks_solution.ipynb) for a discussion on algorithms and code solutions.
