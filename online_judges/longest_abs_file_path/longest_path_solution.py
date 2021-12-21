#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Find the longest absolute file path.
# 
# See the [LeetCode](https://leetcode.com/problems/longest-absolute-file-path/) problem page.
# 
# <pre>
# Suppose we abstract our file system by a string in the following manner:
# 
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# 
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
# 
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# 
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# 
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# 
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
# 
# Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.
# 
# Note:
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..
# Time complexity required: O(n) where n is the size of the input string.
# 
# Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
# </pre>
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Is the input a string?
#     * Yes
# * Can we assume the input is valid?
#     * No
# * Will there always be a file in the input?
#     * Yes
# * Is the output an int?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> TypeError
# * '' -> 0
# * 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext' -> 32

# ## Algorithm
# 
# We'll use a dictionary `path_len` to keep track of the current character length (values) at each depth (keys).  Depth 0 will have a length of 0.
# 
# Initialize `max_len` to 0.
# 
# Split the input based on the newline character.  Iterate on each resulting line:
# 
# * Extract the `name` by excluding the tab characters
# * Calculate the depth length by taking into account the tab characters
# * If we are dealing with a file path (there is a '.' in `name`)
#     * Calculate `path_len[depth] + len(name)` and update `max_len` if needed
# * Else, update `path_len[depth + 1] = path_len[depth] + len(name) + 1`
#     * We add `+ 1` because each depth is separated by the '/' character
# * Return `max_len`
# 
# Complexity:
# * Time: O(n)
# * Space: O(n)

# ## Code

# In[1]:


class Solution(object):

    def length_longest_path(self, file_system):
        if file_system is None:
            raise TypeError('file_system cannot be None')
        max_len = 0
        path_len = {0: 0}
        for line in file_system.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_length_longest_path.py', "import unittest\n\n\nclass TestSolution(unittest.TestCase):\n\n    def test_length_longest_path(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.length_longest_path, None)\n        self.assertEqual(solution.length_longest_path(''), 0)\n        file_system = 'dir\\n\\tsubdir1\\n\\t\\tfile1.ext\\n\\t\\tsubsubdir1\\n\\tsubdir2\\n\\t\\tsubsubdir2\\n\\t\\t\\tfile2.ext'\n        expected = 32\n        self.assertEqual(solution.length_longest_path(file_system), expected)\n        print('Success: test_length_longest_path')\n\n\ndef main():\n    test = TestSolution()\n    test.test_length_longest_path()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_length_longest_path.py')

