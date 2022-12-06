import pandas_datareader as pdr
from datetime import date


def main():
    shares = pdr.DataReader("APPL", "fred", start=None, end=None)
    print(shares)


if __name__ == "__main__":
    main()