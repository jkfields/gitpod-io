import pandas_datareader as pdr
from datetime import date


def main():
    shares = pdr.DataReader("APPL", "google", start="2022-01-01", end="2022-06-30")
    print(shares)


if __name__ == "__main__":
    main()