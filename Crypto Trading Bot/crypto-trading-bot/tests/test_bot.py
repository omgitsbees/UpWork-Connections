import unittest
from src.bot import TradingBot

class TestTradingBot(unittest.TestCase):

    def setUp(self):
        self.bot = TradingBot()

    def test_initialization(self):
        self.assertIsNotNone(self.bot)
        self.assertEqual(self.bot.strategy, "Bollinger Bands")
        self.assertEqual(self.bot.risk_management["stop_loss"], 0.02)
        self.assertEqual(self.bot.risk_management["take_profit"], 0.05)

    def test_trade_logic(self):
        # Simulate a scenario where the bot should execute a LONG trade
        self.bot.current_price = 105
        self.bot.upper_band = 100
        self.bot.lower_band = 90
        self.bot.execute_trade()
        self.assertIn("LONG", self.bot.trades)

        # Simulate a scenario where the bot should execute a SHORT trade
        self.bot.current_price = 85
        self.bot.upper_band = 90
        self.bot.lower_band = 80
        self.bot.execute_trade()
        self.assertIn("SHORT", self.bot.trades)

    def test_risk_management(self):
        self.bot.balance = 1000
        self.bot.current_price = 100
        self.bot.execute_trade()
        self.assertEqual(self.bot.balance, 980)  # Assuming a trade was executed with 2% risk

    def test_learning_mechanism(self):
        initial_length = self.bot.bb_length
        self.bot.analyze_trade_history()
        self.assertNotEqual(initial_length, self.bot.bb_length)  # Ensure the length has been adjusted

if __name__ == '__main__':
    unittest.main()