#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
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
# * Do we expect the function to return a new list?
#     * Yes
# * Can we assume the input x is valid?
#     * Yes
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes
# * Can we create additional data structures?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * Empty list -> []
# * One element list -> [element]
# * Left linked list is empty
# * Right linked list is empty
# * General case
#     * Partition = 10
#     * Input:  4, 3, 7, 8, 10, 1, 10, 12
#     * Output: 4, 3, 7, 8, 1, 10, 10, 12

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/partition/partition_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


get_ipython().run_line_magic('run', '../linked_list/linked_list.py')
get_ipython().run_line_magic('load', '../linked_list/linked_list.py')


# In[ ]:


class MyLinkedList(LinkedList):

    def partition(self, data):
        # TODO: Implement me
        pass


# ## Unit Test

# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_partition.py
import unittest


class TestPartition(unittest.TestCase):

    def test_partition(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(0)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        self.assertEqual(partitioned_list.get_all_data(),
                     [4, 3, 8, 1, 10, 10, 13, 14, 12])

        print('Success: test_partition')


def main():
    test = TestPartition()
    test.test_partition()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/partition/partition_solution.ipynb) for a discussion on algorithms and code solutions.
