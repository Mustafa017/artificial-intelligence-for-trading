import pandas as pd
import numpy as np

def estimate_volatility(prices, l):
    """Create an exponential moving average model of the volatility of a stock
    price, and return the most recent (last) volatility estimate.
    
    Parameters
    ----------
    prices : pandas.Series
        A series of adjusted closing prices for a stock.
        
    l : float
        The 'lambda' parameter of the exponential moving average model. Making
        this value smaller will cause the model to weight older terms less 
        relative to more recent terms.
        
    Returns
    -------
    last_vol : float
        The last element of your exponential moving averge volatility model series.
    
    """
    # TODO: Implement the exponential moving average volatility model and return the last value.

    # calculate log returns
    price_returns = np.log(prices) - np.log(prices.shift())
    price_ret_squared = price_returns**2
    vol = np.sqrt(price_ret_squared.ewm(alpha=1-l).mean())
    last_vol = vol.iloc[-1].price
    return last_vol
    
def test_run(filename='data.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'], index_col='date')
    print("Most recent volatility estimate: {:.6f}".format(estimate_volatility(prices, 0.7)))

if __name__ == '__main__':
    test_run()