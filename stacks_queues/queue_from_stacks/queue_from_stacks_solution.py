#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a queue using two stacks.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# We'll use two stacks (left and right) to implement the queue.  The left stack will be used for enqueue and the right stack will be used for dequeue.
# 
# To prevent multiple dequeue calls from needlessly shifting elements around between the stacks, we'll shift elements in a lazy manner.
# 
# ### Enqueue
# 
# * If right stack is not empty
#     * Shift the elements of the right stack to the left stack
# * Push the data to the left stack
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# ### Dequeue
# 
# * If the left stack is not empty
#     * Shift the elements of the left stack to the right stack
# * Pop from the right stack and return the data
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)
# 
# ### Shift Stacks
# 
# * While the source stack has elements:
#     * Pop from the source stack and push the data to the destination stack
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../stack/stack.py')


# In[2]:


class QueueFromStacks(object):

    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    def shift_stacks(self, source, destination):
        while source.peek() is not None:
            destination.push(source.pop())

    def enqueue(self, data):
        self.shift_stacks(self.right_stack, self.left_stack)
        self.left_stack.push(data)

    def dequeue(self):
        self.shift_stacks(self.left_stack, self.right_stack)
        return self.right_stack.pop()


# ## Unit Test
# 
# 

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_queue_from_stacks.py', "import unittest\n\n\nclass TestQueueFromStacks(unittest.TestCase):\n\n    def test_queue_from_stacks(self):\n        print('Test: Dequeue on empty stack')\n        queue = QueueFromStacks()\n        self.assertEqual(queue.dequeue(), None)\n\n        print('Test: Enqueue on empty stack')\n        print('Test: Enqueue on non-empty stack')\n        print('Test: Multiple enqueue in a row')\n        num_items = 3\n        for i in range(0, num_items):\n            queue.enqueue(i)\n\n        print('Test: Dequeue on non-empty stack')\n        print('Test: Dequeue after an enqueue')\n        self.assertEqual(queue.dequeue(), 0)\n\n        print('Test: Multiple dequeue in a row')\n        self.assertEqual(queue.dequeue(), 1)\n        self.assertEqual(queue.dequeue(), 2)\n\n        print('Test: Enqueue after a dequeue')\n        queue.enqueue(5)\n        self.assertEqual(queue.dequeue(), 5)\n\n        print('Success: test_queue_from_stacks')\n\n\ndef main():\n    test = TestQueueFromStacks()\n    test.test_queue_from_stacks()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_queue_from_stacks.py')

