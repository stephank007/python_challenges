#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find all permutations of an input string.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Can the input have duplicates?
#     * Yes
# * Can the output have duplicates?
#     * No
# * Is the output a list of strings?
#     * Yes
# * Do we have to output the results in sorted order?
#     * No
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> None
# * '' -> ''
# * 'AABC' -> ['AABC', 'AACB', 'ABAC', 'ABCA',
#              'ACAB', 'ACBA', 'BAAC', 'BACA',
#              'BCAA', 'CAAB', 'CABA', 'CBAA']
# </pre>

# ## Algorithm
# 
# * Build a dictionary of {chars: counts} where counts is the number of times each char is found in the input
# * Loop through each item in the dictionary
#     * If the counts is 0, continue
#     * Decrement the current char's count in the dictionary
#     * Add the current char to the current results
#     * If the current result is the same length as the input, add it to the results
#     * Else, recurse
#     * Backtrack by:
#         * Removing the just added current char from the current results
#         * Incrementing the current char's count in the dictionary
# 
# Complexity:
# * Time: O(n!)
# * Space: O(n!) since we are storing the results in an array, or O(n) if we are just printing each result

# ## Code

# In[1]:


from collections import OrderedDict


class Permutations(object):

    def _build_counts_map(self, string):
        counts_map = OrderedDict()
        for char in string:
            if char in counts_map:
                counts_map[char] += 1
            else:
                counts_map[char] = 1
        return counts_map

    def find_permutations(self, string):
        if string is None or string == '':
            return string
        counts_map = self._build_counts_map(string)
        curr_results = []
        results = []
        self._find_permutations(counts_map, curr_results, results, len(string))
        return results

    def _find_permutations(self, counts_map, curr_result,
                           results, input_length):
        for char in counts_map:
            if counts_map[char] == 0:
                continue
            curr_result.append(char)
            counts_map[char] -= 1
            if len(curr_result) == input_length:
                results.append(''.join(curr_result))
            else:
                self._find_permutations(counts_map, curr_result,
                                        results, input_length)
            counts_map[char] += 1
            curr_result.pop()


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_permutations.py', "import unittest\n\n\nclass TestPermutations(unittest.TestCase):\n\n    def test_permutations(self):\n        permutations = Permutations()\n        self.assertEqual(permutations.find_permutations(None), None)\n        self.assertEqual(permutations.find_permutations(''), '')\n        string = 'AABC'\n        expected = [\n            'AABC', 'AACB', 'ABAC', 'ABCA',\n            'ACAB', 'ACBA', 'BAAC', 'BACA',\n            'BCAA', 'CAAB', 'CABA', 'CBAA'\n        ]\n        self.assertEqual(permutations.find_permutations(string), expected)\n        print('Success: test_permutations')\n\n\ndef main():\n    test = TestPermutations()\n    test.test_permutations()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_permutations.py')

