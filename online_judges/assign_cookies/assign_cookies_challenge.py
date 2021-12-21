#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

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
# * [Solution Notebook](#Solution-Notebook)

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
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class Solution(object):

    def find_content_children(self, g, s):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_assign_cookie.py
import unittest


class TestAssignCookie(unittest.TestCase):

    def test_assign_cookie(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.find_content_children, None, None)
        self.assertEqual(solution.find_content_children([1, 2, 3], 
                                                    [1, 1]), 1)
        self.assertEqual(solution.find_content_children([1, 2], 
                                                    [1, 2, 3]), 2)
        self.assertEqual(solution.find_content_children([7, 8, 9, 10], 
                                                    [5, 6, 7, 8]), 2)
        print('Success: test_find_content_children')


def main():
    test = TestAssignCookie()
    test.test_assign_cookie()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
