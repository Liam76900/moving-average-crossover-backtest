from dataloader import load_data
from strategy import create_signals
from backtest import backtesting
from metrics import calculate_metrics

windows=[(5,20),(10,50),(20,100)]
symbols=["AAPL","MSFT","GOOGL"]

for short_window,long_window in windows:
    for symbol in symbols:

        data=load_data(symbol)
        data=create_signals(data, short_window, long_window)
        data=backtesting(data)

        print(f"Results for {symbol} for {short_window} day short window and {long_window} day long window is")
        print(data[["Cumulative_Market", "Cumulative_Strategy"]].tail())
        sharpe_ratio, annualised_volatility, max_drawdown=calculate_metrics(data)
        print("Sharpe ratio:")
        print(sharpe_ratio)
        print("Annualised Volatility:")
        print(annualised_volatility)
        print("Max Drawdown:")
        print(max_drawdown)