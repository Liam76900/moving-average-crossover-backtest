def backtesting(data):
    data["Strategy_Returns"]=data["Signal"] * data["Return"]