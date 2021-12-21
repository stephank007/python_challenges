#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement the method draw_line(screen, width, x1, x2) where screen is a list of bytes, width is divisible by 8, and x1, x2 are absolute pixel positions.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Can we assume the inputs are valid?
#     * No
# * For the output, do we set corresponding bits in screen?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * Invalid inputs -> Exception
#     * screen is empty
#     * width = 0
#     * any input param is None
#     * x1 or x2 is out of bounds
# * General case for len(screen) = 20, width = 32:
#     * x1 = 2, x2 = 6
#         * screen[0] = int('00111110', base=2)
#     * x1 = 68, x2 = 80
#         * screen[8], int('00001111', base=2)
#         * screen[9], int('11111111', base=2)
#         * screen[10], int('10000000', base=2)

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


class BitsScreen(object):

    def draw_line(self, screen, width, x1, x2):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_draw_line.py
import unittest


class TestBitsScreen(unittest.TestCase):

    def test_draw_line(self):
        bits_screen = BitsScreen()
        screen = []
        for _ in range(20):
            screen.append(int('00000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=68, x2=80)
        self.assertEqual(screen[8], int('00001111', base=2))
        self.assertEqual(screen[9], int('11111111', base=2))
        self.assertEqual(screen[10], int('10000000', base=2))
        bits_screen.draw_line(screen, width=32, x1=2, x2=6)
        self.assertEqual(screen[0], int('00111110', base=2))
        bits_screen.draw_line(screen, width=32, x1=10, x2=13)
        self.assertEqual(screen[1], int('00111100', base=2))
        print('Success: test_draw_line')


def main():
    test = TestBitsScreen()
    test.test_draw_line()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
