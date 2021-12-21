#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Maximizing XOR
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/maximizing-xor).
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/maximizing-xor).

# ## Test Cases
# 
# See the [HackerRank problem page](https://www.hackerrank.com/challenges/maximizing-xor).

# ## Algorithm
# 
# * Set max to 0
# * For i in the range (lower, upper) inclusive
#     * For j in the range (lower, upper) inclusive
#         * Compare i ^ j with max, update max if needed
# * return max
# 
# Complexity:
# * Time: O(n^2) - See note below
# * Space: O(1)
# 
# Note:
# * TODO: Add more optimal solutions such as those discussed [here](https://www.hackerrank.com/challenges/maximizing-xor/editorial).

# ## Code

# In[1]:


class Solution(object):

    def max_xor(self, lower, upper):
        result = 0
        for l in range(lower, upper + 1):
            for u in range(lower, upper + 1):
                curr = l ^ u
                if result < curr:
                    result = curr
        return result


# ## Unit Test
# 
# 

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_maximizing_xor.py', "import unittest\n\n\nclass TestMaximizingXor(unittest.TestCase):\n\n    def test_maximizing_xor(self):\n        solution = Solution()\n        self.assertEqual(solution.max_xor(10, 15), 7)\n        print('Success: test_maximizing_xor')\n\n\ndef main():\n    test = TestMaximizingXor()\n    test.test_maximizing_xor()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_maximizing_xor.py')

