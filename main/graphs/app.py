import time
from flask import Flask, render_template, request, flash, redirect, jsonify
from datetime import datetime
import twelvedata as twd
from twelvedata import TDClient
import json


app = Flask(__name__)
td = TDClient("32d5929173a54fa6a74c215aac19b23e")


def get_stock_data(symbol: str, interval: str, outputsize: int) -> json:

    def json_date(time: str):
        try:
            date_time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            date_time = datetime.strptime(time, '%Y-%m-%d')
        epoch = datetime.utcfromtimestamp(0)
        return (date_time - epoch).total_seconds()

    candlesticks = td.time_series(
        symbol=symbol,
        interval=interval,
        outputsize=outputsize,
        timezone="Europe/Moscow"
    ).as_json()

    processed_candlestick = []
    for data in candlesticks:
        candlestick = [
            json_date(data['datetime']),
            data['open'],
            data['high'],
            data['low'],
            data['close'],
        ]
        processed_candlestick.append(candlestick)

    processed_candlestick = processed_candlestick[::-1]
    return jsonify(processed_candlestick)


@app.route('/')
def index():
    title = 'Stock Chart'
    return render_template('index.html', title=title)


@app.route('/stocks/<symbol>')
def stock_data(symbol):
    return get_stock_data(symbol, '5min', 500)


