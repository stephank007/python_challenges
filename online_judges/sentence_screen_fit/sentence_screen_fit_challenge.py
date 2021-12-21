#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find how many times a sentence can fit on a screen.
# 
# See the [LeetCode](https://leetcode.com/problems/sentence-screen-fitting/) problem page.
# 
# <pre>
# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
# 
# Note:
# 
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
# Example 1:
# 
# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]
# 
# Output: 
# 1
# 
# Explanation:
# hello---
# world---
# 
# The character '-' signifies an empty space on the screen.
# Example 2:
# 
# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
# 
# Output: 
# 2
# 
# Explanation:
# a-bcd- 
# e-a---
# bcd-e-
# 
# The character '-' signifies an empty space on the screen.
# Example 3:
# 
# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
# 
# Output: 
# 1
# 
# Explanation:
# I-had
# apple
# pie-I
# had--
# 
# The character '-' signifies an empty space on the screen.
# </pre>
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume sentence is ASCII?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Is the output an integer?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * rows < 0 or cols < 0 -> ValueError
# * cols = 0 -> 0
# * sentence = '' -> 0
# * rows = 2, cols = 8, sentence = ["hello", "world"] -> 1
# * rows = 3, cols = 6, sentence = ["a", "bcd", "e"] -> 2
# * rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"] -> 1

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def count_sentence_fit(self, sentence, rows, cols):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_count_sentence_fit.py
import unittest


class TestSolution(unittest.TestCase):

    def test_count_sentence_fit(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.count_sentence_fit, 
                      None, None, None)
        self.assertRaises(ValueError, solution.count_sentence_fit, 
                      'abc', rows=-1, cols=-1)
        sentence = ["hello", "world"]
        expected = 1
        self.assertEqual(solution.count_sentence_fit(sentence, rows=2, cols=8),
                     expected)
        sentence = ["a", "bcd", "e"]
        expected = 2
        self.assertEqual(solution.count_sentence_fit(sentence, rows=3, cols=6),
                     expected)
        sentence = ["I", "had", "apple", "pie"]
        expected = 1
        self.assertEqual(solution.count_sentence_fit(sentence, rows=4, cols=5),
                     expected)
        print('Success: test_count_sentence_fit')


def main():
    test = TestSolution()
    test.test_count_sentence_fit()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
