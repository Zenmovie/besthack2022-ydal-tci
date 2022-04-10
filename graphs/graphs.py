import time
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

start = datetime.now()

key = 'TVXR0BDVKJAVY9ZZ'
base_url = 'https://www.alphavantage.co/query?'
ts = TimeSeries(key=key, output_format='pandas')


def make_candlestick(symbol: str):
    data, meta_data = ts.get_intraday(symbol=symbol, interval="5min", outputsize='full')
    data.to_excel('stock_data.xlsx')
    df = pd.read_excel('stock_data.xlsx')
    fig = go.Figure(data=[go.Candlestick(x=df['date'],
                    open=df['1. open'],
                    high=df['2. high'],
                    low=df['3. low'],
                    close=df['4. close'])])
    fig.update_layout(title=symbol)
    fig.show()


company_li = ['IBM', 'MSFT', 'AAPL', 'GOOG', 'AMZN', 'JPM', 'TSLA', 'TSM', 'NVDA', 'BABA']

counter = 0
for i in range(len(company_li)):
    if counter == 5:
        time.sleep(60)
    make_candlestick(company_li[i])
    counter += 1

print(datetime.now() - start)

