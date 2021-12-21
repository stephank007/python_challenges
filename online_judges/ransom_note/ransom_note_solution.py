#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Given a magazine, see if a ransom note could have been written using the letters in the magazine.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

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
# * Build a dictionary of the magazine characters and counts.
# * Loop through each letter in the ransom note and see if there are enough letters in the magazine's dictionary.
# * Note: You could make this more efficient by not scanning the entire magazine all at once, but instead scan just in time as you run out of letters in the dictionary.
# 
# Complexity:
# * Time: O(n+m), where n is the length of the ransom note and m is the length of the magazine
# * Space: O(n+m)

# ## Code

# In[1]:


class Solution(object):

    def match_note_to_magazine(self, ransom_note, magazine):
        if ransom_note is None or magazine is None:
            raise TypeError('ransom_note or magazine cannot be None')
        seen_chars = {}
        for char in magazine:
            if char in seen_chars:
                seen_chars[char] += 1
            else:
                seen_chars[char] = 1
        for char in ransom_note:
            try:
                seen_chars[char] -= 1
            except KeyError:
                return False
            if seen_chars[char] < 0:
                return False
        return True


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_ransom_note.py', "import unittest\n\n\nclass TestRansomNote(unittest.TestCase):\n\n    def test_ransom_note(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.match_note_to_magazine, None, None)\n        self.assertEqual(solution.match_note_to_magazine('', ''), True)\n        self.assertEqual(solution.match_note_to_magazine('a', 'b'), False)\n        self.assertEqual(solution.match_note_to_magazine('aa', 'ab'), False)\n        self.assertEqual(solution.match_note_to_magazine('aa', 'aab'), True)\n        print('Success: test_ransom_note')\n\n\ndef main():\n    test = TestRansomNote()\n    test.test_ransom_note()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_ransom_note.py')

