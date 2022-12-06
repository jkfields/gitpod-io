import pandas_datareader as pdr
from datetime import date


def main():
    shares = pdr.DataReader("APPL", "yahoo", start="1/1/2022", end="12/5/2022")
    print(shares)


if __name__ == "__main__":
    main()