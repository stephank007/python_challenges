#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a linked list with insert, append, find, delete, length, and print methods.
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
# * Do we keep track of the tail or just the head?
#     * Just the head
# * Can we insert None values?
#     * No

# ## Test Cases
# 
# ### Insert to Front
# 
# * Insert a None
# * Insert in an empty list
# * Insert in a list with one element or more elements
# 
# ### Append
# 
# * Append a None
# * Append in an empty list
# * Insert in a list with one element or more elements
# 
# ### Find
# 
# * Find a None
# * Find in an empty list
# * Find in a list with one element or more matching elements
# * Find in a list with no matches
# 
# ### Delete
# 
# * Delete a None
# * Delete in an empty list
# * Delete in a list with one element or more matching elements
# * Delete in a list with no matches
# 
# ### Length
# 
# * Length of zero or more elements
# 
# ### Print
# 
# * Print an empty list
# * Print a list with one or more elements

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/linked_list/linked_list_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Node(object):

    def __init__(self, data, next_node=None):
        pass
        # TODO: Implement me

    def __str__(self):
        pass
        # TODO: Implement me


class LinkedList(object):

    def __init__(self, head=None):
        pass
        # TODO: Implement me

    def __len__(self):
        pass
        # TODO: Implement me

    def insert_to_front(self, data):
        pass
        # TODO: Implement me

    def append(self, data):
        pass
        # TODO: Implement me

    def find(self, data):
        pass
        # TODO: Implement me

    def delete(self, data):
        pass
        # TODO: Implement me

    def print_list(self):
        pass
        # TODO: Implement me

    def get_all_data(self):
        pass
        # TODO: Implement me


# ## Unit Test

# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_linked_list.py
import unittest


class TestLinkedList(unittest.TestCase):

    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = LinkedList(None)
        linked_list.insert_to_front(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(linked_list.get_all_data(), ['bc', 'a', 10])

        print('Success: test_insert_to_front\n')

    def test_append(self):
        print('Test: append on an empty list')
        linked_list = LinkedList(None)
        linked_list.append(10)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append a None')
        linked_list.append(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        self.assertEqual(linked_list.get_all_data(), [10, 'a', 'bc'])

        print('Success: test_append\n')

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        self.assertEqual(node, None)

        print('Test: find a None')
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        self.assertEqual(node, None)

        print('Test: find general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        self.assertEqual(str(node), 'a')

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        self.assertEqual(node, None)

        print('Success: test_find\n')

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = LinkedList(None)
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: delete a None')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.delete(None)
        self.assertEqual(linked_list.get_all_data(), [10])

        print('Test: delete general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        self.assertEqual(linked_list.get_all_data(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = LinkedList(None)
        self.assertEqual(len(linked_list), 0)

        print('Test: len general case')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        self.assertEqual(len(linked_list), 3)

        print('Success: test_len\n')


def main():
    test = TestLinkedList()
    test.test_insert_to_front()
    test.test_append()
    test.test_find()
    test.test_delete()
    test.test_len()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/linked_list/linked_list_solution.ipynb) for a discussion on algorithms and code solutions.
