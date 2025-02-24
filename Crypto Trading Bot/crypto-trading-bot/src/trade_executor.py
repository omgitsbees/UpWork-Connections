from ccxt import binance
import json
import requests
import time
import os
from utils.logger import logger
from utils.config import BINANCE_API_KEY, BINANCE_SECRET_KEY

class TradeExecutor:
    def __init__(self):
        self.exchange = binance({
            'apiKey': BINANCE_API_KEY,
            'secret': BINANCE_SECRET_KEY,
        })
        self.filtered_coins = []

    def set_filtered_coins(self, coins):
        self.filtered_coins = coins

    def execute_trade(self, signal, coin, amount):
        try:
            if signal == 'LONG':
                order = self.exchange.create_market_buy_order(coin, amount)
                logger.info(f'Executed LONG order for {coin}: {order}')
            elif signal == 'SHORT':
                order = self.exchange.create_market_sell_order(coin, amount)
                logger.info(f'Executed SHORT order for {coin}: {order}')
        except Exception as e:
            logger.error(f'Error executing trade for {coin}: {str(e)}')

    def listen_for_alerts(self):
        webhook_url = os.getenv('TRADINGVIEW_WEBHOOK_URL')
        while True:
            response = requests.get(webhook_url)
            if response.status_code == 200:
                alert_data = response.json()
                signal = alert_data.get('signal')
                coin = alert_data.get('coin')
                amount = alert_data.get('amount', 1)  # Default amount to 1 if not specified
                if coin in self.filtered_coins:
                    self.execute_trade(signal, coin, amount)
            time.sleep(5)  # Polling interval for alerts

if __name__ == "__main__":
    executor = TradeExecutor()
    # Example: Set filtered coins from a predefined list or external source
    executor.set_filtered_coins(['BTC/USDT', 'ETH/USDT', 'YZY/USDT'])
    executor.listen_for_alerts()