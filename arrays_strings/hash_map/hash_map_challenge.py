#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a hash table with set, get, and remove methods.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * For simplicity, are the keys integers only?
#     * Yes
# * For collision resolution, can we use chaining?
#     * Yes
# * Do we have to worry about load factors?
#     * No
# * Do we have to validate inputs?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * `get` no matching key -> KeyError exception
# * `get` matching key -> value
# * `set` no matching key -> new key, value
# * `set` matching key -> update value
# * `remove` no matching key -> KeyError exception
# * `remove` matching key -> remove key, value

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/hash_map/hash_map_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Item(object):

    def __init__(self, key, value):
        # TODO: Implement me
        pass


class HashTable(object):

    def __init__(self, size):
        # TODO: Implement me
        pass

    def _hash_function(self, key):
        # TODO: Implement me
        pass

    def set(self, key, value):
        # TODO: Implement me
        pass

    def get(self, key):
        # TODO: Implement me
        pass

    def remove(self, key):
        # TODO: Implement me
        pass


# ## Unit Test

# 
# 
# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_hash_map.py
import unittest


class TestHashMap(unittest.TestCase):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")
        self.assertRaises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'foo')
        self.assertEqual(hash_table.get(0), 'foo')
        hash_table.set(1, 'bar')
        self.assertEqual(hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'foo2')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")
        hash_table.set(10, 'foo3')
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertEqual(hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")
        hash_table.remove(10)
        self.assertEqual(hash_table.get(0), 'foo')
        self.assertRaises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        self.assertRaises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


def main():
    test = TestHashMap()
    test.test_end_to_end()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/hash_map/hash_map_solution.ipynb) for a discussion on algorithms and code solutions.
