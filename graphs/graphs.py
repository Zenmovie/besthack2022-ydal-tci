from datetime import datetime
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.graph_objects as go

start = datetime.now()


def make_candlestick(symbol: str):
    data = yf.download(tickers=symbol, period='1d', interval='2m')
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'])])
    fig.update_layout(title=symbol)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=30, label="30m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig.show()


def make_linegraph(symbol: str):
    data = yf.download(tickers=symbol, period='1mo', interval='5m')
    fig = go.Figure([go.Scatter(x=data.index, y=data['Close'])])
    fig.update_layout(title=symbol)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1d", step="day", stepmode="backward"),
                dict(count=7, label="7d", step="day", stepmode="backward"),
                dict(count=21, label="21d", step="day", stepmode="backward"),
                dict(label="1M", step="all")
            ])
        )
    )
    fig.show()


company_li = ['IBM', 'MSFT', 'AAPL', 'GOOG', 'AMZN', 'JPM', 'TSLA', 'TSM', 'NVDA', 'BABA']

make_candlestick('MSFT')

print(datetime.now() - start)

