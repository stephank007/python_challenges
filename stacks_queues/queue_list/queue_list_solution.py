#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a queue with enqueue and dequeue methods using a linked list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Pythonic-Code](#Pythonic-Code)

# ## Constraints
# 
# * If there is one item in the list, do you expect the head and tail pointers to both point to it?
#     * Yes
# * If there are no items on the list, do you expect the head and tail pointers to be None?
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
# ### Enqueue
# 
# * If the list is empty, set head and tail to node
# * Else, set tail to node
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Dequeue
# 
# * If the list is empty, return None
# * If the list has one node
#     * Save the head node's value
#     * Set head and tail to None
#     * Return the saved value
# * Else
#     * Save the head node's value
#     * Set head to its next node
#     * Return the saved value
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'queue_list.py', 'class Node(object):\n\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\n\nclass Queue(object):\n\n    def __init__(self):\n        self.head = None\n        self.tail = None\n\n    def enqueue(self, data):\n        node = Node(data)\n        # Empty list\n        if self.head is None and self.tail is None:\n            self.head = node\n            self.tail = node\n        else:\n            self.tail.next = node\n            self.tail = node\n\n    def dequeue(self):\n        # Empty list\n        if self.head is None and self.tail is None:\n            return None\n        data = self.head.data\n        # Remove only element from a one element list\n        if self.head == self.tail:\n            self.head = None\n            self.tail = None\n        else:\n            self.head = self.head.next\n        return data')


# In[2]:


get_ipython().run_line_magic('run', 'queue_list.py')


# ## Unit Test
# 
# 

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_queue_list.py', "import unittest\n\n\nclass TestQueue(unittest.TestCase):\n\n    # TODO: It would be better if we had unit tests for each\n    # method in addition to the following end-to-end test\n    def test_end_to_end(self):\n        print('Test: Dequeue an empty queue')\n        queue = Queue()\n        self.assertEqual(queue.dequeue(), None)\n\n        print('Test: Enqueue to an empty queue')\n        queue.enqueue(1)\n\n        print('Test: Dequeue a queue with one element')\n        self.assertEqual(queue.dequeue(), 1)\n\n        print('Test: Enqueue to a non-empty queue')\n        queue.enqueue(2)\n        queue.enqueue(3)\n        queue.enqueue(4)\n\n        print('Test: Dequeue a queue with more than one element')\n        self.assertEqual(queue.dequeue(), 2)\n        self.assertEqual(queue.dequeue(), 3)\n        self.assertEqual(queue.dequeue(), 4)\n\n        print('Success: test_end_to_end')\n\n\ndef main():\n    test = TestQueue()\n    test.test_end_to_end()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_queue_list.py')


# ## Pythonic-Code

# Source: https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues
# <pre>
# It is possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
# 
# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:
# 
# >>>
# >>> from collections import deque
# >>> queue = deque(["Eric", "John", "Michael"])
# >>> queue.append("Terry")           # Terry arrives
# >>> queue.append("Graham")          # Graham arrives
# >>> queue.popleft()                 # The first to arrive now leaves
# 'Eric'
# >>> queue.popleft()                 # The second to arrive now leaves
# 'John'
# >>> queue                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])
# </pre>
