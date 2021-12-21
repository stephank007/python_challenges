#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Return all subsets of a set.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Should the resulting subsets be unique?
#     * Yes, treat 'ab' and 'bc' as the same
# * Is the empty set included as a subset?
#     * Yes
# * Are the inputs unique?
#     * No
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> None
# * '' -> ['']
# * 'a' -> ['a', '']
# * 'ab' -> ['a', 'ab', 'b', '']
# * 'abc' -> ['a', 'ab', 'abc', 'ac',
#             'b', 'bc', 'c', '']
# * 'aabc' -> ['a', 'aa', 'aab', 'aabc', 
#              'aac', 'ab', 'abc', 'ac', 
#              'b', 'bc', 'c', '']
# </pre>

# ## Algorithm
# 
# * Build a dictionary of {chars: counts} where counts is the number of times each char is found in the input
# * Loop through each item in the dictionary
#     * Keep track of the current index (first item will have current index 0)
#     * If the char's count is 0, continue
#     * Decrement the current char's count in the dictionary
#     * Add the current char to the current results
#     * Add the current result to the results
#     * Recurse, passing in the current index as the new starting point index
#         * When we recurse, we'll check if current index < starting point index, and if so, continue
#         * This avoids duplicate results such as 'ab' and 'bc'
#     * Backtrack by:
#         * Removing the just added current char from the current results
#         * Incrementing the current char's count in the dictionary
# 
# Complexity:
# * Time: O(2^n)
# * Space: O(2^n) if we are saving each result, or O(n) if we are just printing each result
# 
# We are doubling the number of operations every time we add an element to the results: O(2^n).
# 
# Note, you could also use the following method to solve this problem:
# 
# <pre>
# number binary  subset
# 0      000      {}
# 1      001      {c}
# 2      010      {b}
# 3      011      {b,c}
# 4      100      {a}
# 5      101      {a,c}
# 6      110      {a,b}
# 7      111      {a,b,c}
# </pre>

# ## Code

# In[1]:


from collections import OrderedDict


class Combinatoric(object):

    def _build_counts_map(self, string):
        counts_map = OrderedDict()
        for char in string:
            if char in counts_map:
                counts_map[char] += 1
            else:
                counts_map[char] = 1
        return counts_map

    def find_power_set(self, string):
        if string is None:
            return string
        if string == '':
            return ['']
        counts_map = self._build_counts_map(string)
        curr_results = []
        results = []
        self._find_power_set(counts_map, curr_results,
                             results, index=0)
        results.append('')
        return results

    def _find_power_set(self, counts_map, curr_result,
                        results, index):
        for curr_index, char in enumerate(counts_map):
            if curr_index < index or counts_map[char] == 0:
                continue
            curr_result.append(char)
            counts_map[char] -= 1
            results.append(''.join(curr_result))
            self._find_power_set(counts_map, curr_result,
                                 results, curr_index)
            counts_map[char] += 1
            curr_result.pop()


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_power_set.py', "import unittest\n\n\nclass TestPowerSet(unittest.TestCase):\n\n    def test_power_set(self):\n        input_set = ''\n        expected = ['']\n        self.run_test(input_set, expected)\n        input_set = 'a'\n        expected = ['a', '']\n        self.run_test(input_set, expected)\n        input_set = 'ab'\n        expected = ['a', 'ab', 'b', '']\n        self.run_test(input_set, expected)\n        input_set = 'abc'\n        expected = ['a', 'ab', 'abc', 'ac',\n                    'b', 'bc', 'c', '']\n        self.run_test(input_set, expected)\n        input_set = 'aabc'\n        expected = ['a', 'aa', 'aab', 'aabc', \n                    'aac', 'ab', 'abc', 'ac', \n                    'b', 'bc', 'c', '']\n        self.run_test(input_set, expected)\n        print('Success: test_power_set')\n\n    def run_test(self, input_set, expected):\n        combinatoric = Combinatoric()\n        result = combinatoric.find_power_set(input_set)\n        self.assertEqual(result, expected)\n\n\ndef main():\n    test = TestPowerSet()\n    test.test_power_set()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_power_set.py')

