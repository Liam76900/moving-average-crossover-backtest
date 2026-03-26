import yfinance as yf

from dataloader import load_data

def create_signals(data):

    data["Return"]=data["Close"].pct_change()

    short_ma=data["Close"].rolling(10).mean()

    long_ma=data["Close"].rolling(50).mean()
