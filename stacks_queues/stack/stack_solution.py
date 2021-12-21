#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a stack with push, pop, peek, and is_empty methods using a linked list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Pythonic-Code](#Pythonic-Code)

# ## Constraints
# 
# * If we pop on an empty stack, do we return None?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# ### Push
# 
# * Push to empty stack
# * Push to non-empty stack
# 
# ### Pop
# 
# * Pop on empty stack
# * Pop on single element stack
# * Pop on multiple element stack
# 
# ### Peek
# 
# * Peek on empty stack
# * Peek on one or more element stack
# 
# ### Is Empty
# 
# * Is empty on empty stack
# * Is empty on one or more element stack

# ## Algorithm
# 
# ### Push
# 
# * Create new node with value
# * Set node's next to top
# * Set top to node
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Pop
# 
# * If stack is empty, return None
# * Else 
#     * Save top's value
#     * Set top to top.next
#     * Return saved value
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Peek
# 
# * If stack is empty, return None
# * Else return top's value
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Is Empty
# * If peek has a value, return False
# * Else return True
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'stack.py', 'class Node(object):\n\n    def __init__(self, data, next=None):\n        self.data = data\n        self.next = next\n\n\nclass Stack(object):\n\n    def __init__(self, top=None):\n        self.top = top\n\n    def push(self, data):\n        self.top = Node(data, self.top)\n\n    def pop(self):\n        if self.top is None:\n            return None\n        data = self.top.data\n        self.top = self.top.next\n        return data\n\n    def peek(self):\n        return self.top.data if self.top is not None else None\n\n    def is_empty(self):\n        return self.peek() is None')


# In[2]:


get_ipython().run_line_magic('run', 'stack.py')


# ## Unit Test
# 
# 

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_stack.py', "import unittest\n\n\nclass TestStack(unittest.TestCase):\n\n    # TODO: It would be better if we had unit tests for each\n    # method in addition to the following end-to-end test\n    def test_end_to_end(self):\n        print('Test: Empty stack')\n        stack = Stack()\n        self.assertEqual(stack.peek(), None)\n        self.assertEqual(stack.pop(), None)\n\n        print('Test: One element')\n        top = Node(5)\n        stack = Stack(top)\n        self.assertEqual(stack.pop(), 5)\n        self.assertEqual(stack.peek(), None)\n\n        print('Test: More than one element')\n        stack = Stack()\n        stack.push(1)\n        stack.push(2)\n        stack.push(3)\n        self.assertEqual(stack.pop(), 3)\n        self.assertEqual(stack.peek(), 2)\n        self.assertEqual(stack.pop(), 2)\n        self.assertEqual(stack.peek(), 1)\n        self.assertEqual(stack.is_empty(), False)\n        self.assertEqual(stack.pop(), 1)\n        self.assertEqual(stack.peek(), None)\n        self.assertEqual(stack.is_empty(), True)\n\n        print('Success: test_end_to_end')\n\n\ndef main():\n    test = TestStack()\n    test.test_end_to_end()\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_stack.py')


# ## Pythonic-Code

# Source: https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks
# <pre>
# 5.1.1. Using Lists as Stacks
# The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. For example:
# 
# >>> stack = [3, 4, 5]
# >>> stack.append(6)
# >>> stack.append(7)
# >>> stack
# [3, 4, 5, 6, 7]
# >>> stack.pop()
# 7
# >>> stack
# [3, 4, 5, 6]
# >>> stack.pop()
# 6
# >>> stack.pop()
# 5
# >>> stack
# [3, 4]
# </pre>
