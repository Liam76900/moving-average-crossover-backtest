import yfinance as yf

#Loads real stock data of different assets from yfinance

def load_data(asset):
    data = yf.download(asset, start="2023-01-01", end="2024-01-01")
    data.columns = data.columns.droplevel(1)
    return data