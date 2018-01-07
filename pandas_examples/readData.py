import pandas as pd

def test_run():
    df = pd.read_csv("AAPL.csv")
    print 8*"#" + "Head" + 8*"#"
    print df.head()
    print 8*"#" + "tail" + 8*"#"
    print df.tail()
    print 8*"#" + "FULL" + 8*"#"
    print df
    print 8*"#" + "slicing" + 8*"#"
    print df[10:21] 

if __name__ == "__main__":
    test_run()
