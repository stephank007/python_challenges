#!/usr/bin/env python
# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Given a list of stock prices on each consecutive day, determine the max profits with k transactions.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
# 
# * Is k the number of sell transactions?
#     * Yes
# * Can we assume the prices input is an array of ints?
#     * Yes
# * Can we assume the inputs are valid?
#     * No
# * If the prices are all decreasing and there is no opportunity to make a profit, do we just return 0?
#     * Yes
# * Should the output be the max profit and days to buy and sell?
#     * Yes
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
# 
# <pre>
# * Prices: None or k: None -> None
# * Prices: [] or k <= 0 -> []
# * Prices: [0, -1, -2, -3, -4, -5]
#     * (max profit, list of transactions)
#     * (0, [])
# * Prices: [2, 5, 7, 1, 4, 3, 1, 3] k: 3
#     * (max profit, list of transactions)
#     * (10, [Type.SELL day: 7 price: 3, 
#             Type.BUY  day: 6 price: 1, 
#             Type.SELL day: 4 price: 4, 
#             Type.BUY  day: 3 price: 1, 
#             Type.SELL day: 2 price: 7, 
#             Type.BUY  day: 0 price: 2])
# </pre>

# ## Algorithm
# 
# Refer to the [Solution Notebook]().  If you are stuck and need a hint, the solution notebook's algorithm discussion might be a good place to start.

# ## Code

# In[ ]:


from enum import Enum  # Python 2 users: Run pip install enum34


class Type(Enum):
    SELL = 0
    BUY = 1


class Transaction(object):

    def __init__(self, type, day, price):
        self.type = type
        self.day = day
        self.price = price

    def __eq__(self, other):
        return self.type == other.type and             self.day == other.day and             self.price == other.price

    def __repr__(self):
        return str(self.type) + ' day: ' +             str(self.day) + ' price: ' +             str(self.price)


# In[ ]:


class StockTrader(object):

    def find_max_profit(self, prices, k):
        # TODO: Implement me
        pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_max_profit.py
import unittest


class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        stock_trader = StockTrader()
        self.assertRaises(TypeError, stock_trader.find_max_profit, None, None)
        self.assertEqual(stock_trader.find_max_profit(prices=[], k=0), [])
        prices = [5, 4, 3, 2, 1]
        k = 3
        self.assertEqual(stock_trader.find_max_profit(prices, k), (0, []))
        prices = [2, 5, 7, 1, 4, 3, 1, 3]
        profit, transactions = stock_trader.find_max_profit(prices, k)
        self.assertEqual(profit, 10)
        self.assertTrue(Transaction(Type.SELL,
                                day=7,
                                price=3) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=6,
                                price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                day=4,
                                price=4) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=3,
                                price=1) in transactions)
        self.assertTrue(Transaction(Type.SELL,
                                day=2,
                                price=7) in transactions)
        self.assertTrue(Transaction(Type.BUY,
                                day=0,
                                price=2) in transactions)
        print('Success: test_max_profit')


def main():
    test = TestMaxProfit()
    test.test_max_profit()


if __name__ == '__main__':
    main()


# ## Solution Notebook
# 
# Review the [Solution Notebook]() for a discussion on algorithms and code solutions.
