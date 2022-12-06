import pandas_datareader as pdr
from datetime import date


def main():
    start = date(2022, 1, 1)
    end = date(2022, 1, 31)
    data_source = "yahoo"

    shares = pdr.DataReader("BAC", data_source, start, end)
    #print(shares)


if __name__ == "__main__":
    main()