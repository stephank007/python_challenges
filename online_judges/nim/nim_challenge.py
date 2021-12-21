#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

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
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is the input an int?
#     * Yes
# * Is the output a boolean?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
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
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def can_win_nim(self, num_stones_left):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_can_win_nim.py
import unittest


class TestSolution(unittest.TestCase):

    def test_can_win_nim(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.can_win_nim, None)
        self.assertEqual(solution.can_win_nim(1), True)
        self.assertEqual(solution.can_win_nim(2), True)
        self.assertEqual(solution.can_win_nim(3), True)
        self.assertEqual(solution.can_win_nim(4), False)
        self.assertEqual(solution.can_win_nim(7), True)
        self.assertEqual(solution.can_win_nim(40), False)
        print('Success: test_can_win_nim')


def main():
    test = TestSolution()
    test.test_can_win_nim()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
