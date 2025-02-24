import unittest
from unittest.mock import patch, MagicMock
from src.trade_executor import TradeExecutor

class TestTradeExecutor(unittest.TestCase):

    @patch('src.trade_executor.ccxt')
    def setUp(self, mock_ccxt):
        self.mock_binance = MagicMock()
        mock_ccxt.binance.return_value = self.mock_binance
        self.trade_executor = TradeExecutor(api_key='test_api_key', api_secret='test_api_secret')

    def test_execute_long_trade(self):
        self.mock_binance.create_market_order.return_value = {'status': 'success'}
        result = self.trade_executor.execute_trade('LONG', 'BTC/USDT', 0.01)
        self.assertEqual(result['status'], 'success')
        self.mock_binance.create_market_order.assert_called_once_with('BTC/USDT', 'buy', 0.01)

    def test_execute_short_trade(self):
        self.mock_binance.create_market_order.return_value = {'status': 'success'}
        result = self.trade_executor.execute_trade('SHORT', 'BTC/USDT', 0.01)
        self.assertEqual(result['status'], 'success')
        self.mock_binance.create_market_order.assert_called_once_with('BTC/USDT', 'sell', 0.01)

    def test_execute_trade_invalid_type(self):
        with self.assertRaises(ValueError):
            self.trade_executor.execute_trade('INVALID', 'BTC/USDT', 0.01)

    def test_execute_trade_insufficient_funds(self):
        self.mock_binance.create_market_order.side_effect = Exception('Insufficient funds')
        with self.assertRaises(Exception) as context:
            self.trade_executor.execute_trade('LONG', 'BTC/USDT', 0.01)
        self.assertTrue('Insufficient funds' in str(context.exception))

if __name__ == '__main__':
    unittest.main()