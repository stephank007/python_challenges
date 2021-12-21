#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the kth to last element of a linked list.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume this is a non-circular, singly linked list?
#     * Yes
# * Can we assume k is a valid integer?
#     * Yes
# * If k = 0, does this return the last element?
#     * Yes
# * What happens if k is greater than or equal to the length of the linked list?
#     * Return None
# * Can you use additional data structures?
#     * No
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes

# ## Test Cases
# 
# * Empty list -> None
# * k is >= the length of the linked list -> None
# * One element, k = 0 -> element
# * General case with many elements, k < length of linked list

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/kth_to_last_elem/kth_to_last_elem_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../linked_list/linked_list.py')
get_ipython().run_line_magic('load', '../linked_list/linked_list.py')


# In[ ]:


class MyLinkedList(LinkedList):

    def kth_to_last_elem(self, k):
        # TODO: Implement me
        pass


# ## Unit Test

# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_kth_to_last_elem.py
import unittest


class Test(unittest.TestCase):

    def test_kth_to_last_elem(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        self.assertEqual(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        self.assertEqual(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyLinkedList(head)
        self.assertEqual(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        self.assertEqual(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')


def main():
    test = Test()
    test.test_kth_to_last_elem()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/kth_to_last_elem/kth_to_last_elem_solution.ipynb) for a discussion on algorithms and code solutions.
