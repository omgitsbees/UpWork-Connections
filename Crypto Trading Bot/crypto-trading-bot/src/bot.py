from coin_filter import filter_coins
from trade_executor import execute_trade
from learning_mechanism import optimize_parameters
import time
import json
import logging
from utils.config import API_KEYS
from utils.logger import setup_logger

# Set up logging
logger = setup_logger()

def load_learning_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    learning_data = load_learning_data('src/data/learning_data.json')
    
    while True:
        try:
            # Step 1: Filter and rank coins
            top_coins = filter_coins()
            logger.info(f'Top coins: {top_coins}')
            
            # Step 2: Execute trades based on alerts
            for coin in top_coins:
                execute_trade(coin)
            
            # Step 3: Optimize parameters based on learning data
            optimize_parameters(learning_data)
            
            # Sleep for a specified interval before the next iteration
            time.sleep(300)  # 5 minutes

        except Exception as e:
            logger.error(f'Error in main loop: {e}')
            time.sleep(60)  # Wait before retrying

if __name__ == '__main__':
    main()