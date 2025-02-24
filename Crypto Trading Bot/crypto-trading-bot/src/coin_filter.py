def fetch_coin_data(api_handler, criteria):
    # Fetch coin data from the API
    response = api_handler.get_coin_data()
    if response is None:
        return []

    filtered_coins = []
    for coin in response:
        if (coin['liquidity'] >= criteria['min_liquidity'] and
            criteria['min_market_cap'] <= coin['market_cap'] <= criteria['max_market_cap'] and
            coin['age'] <= criteria['max_age']):
            filtered_coins.append(coin)

    return filtered_coins


def rank_coins(coins):
    # Rank coins based on market cap and liquidity
    ranked_coins = sorted(coins, key=lambda x: (x['market_cap'], x['liquidity']), reverse=True)
    return ranked_coins


def get_top_coins(api_handler, criteria, top_n=10):
    # Get top N coins based on filtering and ranking
    filtered_coins = fetch_coin_data(api_handler, criteria)
    ranked_coins = rank_coins(filtered_coins)
    return ranked_coins[:top_n]