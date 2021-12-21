#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

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
# It can be relatively straightforward to come up with the brute force solution, check out the method `count_sentence_fit_brute_force` below.  
# 
# The optimized solutions is discussed in more depth [here](https://discuss.leetcode.com/topic/62455/21ms-18-lines-java-solution/25).
# 
# <pre>
# rows = 4
# cols = 6
# sentence = ['abc', 'de', 'f']
# 
# "abc de f abc de f abc de f ..." // start=0
#  012345                          // start=start+cols+adjustment=0+6+1=7 (1 space removed in screen string)
#         012345                   // start=7+6+0=13
#               012345             // start=13+6-1=18 (1 space added)
#                    012345        // start=18+6+1=25 (1 space added)
#                           012345
# </pre>
# 
# Complexity:
# * Time: O(1)
# * Space: O(1)

# ## Code

# In[1]:


class Solution(object):

    def count_sentence_fit_brute_force(self, sentence, rows, cols):
        if sentence is None:
            raise TypeError('sentence cannot be None')
        if rows is None or cols is None:
            raise TypeError('rows and cols cannot be None')
        if rows < 0 or cols < 0:
            raise ValueError('rows and cols cannot be negative')
        if cols == 0 or not sentence:
            return 0
        curr_row = 0
        curr_col = 0
        count = 0
        while curr_row < cols:
            for word in sentence:
                # If the current word doesn't fit on the current line,
                # move to the next line
                if len(word) > cols - curr_col:
                    curr_col = 0
                    curr_row += 1
                # If we are beyond the number of rows, return
                if curr_row >= rows:
                    return count
                # If the current word fits on the current line,
                # 'insert' it here
                if len(word) <= cols - curr_col:
                    curr_col += len(word) + 1
                # If it still doesn't fit, then the word is too long
                # and we should just return the current count
                else:
                    return count
            count += 1
        return count

    def count_sentence_fit(self, sentence, rows, cols):
        if sentence is None:
            raise TypeError('sentence cannot be None')
        if rows is None or cols is None:
            raise TypeError('rows and cols cannot be None')
        if rows < 0 or cols < 0:
            raise ValueError('rows and cols cannot be negative')
        if cols == 0 or not sentence:
            return 0
        string = ' '.join(sentence) + ' '
        start = 0
        str_len = len(string)
        for row in range(rows):
            start += cols
            # We don't need extra space for the current row
            if string[start % str_len] == ' ':
                start += 1
            # The current row can't fit, so we'll need to 
            # remove characters from the next word
            else:
                while (start > 0 and string[(start - 1) % str_len] != ' '):
                    start -= 1
        return start // str_len


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_count_sentence_fit.py', 'import unittest\n\n\nclass TestSolution(unittest.TestCase):\n\n    def test_count_sentence_fit(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.count_sentence_fit, \n                      None, None, None)\n        self.assertRaises(ValueError, solution.count_sentence_fit, \n                      \'abc\', rows=-1, cols=-1)\n        sentence = ["hello", "world"]\n        expected = 1\n        self.assertEqual(solution.count_sentence_fit(sentence, rows=2, cols=8),\n                     expected)\n        sentence = ["a", "bcd", "e"]\n        expected = 2\n        self.assertEqual(solution.count_sentence_fit(sentence, rows=3, cols=6),\n                     expected)\n        sentence = ["I", "had", "apple", "pie"]\n        expected = 1\n        self.assertEqual(solution.count_sentence_fit(sentence, rows=4, cols=5),\n                     expected)\n        print(\'Success: test_count_sentence_fit\')\n\n\ndef main():\n    test = TestSolution()\n    test.test_count_sentence_fit()\n\n\nif __name__ == \'__main__\':\n    main()')


# In[3]:


get_ipython().run_line_magic('run', '-i test_count_sentence_fit.py')

