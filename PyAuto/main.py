import pandas as pd
#import sqlite3

def get_data(location):
    headers = [ "symboling",
            "normalized-losses",
            "make",
            "fuel-type",
            "aspiration",
            "num-of-doors",
            "body-style",
            "drive-wheels",
            "engine-location",
            "wheel-base",
            "length",
            "width",
            "height",
            "curb-weight",
            "engine-type",
            "num-of-cylinders",
            "engine-size",
            "fuel-system",
            "bore",
            "stroke",
            "compression-ratio",
            "horsepower",
            "peak-rpm",
            "city-mpg",
            "highway-mpg",
            "price",
          ]

    data = pd.read_csv(location, header=None)
    data.columns = headers
    return data


def main():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

    data = get_data(url)
    print(data.describe())
    #print(data.info())

    # print some rows
    print()
    print(data.head(15))
    print(data.tail(15))

    # sava data with headers
    path = "/workspace/gitpod/PyAuto/automobiles.csv"
    data.to_csv(path)
    data.to_json("/workspace/gitpod/PyAuto/automobiles.json")
    data.to_excel("/workspace/gitpod/PyAuto/automobiles.xlsx")
    #data.to_sql("/workspace/gitpod/PyAuto/automobiles.sql", sqlite3.Connection("/workspace.gitpod/PyAuto/automobiles.db"))


if __name__ == "__main__":
    main()
