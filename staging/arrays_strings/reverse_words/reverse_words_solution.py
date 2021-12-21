#!/usr/bin/env python
# coding: utf-8

# <small> <i> This notebook was prepared by Marco Guajardo. For license visit [github](https://github.com/donnemartin/interactive-coding-challenges) </i> </small>

# # Solution notebook
# ## Problem: Given a string of words, return a string with the words in reverse

# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# * Can we assume the string is ASCII?
#   * Yes
# * Is whitespace important?
#   * no the whitespace does not change
# * Is this case sensitive?
#   * yes
# * What if the string is empty?
#   * return None
# * Is the order of words important?
#   * yes
# 
# 

# ## Algorithm: Split words into a list and reverse each word individually
# Steps:
# 
# * Check if string is empty
# * If not empty, split the string into a list of words 
# * For each word on the list
#   * reverse the word
# * Return the string representation of the list
# 
# Complexity:
# 
# * Time complexity is O(n) where n is the number of chars.
# * Space complexity is O(n) where n is the number of chars. 

# In[1]:


def reverse_words(S):
    if len(S) is 0:
        return None

    words = S.split()
    for i in range (len(words)):
        words[i] = words[i][::-1]

    return " ".join(words)


# In[2]:


get_ipython().run_cell_magic('writefile', 'reverse_words_solution.py', 'import unittest\n\n\nclass TestReverseWords(unittest.TestCase):\n\n    def testReverseWords(self, func):\n            self.assertEqual(func(\'the sun is hot\'), \'eht nus si toh\')\n            self.assertEqual(func(\'\'), None)\n            self.assertEqual(func(\'123 456 789\'), \'321 654 987\')\n            self.assertEqual(func(\'magic\'), \'cigam\')\n            print(\'Success: reverse_words\')\n\n\ndef main():\n    test = TestReverseWords()\n    test.testReverseWords(reverse_words)\n\n\nif __name__=="__main__":\n  main()')


# In[3]:


run -i reverse_words_solution.py

