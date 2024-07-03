import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # Done: Fill in this function.
    # Represent data in 3d
    data = prices.reset_index().pivot(index='date', columns='ticker', values='price')
    # print(data.info())

    # Resample time series data to Month End. The method expects a datetime Index.
    prices_res = data.resample('M').last()
    # print(prices_res.iloc[:10,:2])

    #calculate returns
    prices_log_ret = np.log(prices_res) - np.log(prices_res.shift())

    #calculate standard deviation of log returns and return index (ticker) of most volatile stock
    return prices_log_ret.std().idxmax()



def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()