#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Determine whether you can win the Nim game given the remaining stones.
# 
# See the [LeetCode](https://leetcode.com/problems/nim-game/) problem page.
# 
# You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
# 
# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
# 
# For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the input an int?
#     * Yes
# * Is the output a boolean?
#     * Yes
# * Can we assume the inputs are valid?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * 1, 2, or 3 -> True
# * 4 -> False
# * 7 -> True
# * 40 -> False

# ## Algorithm
# 
# This is somewhat of a one-trick puzzle, where the only way you can lose if you take the first stone while playing optimally is if the number of remaining stones is divisible by 4.
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


class Solution(object):

    def can_win_nim(self, num_stones_left):
        return num_stones_left % 4 != 0


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_can_win_nim.py', "import unittest\n\n\nclass TestSolution(unittest.TestCase):\n\n    def test_can_win_nim(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.can_win_nim, None)\n        self.assertEqual(solution.can_win_nim(1), True)\n        self.assertEqual(solution.can_win_nim(2), True)\n        self.assertEqual(solution.can_win_nim(3), True)\n        self.assertEqual(solution.can_win_nim(4), False)\n        self.assertEqual(solution.can_win_nim(7), True)\n        self.assertEqual(solution.can_win_nim(40), False)\n        print('Success: test_can_win_nim')\n\n\ndef main():\n    test = TestSolution()\n    test.test_can_win_nim()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_can_win_nim.py')

