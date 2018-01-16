import os
import pandas as pd

def test_run():
    start_date = '2015-01-22'
    end_date = '2015-01-26'
    dates = pd.date_range(start_date, end_date)
    #build empty data frame for date range
    df1 = pd.DataFrame(index=dates)

    #read SPY info with date indexing
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

    #rename the column from Adj Close to stock name so that join doesnt complain about column name and 
    # data can be sorted based on stock symbol
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    #update the empty frame with SPY details.
    df1 = df1.join(dfSPY, how='inner')

    #Read More Stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df1_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    #rename the column from Adj Close to stock name so that join doesnt complain about column name and 
    # data can be sorted based on stock symbol
        df1_temp = df1_temp.rename(columns={'Adj Close':symbol})
        df1 = df1.join(df1_temp)

    print df1


if __name__ == "__main__":
    test_run()
