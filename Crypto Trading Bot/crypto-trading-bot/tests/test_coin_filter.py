import unittest
from src.coin_filter import filter_coins

class TestCoinFilter(unittest.TestCase):

    def setUp(self):
        self.test_coins = [
            {'name': 'CoinA', 'liquidity': 10000, 'market_cap': 500000, 'age': 1},
            {'name': 'CoinB', 'liquidity': 5000, 'market_cap': 300000, 'age': 2},
            {'name': 'CoinC', 'liquidity': 15000, 'market_cap': 800000, 'age': 0.5},
            {'name': 'CoinD', 'liquidity': 2000, 'market_cap': 100000, 'age': 3},
        ]

    def test_filter_coins_by_liquidity(self):
        filtered_coins = filter_coins(self.test_coins, liquidity_threshold=8000)
        self.assertEqual(len(filtered_coins), 3)
        self.assertIn({'name': 'CoinA', 'liquidity': 10000, 'market_cap': 500000, 'age': 1}, filtered_coins)
        self.assertIn({'name': 'CoinC', 'liquidity': 15000, 'market_cap': 800000, 'age': 0.5}, filtered_coins)

    def test_filter_coins_by_market_cap(self):
        filtered_coins = filter_coins(self.test_coins, market_cap_min=400000)
        self.assertEqual(len(filtered_coins), 2)
        self.assertIn({'name': 'CoinA', 'liquidity': 10000, 'market_cap': 500000, 'age': 1}, filtered_coins)
        self.assertIn({'name': 'CoinC', 'liquidity': 15000, 'market_cap': 800000, 'age': 0.5}, filtered_coins)

    def test_filter_coins_by_age(self):
        filtered_coins = filter_coins(self.test_coins, max_age=2)
        self.assertEqual(len(filtered_coins), 3)
        self.assertIn({'name': 'CoinA', 'liquidity': 10000, 'market_cap': 500000, 'age': 1}, filtered_coins)
        self.assertIn({'name': 'CoinB', 'liquidity': 5000, 'market_cap': 300000, 'age': 2}, filtered_coins)
        self.assertIn({'name': 'CoinC', 'liquidity': 15000, 'market_cap': 800000, 'age': 0.5}, filtered_coins)

if __name__ == '__main__':
    unittest.main()