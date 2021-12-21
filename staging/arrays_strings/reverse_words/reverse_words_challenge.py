#!/usr/bin/env python
# coding: utf-8

# <small> <i> This notebook was prepared by Marco Guajardo. For license visit [github](https://github.com/donnemartin/interactive-coding-challenges) </i> </small>
# .

# # Challenge Notebook
# 

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

# ## Test Cases
# * Empty string -> None
# * "the sun is very hot" -> "eht nus si yrev toh"
# 

# ## Algorithm
# * Refer to the [Solution](https://github.com/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/reverse_words/reverse_words_solution.ipynb) if you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code 

# In[21]:


def reverse_words (S):
    #TODO: implement me
    pass


# ## Unit Test
# <b> The following unit test is expected to fail until you solve challenge </b>

# In[1]:


import unittest


class UnitTest(unittest.TestCase):

    def testReverseWords(self, func):
            self.assertEqual(func('the sun is hot'), 'eht nus si toh')
            self.assertEqual(func(''), None)
            self.assertEqual(func('123 456 789'), '321 654 987')
            self.assertEqual(func('magic'), 'cigam')
            print('Success: reverse_words')


def main():
    test = UnitTest()
    test.testReverseWords(reverse_words)


if __name__=="__main__":
  main()


# ## Solution Notebook
# * Review the [Solution Notebook](https://github.com/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/reverse_words/reverse_words_solution.ipynb) for discussion on algorithms and code solutions.
