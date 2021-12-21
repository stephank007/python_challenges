#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Rishi Rajasekaran](https://github.com/rishihot55). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find all valid combinations of n-pairs of parentheses.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the input an integer representing the number of pairs?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Is the output a list of valid combinations?
#     * Yes
# * Should the output have duplicates?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None -> Exception
# * Negative -> Exception
# * 0 -> []
# * 1 -> ['()']
# * 2 -> ['(())', '()()']
# * 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
# </pre>

# # Algorithm
# 
# Let `l` and `r` denote the number of left and right parentheses remaining at any given point. 
# The algorithm makes use of the following conditions applied recursively:
# * Left braces can be inserted any time, as long as we do not exhaust them i.e. `l > 0`.
# * Right braces can be inserted, as long as the number of right braces remaining is greater than the left braces remaining i.e. `r > l`. Violation of the aforementioned condition produces an unbalanced string of parentheses.
# * If both left and right braces have been exhausted i.e. `l = 0 and r = 0`, then the resultant string produced is balanced.
# 
# The algorithm can be rephrased as:
# * Base case: `l = 0 and r = 0`
#     - Add the string generated to the result set
# * Case 1: `l > 0`
#     - Add a left parenthesis to the parentheses string.
#     - Recurse (l - 1, r, new_string, result_set)
# * Case 2: `r > l`
#     - Add a right parenthesis to the parentheses string.
#     - Recurse (l, r - 1, new_string, result_set)
# 
# Complexity:
# * Time: `O(4^n/n^(3/2))`, see [Catalan numbers](https://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics) - 1, 1, 2, 5, 14, 42, 132...
# * Space complexity: `O(n)`, due to the implicit call stack storing a maximum of 2n function calls)

# ## Code

# In[1]:


class Parentheses(object):

    def find_pair(self, num_pairs):
        if num_pairs is None:
            raise TypeError('num_pairs cannot be None')
        if num_pairs < 0:
            raise ValueError('num_pairs cannot be < 0')
        if not num_pairs:
            return []
        results = []
        curr_results = []
        self._find_pair(num_pairs, num_pairs, curr_results, results)
        return results

    def _find_pair(self, nleft, nright, curr_results, results):
        if nleft == 0 and nright == 0:
            results.append(''.join(curr_results))
        else:
            if nleft >= 0:
                self._find_pair(nleft-1, nright, curr_results+['('], results)
            if nright > nleft:
                self._find_pair(nleft, nright-1, curr_results+[')'], results)


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_n_pairs_parentheses.py', "import unittest\n\n\nclass TestPairParentheses(unittest.TestCase):\n\n    def test_pair_parentheses(self):\n        parentheses = Parentheses()\n        self.assertRaises(TypeError, parentheses.find_pair, None)\n        self.assertRaises(ValueError, parentheses.find_pair, -1)\n        self.assertEqual(parentheses.find_pair(0), [])\n        self.assertEqual(parentheses.find_pair(1), ['()'])\n        self.assertEqual(parentheses.find_pair(2), ['(())',\n                                                '()()'])\n        self.assertEqual(parentheses.find_pair(3), ['((()))',\n                                                '(()())',\n                                                '(())()',\n                                                '()(())',\n                                                '()()()'])\n        print('Success: test_pair_parentheses')\n\n\ndef main():\n    test = TestPairParentheses()\n    test.test_pair_parentheses()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_n_pairs_parentheses.py')

