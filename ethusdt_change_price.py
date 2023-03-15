import time
from threading import Thread

from binance.client import Client

api_key = 'h7RIj7xQvMDBJCwLbqv8XqC2LofwjLjdvlGrwBUhJfttJaaJ3OgUbwfbbb7pUkK9'
api_secret = '9JmuI5aSoXgvww3odwshdj0cC1wnuB2oEmqhH6svqZpGuuS6zy0Wx6zCsgT4RGd1'

client = Client(api_key, api_secret)
symbol = "ETHUSDT"


# Returns klines for the specified symbol and interval
def get_klines(interval):
    return client.futures_klines(
        symbol=symbol,
        interval=interval,
        limit=60
    )


# Calculates the change in price over the last hour
def calculate_change():
    while True:
        klines = get_klines(Client.KLINE_INTERVAL_1MINUTE)
        start_price = float(klines[0][1])
        end_price = float(klines[59][4])

        percent = (end_price - start_price) / start_price * 100
        # Checks if the price has changed by 1% in the last hour
        if abs(percent) >= 1:
            print("ETH price has changed by more than 1% in the last 60 minutes.")
            time.sleep(10)


def price_change_symbol():
    while True:
        klines = get_klines(Client.KLINE_INTERVAL_1MINUTE)
        price_symbol = float(klines[0][1])

        print(price_symbol)
        time.sleep(20)


t1 = Thread(target=calculate_change)
t2 = Thread(target=price_change_symbol)
t1.start()
t2.start()
t1.join()
t2.join()

