#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Sort a stack.  You can use another stack as a buffer.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * When sorted, should the largest element be at the top or bottom?
#     * Top
# * Can you have duplicate values like 5, 5?
#     * Yes
# * Can we assume we already have a stack class that can be used for this problem?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * Empty stack -> None
# * One element stack
# * Two or more element stack (general case)
# * Already sorted stack

# ## Algorithm
# 
# * Our buffer will hold elements in reverse sorted order, smallest at the top
# * Store the current top element in a temp variable
# * While stack is not empty
#     * While buffer is not empty or buffer top is > than temp
#         * Move buffer top to stack
#     * Move temp to top of buffer
# * Return buffer
# 
# Complexity:
# * Time: O(n^2)
# * Space: O(n)

# ## Code

# In[1]:


get_ipython().run_line_magic('run', '../stack/stack.py')


# In[2]:


class MyStack(Stack):

    def sort(self):
        buff = MyStack()
        while not self.is_empty():
            temp = self.pop()
            if buff.is_empty() or temp >= buff.peek():
                buff.push(temp)
            else:
                while not buff.is_empty() and temp < buff.peek():
                    self.push(buff.pop())
                buff.push(temp)
        return buff


# The solution can be further simplified:

# In[3]:


class MyStackSimplified(Stack):

    def sort(self):
        buff = MyStack()
        while not self.is_empty():
            temp = self.pop()
            while not buff.is_empty() and temp < buff.peek():
                self.push(buff.pop())
            buff.push(temp)
        return buff


# ## Unit Test
# 
# 

# In[4]:


get_ipython().run_cell_magic('writefile', 'test_sort_stack.py', "from random import randint\nimport unittest\n\n\nclass TestSortStack(unittest.TestCase):\n\n    def get_sorted_stack(self, stack, numbers):\n        for x in numbers:\n            stack.push(x)\n        sorted_stack = stack.sort()\n        return sorted_stack\n\n    def test_sort_stack(self, stack):\n        print('Test: Empty stack')\n        sorted_stack = self.get_sorted_stack(stack, [])\n        self.assertEqual(sorted_stack.pop(), None)\n\n        print('Test: One element stack')\n        sorted_stack = self.get_sorted_stack(stack, [1])\n        self.assertEqual(sorted_stack.pop(), 1)\n\n        print('Test: Two or more element stack (general case)')\n        num_items = 10\n        numbers = [randint(0, 10) for x in range(num_items)]\n        sorted_stack = self.get_sorted_stack(stack, numbers)\n        sorted_numbers = []\n        for _ in range(num_items):\n            sorted_numbers.append(sorted_stack.pop())\n        self.assertEqual(sorted_numbers, sorted(numbers, reverse=True))\n\n        print('Success: test_sort_stack')\n\n\ndef main():\n    test = TestSortStack()\n    test.test_sort_stack(MyStack())\n    test.test_sort_stack(MyStackSimplified())\n\n\nif __name__ == '__main__':\n    main()")


# In[5]:


get_ipython().run_line_magic('run', '-i test_sort_stack.py')

