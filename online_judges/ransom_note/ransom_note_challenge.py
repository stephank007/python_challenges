#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a magazine, see if a ransom note could have been written using the letters in the magazine.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is this case sensitive?
#     * Yes
# * Can we assume we're working with ASCII characters?
#     * Yes
# * Can we scan the entire magazine, or should we scan only when necessary?
#     * You can scan the entire magazine
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * '', '' -> Exception
# * 'a', 'b' -> False
# * 'aa', 'ab' -> False
# * 'aa', 'aab' -> True

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def match_note_to_magazine(self, ransom_note, magazine):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_ransom_note.py
import unittest


class TestRansomNote(unittest.TestCase):

    def test_ransom_note(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.match_note_to_magazine, None, None)
        self.assertEqual(solution.match_note_to_magazine('', ''), True)
        self.assertEqual(solution.match_note_to_magazine('a', 'b'), False)
        self.assertEqual(solution.match_note_to_magazine('aa', 'ab'), False)
        self.assertEqual(solution.match_note_to_magazine('aa', 'aab'), True)
        print('Success: test_ransom_note')


def main():
    test = TestRansomNote()
    test.test_ransom_note()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
