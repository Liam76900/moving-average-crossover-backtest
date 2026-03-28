def backtesting(data):

    #Computes strategy returns by multiplying the return value by the signal value so the return is only awarded when the signal is 1

    data["Strategy_Returns"]=data["Signal"] * data["Return"]

    #This represents the transaction cost

    cost=0.001

    #This returns either a 1 or 0, a 1 when the stock is bought or sold and 0 otherwise

    data["Trade"]=data["Signal"].diff().abs()

    #This means that the transaction cost is only accounted for when the position in the market changes

    data["Transaction_Costs"]=data["Trade"] * cost

    #Computes net strategy returns by finding the difference between the strategy returns and the transaction costs values

    data["Net_Strategy_Returns"]=data["Strategy_Returns"] - data["Transaction_Costs"]

    #Creates a new column called market transaction costs and makes all entries 0.0
    #This is done as the buy and hold strategy will only have transaction costs implemented at the start and end of the time period so the rest of the values will be 0.0

    data["Market_Transaction_Costs"]=0.0

    #Changes the first and last entries to the value of cost where the stock was bought and sold

    data.loc[data.index[0], "Market_Transaction_Costs"] = cost
    data.loc[data.index[-1], "Market_Transaction_Costs"] = cost

    #Net market returns found by finding the difference between the market transaction costs and the return values

    data["Net_Market_Returns"]=data["Return"] - data["Market_Transaction_Costs"]

    #Computes the cumulative returns of market and strategy by changing the net return values into growth factors and compounding these values

    data["Cumulative_Market"]=(1+data["Net_Market_Returns"]).cumprod()
    data["Cumulative_Strategy"]=(1+data["Net_Strategy_Returns"]).cumprod()

    return data