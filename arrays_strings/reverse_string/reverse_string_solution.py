#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Solution Notebook

# ## Problem: Implement a function to reverse a string (a list of characters), in-place.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Pythonic-Code](#Pythonic-Code)
# * [Unit Test](#Unit-Test)
# * [Bonus C Algorithm](#Bonus-C-Algorithm)
# * [Bonus C Code](#Bonus-C-Code)

# ## Constraints
# 
# * Can we assume the string is ASCII?
#     * Yes
#     * Note: Unicode strings could require special handling depending on your language
# * Since we need to do this in-place, it seems we cannot use the slice operator or the reversed function?
#     * Correct
# * Since Python string are immutable, can we use a list of characters instead?
#     * Yes

# ## Test Cases
# 
# * None -> None
# * [''] -> ['']
# * ['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']

# ## Algorithm
# 
# Since Python strings are immutable, we'll use a list of chars instead to exercise in-place string manipulation as you would get with a C string.
# 
# * Iterate len(string)/2 times, starting with i = 0:
#     * Swap char with index (i) and char with index (len(string) - 1 - i)
#     * Increment i
# 
# Complexity:
# * Time: O(n)
# * Space: O(1)
# 
# Note:
# * You could use a byte array instead of a list to do in-place string operations

# ## Code

# In[1]:


from __future__ import division


class ReverseString(object):

    def reverse(self, chars):
        if chars:
            size = len(chars)
            for i in range(size // 2):
                chars[i], chars[size - 1 - i] =                     chars[size - 1 - i], chars[i]
        return chars


# ## Pythonic-Code
# 
# This question has an artificial constraint that prevented the use of the slice operator and the reversed method.  For completeness, the solutions for these are provided below.  Note these solutions are not in-place.

# In[2]:


class ReverseStringAlt(object):

    def reverse_string_alt(string):
        if string:
            return string[::-1]
        return string

    def reverse_string_alt2(string):
        if string:
            return ''.join(reversed(string))
        return string


# ## Unit Test

# In[3]:


get_ipython().run_cell_magic('writefile', 'test_reverse_string.py', "import unittest\n\n\nclass TestReverse(unittest.TestCase):\n\n    def test_reverse(self, func):\n        self.assertEqual(func(None), None)\n        self.assertEqual(func(['']), [''])\n        self.assertEqual(func(\n            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),\n            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])\n        print('Success: test_reverse')\n\n    def test_reverse_inplace(self, func):\n        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']\n        func(target_list)\n        self.assertEqual(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])\n        print('Success: test_reverse_inplace')\n\n\ndef main():\n    test = TestReverse()\n    reverse_string = ReverseString()\n    test.test_reverse(reverse_string.reverse)\n    test.test_reverse_inplace(reverse_string.reverse)\n\n\nif __name__ == '__main__':\n    main()")


# In[4]:


get_ipython().run_line_magic('run', '-i test_reverse_string.py')


# ## C Algorithm
# 
# This is a classic problem in C/C++
# 
# We'll want to keep two pointers:
# * i is a pointer to the first char
# * j is a pointer to the last char
# 
# To get a pointer to the last char, we need to loop through all characters, take note of null terminator.
# 
# * while i < j
#     * swap i and j
# 
# Complexity:
# * Time: O(n)
# * Space: In-place
# 
# Note:
# * Instead of using i, you can use str instead, although this might not be as intuitive.

# ## C Code

# In[ ]:


# %load reverse_string.cpp
#include <stdio.h>

void Reverse(char* str) {
    if (str) {
        char* i = str;	// first letter
        char* j = str;	// last letter
        
        // find the end of the string
        while (*j) {
            j++;
        }
        
        // don't point to the null terminator
        j--;
        
        char tmp;
        
        (/, swap, chars, to, reverse, the, string)
        while (i < j) {
            tmp = *i;
            *i++ = *j;
            *j-- = tmp;
        }
    }
}

int main() {
    char test0[] = "";
    char test1[] = "foo";
    Reverse(NULL);
    Reverse(test0);
    Reverse(test1);
    printf("%s \n", test0);
    printf("%s \n", test1);
    return 0;
}

