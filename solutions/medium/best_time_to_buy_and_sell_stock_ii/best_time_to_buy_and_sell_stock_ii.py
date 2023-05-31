import unittest

def maxProfit(prices: list) -> int:
    profit = 0

    # Start at the second day, because we need to compare
    # to the first days stock price, to make a judgement.

    i = 1
    while i < len(prices):
        if prices[i - 1] < prices[i]:
            profit = profit + prices[i] - prices[i - 1]

        i += 1

    return profit

class MaxProfitTestCase(unittest.TestCase):
    def test_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        result = maxProfit(prices)
        self.assertEqual(result, expected)

    def test_2(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        result = maxProfit(prices)
        self.assertEqual(result, expected)

    def test_3(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        result = maxProfit(prices)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
