#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Generate a list of primes.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is it correct that 1 is not considered a prime number?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# * None -> Exception
# * Not an int -> Exception
# * 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[3]:


class PrimeGenerator(object):

    def generate_primes(self, max_num):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_generate_primes.py
import unittest


class TestMath(unittest.TestCase):

    def test_generate_primes(self):
        prime_generator = PrimeGenerator()
        self.assertRaises(TypeError, prime_generator.generate_primes, None)
        self.assertRaises(TypeError, prime_generator.generate_primes, 98.6)
        self.assertEqual(prime_generator.generate_primes(20), [False, False, True, 
                                                           True, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True])
        print('Success: generate_primes')


def main():
    test = TestMath()
    test.test_generate_primes()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
