#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a trie with find, insert, remove, and list_words methods.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume we are working with strings?
#     * Yes
# * Are the strings in ASCII?
#     * Yes
# * Should `find` only match exact words with a terminating character?
#     * Yes
# * Should `list_words` only return words with a terminating character?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# 
#          root
#        /  |  \
#       h   a*  m
#      / \   \   \
#     a   e*  t*  e*
#    / \         / \
#   s*  t*      n*  t*
#              /
#             s*
# 
# find
# 
# * Find on an empty trie
# * Find non-matching
# * Find matching
# 
# insert
# 
# * Insert on empty trie
# * Insert to make a leaf terminator char
# * Insert to extend an existing terminator char
# 
# remove
# 
# * Remove me
# * Remove mens
# * Remove a
# * Remove has
# 
# list_words
# 
# * List empty
# * List general case
# </pre>
# 
# 

# ## Algorithm
# 
# Refer to the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/trie/trie_solution.ipynb).  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


from collections import OrderedDict


class Node(object):

    def __init__(self, data, parent=None, terminates=False):
        # TODO: Implement me
        pass


class Trie(object):

    def __init__(self):
        # TODO: Implement me
        pass

    def find(self, word):
        # TODO: Implement me
        pass

    def insert(self, word):
        # TODO: Implement me
        pass

    def remove(self, word):
        # TODO: Implement me
        pass

    def list_words(self):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_trie.py
import unittest


class TestTrie(unittest.TestCase):       

    def test_trie(self):
        trie = Trie()

        print('Test: Insert')
        words = ['a', 'at', 'has', 'hat', 'he',
                 'me', 'men', 'mens', 'met']
        for word in words:
            trie.insert(word)
        for word in trie.list_words():
            self.assertTrue(trie.find(word) is not None)
            
        print('Test: Remove me')
        trie.remove('me')
        words_removed = ['me']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'mens', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove mens')
        trie.remove('mens')
        words_removed = ['me', 'mens']
        words = ['a', 'at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove a')
        trie.remove('a')
        words_removed = ['a', 'me', 'mens']
        words = ['at', 'has', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Test: Remove has')
        trie.remove('has')
        words_removed = ['a', 'has', 'me', 'mens']
        words = ['at', 'hat', 'he',
                 'men', 'met']
        for word in words:
            self.assertTrue(trie.find(word) is not None)
        for word in words_removed:
            self.assertTrue(trie.find(word) is None)

        print('Success: test_trie')

    def test_trie_remove_invalid(self):
        print('Test: Remove from empty trie')
        trie = Trie()
        self.assertTrue(trie.remove('foo') is None) 


def main():
    test = TestTrie()
    test.test_trie()
    test.assertRaises(KeyError, test.test_trie_remove_invalid)


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/trie/trie_solution.ipynb) for a discussion on algorithms and code solutions.
