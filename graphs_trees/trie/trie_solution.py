#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a trie with find, insert, remove, and list_words methods.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# root node is denoted by ''
# 
#          ''
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
# 

# ## Algorithm
# 
# ### find
# 
# * Set node to the root
# * For each char in the input word
#     * Check the current node's children to see if it contains the char
#         * If a child has the char, set node to the child
#         * Else, return None
# * Return the last child node if it has a terminator, else None
# 
# Complexity:
# * Time: O(m), where m is the length of the word
# * Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach
# 
# ### insert
# 
# * set node to the root
# * For each char in the input word
#     * Check the current node's children to see if it contains the char
#         * If a child has the char, set node to the child
#         * Else, insert a new node with the char
#             * Update children and parents
# * Set the last node as a terminating node
# 
# Complexity:
# * Time: O(m), where m is the length of the word
# * Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach
# 
# ### remove
# 
# * Determine the matching terminating node by calling the find method
# * If the matching node has children, remove the terminator to prevent orphaning its children
# * Set the parent node to the matching node's parent
# * We'll be looping up the parent chain to propagate the delete
# * While the parent is valid
#     * If the node has children
#         * Return to prevent orphaning its remaining children
#     * If the node is a terminating node and it isn't the original matching node from the find call
#         * Return to prevent deleting this additional valid word
#     * Remove the parent node's child entry matching the node
#     * Set the node to the parent
#     * Set the parent to the parent's parent
# 
# Complexity:
# * Time: O(m+h), where where m is the length of the word and h is the tree height
# * Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach
# 
# ### list_words
# 
# * Do a pre-order traversal, passing down the current word
#     * When you reach a terminating node, add it to the list of results
# 
# Complexity:
# * Time: O(n)
# * Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach

# ## Code

# In[1]:


get_ipython().run_cell_magic('writefile', 'trie.py', "from collections import OrderedDict\n\n\nclass Node(object):\n\n    def __init__(self, key, parent=None, terminates=False):\n        self.key = key\n        self.terminates = False\n        self.parent = parent\n        self.children = {}\n\n\nclass Trie(object):\n\n    def __init__(self):\n        self.root = Node('')\n\n    def find(self, word):\n        if word is None:\n            raise TypeError('word cannot be None')\n        node = self.root\n        for char in word:\n            if char in node.children:\n                node = node.children[char]\n            else:\n                return None\n        return node if node.terminates else None\n\n    def insert(self, word):\n        if word is None:\n            raise TypeError('word cannot be None')\n        node = self.root\n        parent = None\n        for char in word:\n            if char in node.children:\n                node = node.children[char]\n            else:\n                node.children[char] = Node(char, parent=node)\n                node = node.children[char]\n        node.terminates = True\n\n    def remove(self, word):\n        if word is None:\n            raise TypeError('word cannot be None')\n        node = self.find(word)\n        if node is None:\n            raise KeyError('word does not exist')\n        node.terminates = False\n        parent = node.parent\n        while parent is not None:\n            # As we are propagating the delete up the \n            # parents, if this node has children, stop\n            # here to prevent orphaning its children.\n            # Or\n            # if this node is a terminating node that is\n            # not the terminating node of the input word, \n            # stop to prevent removing the associated word.\n            if node.children or node.terminates:\n                return\n            del parent.children[node.key]\n            node = parent\n            parent = parent.parent\n\n    def list_words(self):\n        result = []\n        curr_word = ''\n        self._list_words(self.root, curr_word, result)\n        return result\n\n    def _list_words(self, node, curr_word, result):\n        if node is None:\n            return\n        for key, child in node.children.items():\n            if child.terminates:\n                result.append(curr_word + key)\n            self._list_words(child, curr_word + key, result)")


# In[2]:


get_ipython().run_line_magic('run', 'trie.py')


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_trie.py', "import unittest\n\n\nclass TestTrie(unittest.TestCase):       \n\n    def test_trie(self):\n        trie = Trie()\n\n        print('Test: Insert')\n        words = ['a', 'at', 'has', 'hat', 'he',\n                 'me', 'men', 'mens', 'met']\n        for word in words:\n            trie.insert(word)\n        for word in trie.list_words():\n            self.assertTrue(trie.find(word) is not None)\n            \n        print('Test: Remove me')\n        trie.remove('me')\n        words_removed = ['me']\n        words = ['a', 'at', 'has', 'hat', 'he',\n                 'men', 'mens', 'met']\n        for word in words:\n            self.assertTrue(trie.find(word) is not None)\n        for word in words_removed:\n            self.assertTrue(trie.find(word) is None)\n\n        print('Test: Remove mens')\n        trie.remove('mens')\n        words_removed = ['me', 'mens']\n        words = ['a', 'at', 'has', 'hat', 'he',\n                 'men', 'met']\n        for word in words:\n            self.assertTrue(trie.find(word) is not None)\n        for word in words_removed:\n            self.assertTrue(trie.find(word) is None)\n\n        print('Test: Remove a')\n        trie.remove('a')\n        words_removed = ['a', 'me', 'mens']\n        words = ['at', 'has', 'hat', 'he',\n                 'men', 'met']\n        for word in words:\n            self.assertTrue(trie.find(word) is not None)\n        for word in words_removed:\n            self.assertTrue(trie.find(word) is None)\n\n        print('Test: Remove has')\n        trie.remove('has')\n        words_removed = ['a', 'has', 'me', 'mens']\n        words = ['at', 'hat', 'he',\n                 'men', 'met']\n        for word in words:\n            self.assertTrue(trie.find(word) is not None)\n        for word in words_removed:\n            self.assertTrue(trie.find(word) is None)\n\n        print('Success: test_trie')\n\n    def test_trie_remove_invalid(self):\n        print('Test: Remove from empty trie')\n        trie = Trie()\n        self.assertTrue(trie.remove('foo') is None) \n\n\ndef main():\n    test = TestTrie()\n    test.test_trie()\n    test.assertRaises(KeyError, test.test_trie_remove_invalid)\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_trie.py')

