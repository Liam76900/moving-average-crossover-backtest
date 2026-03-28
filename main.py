import matplotlib.pyplot as plt
from dataloader import load_data
from strategy import create_signals
from backtest import backtesting
from metrics import calculate_metrics

#Assigns the different parameters for the windows of time and the different assets

windows=[(5,20),(10,50),(20,100)]
assets=["AAPL","MSFT","GOOGL"]

#Loops through the different parameters for the windows of time

for short_window,long_window in windows:

    #Creates a new figure for our plot

    plt.figure(figsize=(10, 5))

    #Loops through the different assets

    for asset in assets:

        #Assigned variables are ran through the different defined functions

        data=load_data(asset)
        data=create_signals(data, short_window, long_window)
        data=backtesting(data)
        sharpe_ratio, annualised_volatility, max_drawdown=calculate_metrics(data)

        #Outputs the dataframe for Cumulative Market and Strategy Return values

        print(f"Results for {asset} for {short_window} day short window and {long_window} day long window is")
        print(data[["Cumulative_Market", "Cumulative_Strategy"]].tail())

        #Outputs Risk Metrics

        print("Sharpe ratio:")
        print(sharpe_ratio)
        print("Annualised Volatility:")
        print(annualised_volatility)
        print("Max Drawdown:")
        print(max_drawdown)

        #Plots Cumulative Strategy Returns of all the different asssets over the time frame

        plt.plot(data["Cumulative_Strategy"], label=asset)

    #Adds legend, axis labels, title, gridlines to graph and returns the graph

    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Returns")
    plt.title("Strategy Returns Over Assets")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

    #Creates a new figure for our plot

    plt.figure(figsize=(10, 5))

    #Loops through different assets

    for asset in assets:

        #Assigned variables are ran through the different defined functions

        data=load_data(asset)
        data=create_signals(data, short_window, long_window)
        data=backtesting(data)
        sharpe_ratio, annualised_volatility, max_drawdown=calculate_metrics(data)

        #Plots graph of drawdown against time
        
        plt.plot(data["Drawdown"], label=asset)

    #Adds legend, axis labels, title, gridlines to graph and returns the graph

    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Drawdown")
    plt.title("Drawdown Over Time")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()