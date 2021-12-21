#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a hash table with set, get, and remove methods.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# ### Hash Function
# 
# * Return key % table size
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)
# 
# ### Set
# 
# * Get hash index for lookup
# * If key exists, replace
# * Else, add
# 
# Complexity:
# * Time: O(1) average and best, O(n) worst
# * Space: O(1) space for newly added element
# 
# ### Get
# 
# * Get hash index for lookup
# * If key exists, return value
# * Else, raise KeyError
# 
# Complexity:
# * Time: O(1) average and best, O(n) worst
# * Space: O(1)
# 
# ### Remove
# 
# * Get hash index for lookup
# * If key exists, delete the item
# * Else, raise KeyError
# 
# Complexity:
# * Time: O(1) average and best, O(n) worst
# * Space: O(1)

# ## Code

# In[1]:


class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Key not found')


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_hash_map.py', 'import unittest\n\n\nclass TestHashMap(unittest.TestCase):\n\n    # TODO: It would be better if we had unit tests for each\n    # method in addition to the following end-to-end test\n    def test_end_to_end(self):\n        hash_table = HashTable(10)\n\n        print("Test: get on an empty hash table index")\n        self.assertRaises(KeyError, hash_table.get, 0)\n\n        print("Test: set on an empty hash table index")\n        hash_table.set(0, \'foo\')\n        self.assertEqual(hash_table.get(0), \'foo\')\n        hash_table.set(1, \'bar\')\n        self.assertEqual(hash_table.get(1), \'bar\')\n\n        print("Test: set on a non empty hash table index")\n        hash_table.set(10, \'foo2\')\n        self.assertEqual(hash_table.get(0), \'foo\')\n        self.assertEqual(hash_table.get(10), \'foo2\')\n\n        print("Test: set on a key that already exists")\n        hash_table.set(10, \'foo3\')\n        self.assertEqual(hash_table.get(0), \'foo\')\n        self.assertEqual(hash_table.get(10), \'foo3\')\n\n        print("Test: remove on a key that already exists")\n        hash_table.remove(10)\n        self.assertEqual(hash_table.get(0), \'foo\')\n        self.assertRaises(KeyError, hash_table.get, 10)\n\n        print("Test: remove on a key that doesn\'t exist")\n        self.assertRaises(KeyError, hash_table.remove, -1)\n\n        print(\'Success: test_end_to_end\')\n\n\ndef main():\n    test = TestHashMap()\n    test.test_end_to_end()\n\n\nif __name__ == \'__main__\':\n    main()')


# In[3]:


run -i test_hash_map.py


# In[ ]:




