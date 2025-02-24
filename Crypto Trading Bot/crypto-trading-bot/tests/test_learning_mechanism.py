import unittest
from src.learning_mechanism import LearningMechanism

class TestLearningMechanism(unittest.TestCase):

    def setUp(self):
        self.learning_mechanism = LearningMechanism()

    def test_initialization(self):
        self.assertIsNotNone(self.learning_mechanism)

    def test_optimize_parameters(self):
        trade_history = [
            {'result': 'win', 'bb_length': 20, 'bb_multiplier': 2.2},
            {'result': 'loss', 'bb_length': 20, 'bb_multiplier': 2.2},
            {'result': 'win', 'bb_length': 25, 'bb_multiplier': 2.0},
        ]
        optimized_params = self.learning_mechanism.optimize_parameters(trade_history)
        self.assertIn('bb_length', optimized_params)
        self.assertIn('bb_multiplier', optimized_params)

    def test_adjust_stop_loss_take_profit(self):
        volatility = 0.05
        stop_loss, take_profit = self.learning_mechanism.adjust_stop_loss_take_profit(volatility)
        self.assertGreaterEqual(stop_loss, 0)
        self.assertGreaterEqual(take_profit, stop_loss)

    def test_learning_data_integration(self):
        self.learning_mechanism.load_learning_data('src/data/learning_data.json')
        self.assertGreater(len(self.learning_mechanism.trade_history), 0)

if __name__ == '__main__':
    unittest.main()