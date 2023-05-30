import unittest

def maxProfit(prices: list) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """

    #Input: prices = [7, 1, 5, 3, 6, 4]
    #Output: 7

    # read a price
    #
    # if that price is smaller than yesterday == hold
    # if that price is

    priority = []

    profit = 0
    owned = False

    i = 0
    while i < len(prices):
        if i - 1
        print(prices[i])
        i += 1

    return 0

class MaxProfitTestCase(unittest.TestCase):
    def test_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        result = maxProfit(prices)
        #self.assertEqual(result, expected)

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
