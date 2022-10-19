import csv
from statistics import mean
import sys


def analysis(months=86,
             total=22564198,
             average=-8311.11,
             increase="Aug-16 ($1862002)",
             decrease="Feb-14 ($-1825558)"):
             
    output = f"""Financial Analysis
                ----------------------------
                Total Months: {months}
                Total: ${total}
                Average Change: ${average}
                Greatest Increase in Profits: Aug-16 ({increase})
                Greatest Decrease in Profits: Feb-14 ({decrease})"""

    """ this is purely due to the indentation of the output string
        format above to remove the indentation which isn't needed 
       in the output """
    return'\n'.join(ln.strip() for ln in output.split("\n"))


# we have not comparison for the initial month; so we drop it
def average_change(data):
    changes = [ row.get("change") for idx, row in enumerate(data) if idx > 0 ]
    return  round(sum(changes) / len(changes), 2)
    

# get the minimum change
def get_maximum(data):
    return 12346


def  get_minimum(data):
    #key = min(data, data.get)
    #return key, data.get(key)
    return 12
    
# number of months in input; assumes 1 month per line
def number_of_months(data):
    return len(data)

# calculate the total profit/loss for all months
def sum_of_profits(data):
    return sum(row.get("Profit/Losses") for row in data)


def csv_to_dict(fpath):
    # read the file and return a list of rows; each row a dict
    rows = []
    with open(fpath, "r") as fh:
        for idx, row in enumerate(csv.DictReader(fh)):
            # current profit/loss amount; initially a str
            pl = int(row.get("Profit/Losses"))

            # since were processing the row; update str to int
            row["Profit/Losses"] = pl

            """add the change to the row/month; if it is the first
               line of input there is no change to record; set 0,
               otherwise, value is the previous amount subtracted
               from the current amount. """
            row["change"] = 0 if idx == 0 else (pl - previous)
            previous = pl

            # add the row to the array we will return
            rows.append(row)

    return rows

             
def main():
    fpath = "/workspace/gitpod/PyBank/Resources/budget_data.csv"
    data = csv_to_dict(fpath)
  
    months = number_of_months(data)
    total = sum_of_profits(data)
    minimum = get_minimum(data)
    maximum = get_maximum(data)
    average = average_change(data)

    print(analysis(months, total, average, maximum, minimum))


if __name__ == "__main__":
    main()
