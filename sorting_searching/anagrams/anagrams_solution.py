#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Sort an array of strings so all anagrams are next to each other.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Are there any other sorting requirements other than the grouping of anagrams?
#     * No
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * [] -> []
# * General case
#     * Input: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
#     * Result: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']

# ## Algorithm
# 
# <pre>
# Input: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
# 
# Sort the chars for each item:
# 
# 'ram' -> 'amr'
# 'act' -> 'act'
# 'arm' -> 'amr'
# 'abt' -> 'bat'
# 'cat' -> 'act'
# 'abt' -> 'tab'
# 
# Use a map of sorted chars to each item to group anagrams:
# 
# {
#     'amr': ['ram', 'arm'], 
#     'act': ['act', 'cat'], 
#     'abt': ['bat', 'tab']
# }
# 
# Result: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']
# </pre>
# 
# Complexity:
# * Time: O(k * n), due to the modified bucket sort
# * Space: O(n)

# ## Code

# In[1]:


from collections import OrderedDict


class Anagram(object):

    def group_anagrams(self, items):
        if items is None:
            raise TypeError('items cannot be None')
        if not items:
            return items
        anagram_map = OrderedDict()
        for item in items:
            # Use a tuple, which is hashable and
            # serves as the key in anagram_map
            sorted_chars = tuple(sorted(item))
            if sorted_chars in anagram_map:
                anagram_map[sorted_chars].append(item)
            else:
                anagram_map[sorted_chars] = [item]
        result = []
        for value in anagram_map.values():
            result.extend(value)
        return result


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_anagrams.py', "import unittest\n\n\nclass TestAnagrams(unittest.TestCase):\n\n    def test_group_anagrams(self):\n        anagram = Anagram()\n        self.assertRaises(TypeError, anagram.group_anagrams, None)\n        data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']\n        expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']\n        self.assertEqual(anagram.group_anagrams(data), expected)\n\n        print('Success: test_group_anagrams')\n\n\ndef main():\n    test = TestAnagrams()\n    test.test_group_anagrams()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_anagrams.py')

