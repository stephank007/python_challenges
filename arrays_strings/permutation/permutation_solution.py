#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine if a string is a permutation of another string.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm: Compare Sorted Strings](#Algorithm:-Compare-Sorted-Strings)
# * [Code: Compare Sorted Strings](#Code:-Compare-Sorted-Strings)
# * [Algorithm: Hashmap Lookup](#Algorithm:-Hash-Map-Lookup)
# * [Code: Hashmap Lookup](#Code:-Hash-Map-Lookup)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can we assume the string is ASCII?
#     * Yes
#     * Note: Unicode strings could require special handling depending on your language
# * Is whitespace important?
#     * Yes
# * Is this case sensitive?  'Nib', 'bin' is not a match?
#     * Yes
# * Can we use additional data structures?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * One or more None inputs -> False
# * One or more empty strings -> False
# * 'Nib', 'bin' -> False
# * 'act', 'cat' -> True
# * 'a ct', 'ca t' -> True
# * 'dog', 'doggo' -> False

# ## Algorithm: Compare Sorted Strings
# 
# Permutations contain the same strings but in different orders.  This approach could be slow for large strings due to sorting.
# 
# * Sort both strings
# * If both sorted strings are equal
#     * return True
# * Else
#     * return False
# 
# Complexity:
# * Time: O(n log n) from the sort, in general
# * Space: O(n)

# ## Code: Compare Sorted Strings

# In[1]:


class Permutations(object):

    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        return sorted(str1) == sorted(str2)


# ## Algorithm: Hash Map Lookup
# 
# We'll keep a hash map (dict) to keep track of characters we encounter.  
# 
# Steps:
# * Scan each character
# * For each character in each string:
#     * If the character does not exist in a hash map, add the character to a hash map
#     * Else, increment the character's count
# * If the hash maps for each string are equal
#     * Return True
# * Else
#     * Return False
# 
# Notes:
# * Since the characters are in ASCII, we could potentially use an array of size 128 (or 256 for extended ASCII), where each array index is equivalent to an ASCII value
# * Instead of using two hash maps, you could use one hash map and increment character values based on the first string and decrement based on the second string
# * You can short circuit if the lengths of each string are not equal, although len() in Python is generally O(1) unlike other languages like C where getting the length of a string is O(n)
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)

# ## Code: Hash Map Lookup

# In[2]:


from collections import defaultdict


class PermutationsAlt(object):

    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        unique_counts1 = defaultdict(int)
        unique_counts2 = defaultdict(int)
        for char in str1:
            unique_counts1[char] += 1
        for char in str2:
            unique_counts2[char] += 1
        return unique_counts1 == unique_counts2


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_permutation_solution.py', "import unittest\n\n\nclass TestPermutation(unittest.TestCase):\n\n    def test_permutation(self, func):\n        self.assertEqual(func(None, 'foo'), False)\n        self.assertEqual(func('', 'foo'), False)\n        self.assertEqual(func('Nib', 'bin'), False)\n        self.assertEqual(func('act', 'cat'), True)\n        self.assertEqual(func('a ct', 'ca t'), True)\n        self.assertEqual(func('dog', 'doggo'), False)\n        print('Success: test_permutation')\n\n\ndef main():\n    test = TestPermutation()\n    permutations = Permutations()\n    test.test_permutation(permutations.is_permutation)\n    try:\n        permutations_alt = PermutationsAlt()\n        test.test_permutation(permutations_alt.is_permutation)\n    except NameError:\n        # Alternate solutions are only defined\n        # in the solutions file\n        pass\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


run -i test_permutation_solution.py

