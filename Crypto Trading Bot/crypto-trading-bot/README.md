# Crypto Trading Bot

## Overview
The Crypto Trading Bot is designed to automate cryptocurrency trading using a strategy based on Bollinger Bands. It filters and ranks coins based on various criteria and executes trades on Binance. The bot incorporates a learning mechanism to optimize its trading strategy over time.

## Features
- **Bollinger Bands Strategy**: Utilizes Bollinger Bands for generating trading signals.
- **Coin Filtering**: Filters and ranks coins based on liquidity, market cap, and age.
- **Trade Execution**: Executes trades on Binance based on alerts from TradingView.
- **Learning Mechanism**: Analyzes trade history and optimizes parameters using machine learning techniques.
- **Logging and Error Handling**: Provides insights into operations and manages API requests securely.

## Project Structure
```
crypto-trading-bot
├── src
│   ├── bot.py                  # Main entry point for the trading bot
│   ├── coin_filter.py          # Functions for filtering and ranking coins
│   ├── trade_executor.py        # Handles trade execution on Binance
│   ├── learning_mechanism.py    # Implements the learning mechanism
│   ├── utils
│   │   ├── api_handler.py       # Manages API requests and responses
│   │   ├── config.py            # Configuration settings
│   │   └── logger.py            # Logging utility
│   └── data
│       └── learning_data.json   # Historical trade data
├── tests
│   ├── test_bot.py              # Unit tests for the bot's functionalities
│   ├── test_coin_filter.py      # Unit tests for coin filtering functions
│   ├── test_trade_executor.py    # Unit tests for trade execution logic
│   └── test_learning_mechanism.py # Unit tests for the learning mechanism
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
└── .env                         # Environment variables
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd crypto-trading-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your API keys and settings in the `.env` file.

## Usage
- Run the bot using the following command:
  ```
  python src/bot.py
  ```

- Ensure that your TradingView alerts are set up to trigger the bot's trading logic.

## Testing
To run the unit tests, use:
```
pytest tests/
```

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.