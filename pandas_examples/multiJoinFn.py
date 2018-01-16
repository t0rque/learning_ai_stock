''' Same as multip join but using the python 
function for get data and get symbol '''
import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    ''' Return CSV file for the given symbol '''
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
def get_data(symbols, dates):
    '''Read data from CSV files '''
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols: #ADD SPY for reference
        symbols.insert(0,'SPY')
    for symbol in symbols:
        df1_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        # data can be sorted based on stock symbol
        df1_temp = df1_temp.rename(columns={'Adj Close':symbol})
        df = df.join(df1_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])
    return df



def test_run():
    start_date = '2015-01-22'
    end_date = '2015-01-26'
    dates = pd.date_range(start_date, end_date)
    syms = ['GOOG', 'IBM', 'GLD']
    print get_data(syms,dates) 


if __name__ == "__main__":
    test_run()
