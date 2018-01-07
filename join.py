import pandas as pd

def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    #build empty data frame for date range
    df1 = pd.DataFrame(index=dates)

    #read SPY info with date indexing
    dfSPY = pd.read_csv("SPY.csv", index_col="Date", parse_dates=True)
    print dfSPY

    #update the empty frame with SPY details.
    df1 = df1.join(dfSPY)
    print df1



if __name__ == "__main__":
    test_run()
