#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Assign Cookies.
# 
# See the [LeetCode](https://leetcode.com/problems/assign-cookies/) problem page.
# 
# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
# 
# Note:
# You may assume the greed factor is always positive. 
# You cannot assign more than one cookie to one child.
# 
# Example 1:
# Input: [1,2,3], [1,1]
# 
# Output: 1
# 
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.
# Example 2:
# Input: [1,2], [1,2,3]
# 
# Output: 2
# 
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
# You have 3 cookies and their sizes are big enough to gratify all of the children, 
# You need to output 2.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)

# ## Constraints
# 
# * Are the inputs two list(int), one for greed factor and the other for cookie size?
#     * Yes
# * Are the inputs are sorted increasing order?
#     * No
# * Can we change inputs themselves, or do we need to make a copy?
#     * You can change them
# * Is the output an int?
#     * Yes
# * Is the greed factor always >= 1?
#     * Yes
# * Can we assume the inputs are valid?
#     * No, check for None
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * None input -> TypeError
# [1, 2, 3], [1, 1] -> 1
# [1, 2], [1, 2, 3] -> 2
# [7, 8, 9, 10], [5, 6, 7, 8] -> 2
# </pre>

# ## Algorithm
# 
# * Sort the inputs
# * We'll keep an index to the current greed factor
# * For each cookie
#     * Assign it to a child if its size >= the child's greed factor
#         * Increment result counter
#         * Increment the index to the greed factor
#             * Careful of this index going out of bounds
# * Return the result counter
# 
# Complexity:
# * Time: O(n log n) for the sort
# * Space: O(1), assuming the sort is in-place

# ## Code

# In[1]:


class Solution(object):

    def find_content_children(self, greed_indices, cookie_sizes):
        if greed_indices is None or cookie_sizes is None:
            raise TypeError('greed_indices or cookie_sizes cannot be None')
        if not greed_indices or not cookie_sizes:
            return 0
        greed_indices.sort()
        cookie_sizes.sort()
        greed_index = 0
        num_children = 0
        for size in cookie_sizes:
            if greed_index >= len(greed_indices):
                break
            if size >= greed_indices[greed_index]:
                num_children += 1
                greed_index += 1
        return num_children


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_assign_cookie.py', "import unittest\n\n\nclass TestAssignCookie(unittest.TestCase):\n\n    def test_assign_cookie(self):\n        solution = Solution()\n        self.assertRaises(TypeError, solution.find_content_children, None, None)\n        self.assertEqual(solution.find_content_children([1, 2, 3], \n                                                    [1, 1]), 1)\n        self.assertEqual(solution.find_content_children([1, 2], \n                                                    [1, 2, 3]), 2)\n        self.assertEqual(solution.find_content_children([7, 8, 9, 10], \n                                                    [5, 6, 7, 8]), 2)\n        print('Success: test_find_content_children')\n\n\ndef main():\n    test = TestAssignCookie()\n    test.test_assign_cookie()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_assign_cookie.py')

