import backtrader as bt
import yfinance as yf
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from datetime import datetime
import alpaca_trade_api as tradeapi
import dash
from dash import dcc, html
import plotly.graph_objects as go
from flask import Flask, jsonify, request
import sqlite3

# Define Moving Average Strategy
class MovingAverageStrategy(bt.Strategy):
    params = (
        ('fast', 10),
        ('slow', 20),
        ('risk_per_trade', 0.01),
    )

    def __init__(self):
        self.fast_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.fast)
        self.slow_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.slow)
        self.crossover = bt.indicators.CrossOver(self.fast_ma, self.slow_ma)
        self.initial_cash = self.broker.get_cash()
        self.position_size = None
        self.risk_amount = self.initial_cash * self.params.risk_per_trade

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy(size=self.position_size)
        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()

# Define Backtesting function
def run_backtest():
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MovingAverageStrategy)

    data = bt.feeds.PandasData(dataname=yf.download('AAPL', '2020-01-01', '2021-01-01'))
    cerebro.adddata(data)

    cerebro.broker.set_cash(100000)
    cerebro.broker.setcommission(commission=0.001)

    initial_value = cerebro.broker.getvalue()
    cerebro.run()
    final_value = cerebro.broker.getvalue()
    print(f"Initial Value: {initial_value}, Final Value: {final_value}")

# Define LSTM Model
def create_lstm_model():
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(60, 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Real-Time Trading Function
def trade_live(symbol):
    api_key = "your_alpaca_api_key"
    api_secret = "your_alpaca_api_secret"
    base_url = "https://paper-api.alpaca.markets"
    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

    account = api.get_account()
    print(f"Account Balance: ${account.cash}")

    # Place an order
    api.submit_order(
        symbol=symbol,
        qty=1,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

# Initialize Dash app
def create_dashboard():
    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.H1("Trading Strategy Performance"),
        dcc.Graph(id="backtest-chart"),
    ])

    @app.callback(dash.Output("backtest-chart", "figure"))
    def update_chart():
        fig = go.Figure()
        # Assuming a backtest result dataset
        dates = pd.date_range(start='2020-01-01', end='2021-01-01')
        prices = np.random.normal(100, 10, len(dates))
        fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name='AAPL Price'))
        return fig

    return app

# Flask API
app = Flask(__name__)

@app.route('/trade', methods=['POST'])
def api_trade():
    data = request.json
    symbol = data.get('symbol')
    side = data.get('side')
    quantity = data.get('quantity')

    if symbol and side and quantity:
        # Execute trade logic here
        trade_live(symbol)
        return jsonify({"status": "order placed"})
    else:
        return jsonify({"error": "Invalid data"}), 400

# User Management with SQLite
def init_user_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Main execution
if __name__ == '__main__':
    # Initialize User Database
    init_user_db()

    # Run Backtest
    run_backtest()

    # Create and run Dash dashboard
    dashboard_app = create_dashboard()
    dashboard_app.run_server(debug=True)

    # Start Flask API
    app.run(port=5000)
