def backtesting(data):
    data["Strategy_Returns"]=data["Signal"] * data["Return"]
<<<<<<< HEAD
    
=======

>>>>>>> 5caa5b849eb32e1e16a62febca2176c8ff6afe95
    data["Cumulative_Market"]=(1+data["Return"]).cumprod()
    data["Cumulative_Strategy"]=(1+data["Strategy_Returns"]).cumprod()

    return data