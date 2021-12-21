#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [mrb00l34n](http://github.com/mrb00l34n). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Counting Ways of Making Change.
# 
# * [Hints](#Hints)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Hints
# 
# * Can you think of a way to build up to a solution?
# * If there are 2 ways of making 3, and you are now given a coin of value v, how many ways can you make 3 + v?
# * Can you think of a way to divide the problem into smaller subproblems?

# ## Algorithm
# 
# One possible solution using dynamic programming:
# * Create an array, s.t arr[i] = # of ways to make change for i
# * Initialize arr[0] = 1, arr[i>0] = 0
# * For each coin, and for each index from coin to n, increment arr[i] by arr[i - coin]
# 
# How does this work?
# * As we iterate through each coin, we are adding the ways of making arr[i - coin] to arr[i]
# * If we have 2 ways of making 4, and are now iterating on a coin of value 3, there should be 2 ways of making 7.
# * We are essentially adding the coin we are iterating on to the # of ways of making arr[i].
# 
# Complexity:
# * Time: O(mn); let the number of coins be m. We iterate from arr[coin] -> arr[n], or ~ n operations on each coin, hence n*m. 
# * Space: O(n)

# ## Code

# In[1]:


def change_ways(n, coins):
    arr = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
    return 0 if n == 0 else arr[n]


# ## Unit Test
# 
# 

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_coin_change_ways.py', "import unittest\n\n\nclass Challenge(unittest.TestCase):\n\n    def test_coin_change_ways(self,solution):\n        self.assertEqual(solution(0, [1, 2]), 0)\n        self.assertEqual(solution(100, [1, 2, 3]), 884)\n        self.assertEqual(solution(1000, range(1, 101)), \n                     15658181104580771094597751280645)\n        print('Success: test_coin_change_ways')\n\n\ndef main():\n    test = Challenge()\n    test.test_coin_change_ways(change_ways)\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_coin_change_ways.py')

