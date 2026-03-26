import yfinance as yf

from dataloader import load_data

def create_signals(data):

    data["Return"]=data["Close"].pct_change()
