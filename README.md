Markdown

Multi-Asset Backtesting of a Moving Average Crossover Strategy

#Overview

This project acts as a simulation of a moving average crossover trading strategy against a buy and hold strategy with mutiple different assets. It also simulatneously incorporates different parameter choices (moving average windows) which help to interpret how these conditions affect risk and returns as well as having transaction costs for when a trade is made to increase the precision of my returns.

#How to run

Install the required libraries:
```bash
pip install numpy pandas matplotlib yfinance

1. Clone this repository:
```bash
git clone https://github.com/Liam76900/moving-average-crossover-backtest.git
cd moving-average-crossover-backtest

2. Run the script:
python main.py

#Features

-Multi-asset backtesting
-Many risk metrics including Sharpe Ratio, Maximum Drawdown and Annualised Volatility
-A set of parameter choices(window combinations)
-Transaction costs
-Moving Average Crossover Strategy
-Comparative data against a buy and hold strategy
-Graphical visualisations of Cumulative Returns and Drawdowns

#Method and Logic

Signals are generated depending on the relationship between short-term and long-term moving averages. When the short-term moving average surpasses the long-term moving average, a long position is taken. Conversely, when the short-term moving average sinks below the long-term moving average, the position is closed. These binary signals shows whether the strategy is exposed to price movements where 1 indicates you are in the market (long position) and, 0, out of the market.

Strategy returns are computed from the percentage change in  asset prices and multiplied by the signal to ensure that these returns are only being granted when the strategy is in a long position.

The cumulative performance of the strategy is calculated by compounding the strategy returns to mirror the growth of the investment progressively. This same technique is used for the cumulative market (buy and hold) returns as a control.

The Buy and Hold strategy makes the assumption that the investor buys at the start and holds it throughout the duration of the time. This then serves as a reference to observe whether the strategy adds value.

The risk metrics taken into account are the sharpe ratio, annualised volatility and maximum drawdown. Sharpe ratio measures risk-adjusted returns to perceive whether the returns made are in fact as valuable as the risk taken. Annualised volatility represents how variable the stock prices are with higher percentages indicating greater risk, and lower percentages, more stability. Max drawdowns takes into account the greatest peak-to-trough decline in stock value, demonstrating the worst potential outcome of an investment.

The strategy is also tested against a selection of different short-term and long-term windows of [5, 10, 20] and [20, 50, 100] days respectively. This, therefore, allows us to analyse the sensitivity of the strategy to the parameter choices made.

#Results

| Asset | MA Windows | Strategy Return (%) | Market Return (%) | Annualised Volatility (%) | Sharpe | Max Drawdown (%) |
|-------|------------|---------------------|-------------------|---------------------------|--------|------------------|
| AAPL  | 5  / 20    |      20.03          |       54.49       |         16.32             | 1.218  |     -14.69       |
| MSFT  | 5  / 20    |      20.43          |       58.03       |         19.61             | 1.061  |     -13.23       |
| GOOGL | 5  / 20    |     -0.992          |       56.43       |         24.80             | 0.084  |     -16.53       |
| AAPL  | 10 / 50    |      16.91          |       54.49       |         13.16             | 1.272  |     -12.64       |
| MSFT  | 10 / 50    |      34.62          |       58.03       |         19.62             | 1.637  |     -13.93       |
| GOOGL | 10 / 50    |      13.30          |       56.43       |         23.54             | 0.657  |     -19.59       |
| AAPL  | 20 / 100   |      08.99          |       54.49       |         10.68             | 0.872  |     -11.31       |
| MSFT  | 20 / 100   |      04.19          |       58.03       |         14.75             | 0.356  |     -13.07       |
| GOOGL | 20 / 100   |      12.99          |       56.43       |         20.59             | 0.706  |     -13.08       |

#Plot of Strategy Returns of all assets with the [5, 20]
 day window against time

<p align="center">
  <img src=".\images\five-twenty.png" alt="Moving Average" width="600"/>
</p>

#Plot of Strategy Returns of all assets with the [10, 50]
 day window against time

<p align="center">
  <img src=".\images\ten-fifty.png" alt="Moving Average" width="600"/>
</p>

#Plot of Strategy Returns Vs Market Returns of all assets with the [10, 50]
day window against time

<p align="center">
  <img src=".\images\ten-fifty-market-strategy.png" alt="Moving Average" width="600"/>
</p>

#Plot of Strategy Return Drawdowns of all assets with the [10, 50] day window against time

<p align="center">
  <img src=".\images\ten-fifty-d.png" alt="Moving Average" width="600"/>
</p>

#Analysis of Results

-Risk-adjusted performance and capital preservation
  -Strategy exhibited lower upside capture compared to benchmark buy and hold strategy due to high Bull Market Beta observed during the sample duration
  -However, strategy offers superior capital preservation as seen by 10/50 MSFT configuration achieving a sharpe ratio of 1.637 as well as a 34.62% return
  -Demonstrates a strong risk-adjusted performance compared to the market

-Optimal parameter
  -10/50 Window: ighlighted as most optimal by returning the consistently best results
  -5/20 Window: too sensitive leading to false signals (whiplaws) which contracts unneccesary transaction costs
  -20/100 Window: extreme lagging leading to taking the long position too late into trends and selling way past peaks

-Volaitlity dampening and drawdown analysis
  -Annualsied volatility decreases as the length of window increases 
  -Strategy acts as a filter to reduce exposure to the market during highly volatile periods (AAPL annualised volatility from 16.32% to 10.68%)
  -Max drawdowns are less than 20% throughout all results meaning that if maximum loss is made the return needed to recover is reduced compared to the typical benchmark buy and hold strategy
  -Highlights usefulness of strategy to more risk-averse investors

-Strategy Limitations
  -Effecfiveness of strategy erodes as volatility of market increases
  -As seen by 5/20 GOOGL configuration, tight windows can amplify losses by entering and exiting the market at erroneous times during highly flucuating price movements

  #Conclusion

  My moving average crossover strategy underperformed against the benchmark buy and hold strategy due to its lagging nature in a strong bull market, where it takes the long position after upward trends have begun and exiting after peaks. However, it improves risk-adjusted returns by reducing volatility and max drawdowns.

  Over the results, the 10/50 window configuration appears most optimal with the most consistently high returns and, overall, the best sharpe ratios. In contrast, the 5/20 configuration was extremely sensitive, generating noise-driven trades and the 20/100 configuration suffering from excessive lag; making trades after trends have passed.
  
  As seen by results, the strategy fails in highly volatile markets as moving average crossover strategies are trend-following and lagging indicators so the fluctuating stock prices create whipsaws that, therefore, erode returns due to amplifying losses and escalating unnecessary transaction costs.

  Potential improvements I would make to this project are benchmarking drawdowns against the buy and hold strategy to better quantify how my strategy diminishes risk, as well as, including dynamic parameter optimisation to adapt to ever-changing market regimes. Further extensions including incorporating more metrics and regime-filters to improve the robustness of my strategy.

  Ultimately, I think my project has given great insight on the trade-offs between risk and return in systematic trading strategies and the importance of adapting models to different market regimes.