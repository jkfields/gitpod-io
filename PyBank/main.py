import csv
from statistics import mean
import sys

# generate the analysis
def analysis(months, total, average, increase, decrease):
    output = f"""Financial Analysis
                ----------------------------
                Total Months: {months}
                Total: ${total}
                Average Change: ${average}
                Greatest Increase in Profits: {increase}
                Greatest Decrease in Profits: {decrease}   
              """

    """ this is purely due to the indentation of the output string
        format above to remove the indentation which isn't needed 
       in the displayed and file output """
    return '\n'.join(ln.strip() for ln in output.split("\n"))


# we have no comparison for the initial month; so we drop it
def average_change(data):
    changes = [ row.get("change") for idx, row in enumerate(data) if idx > 0 ]
    return  round(sum(changes) / len(changes), 2)
    

# get the minimum change
def get_maximum(data):
    delta = max(data, key=lambda row:row.get("change"))
    return f"{delta.get('Date')} ({delta.get('change')})"


def  get_minimum(data):
    delta = min(data, key=lambda row:row.get("change"))
    return f"{delta.get('Date')} ({delta.get('change')})"
    

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

             
def save_analysis(fpath, output):
    with open(fpath, "w") as fh:
        fh.write(output)


def main():
    fpath = ("/workspace/gitpod/PyBank/Resources/budget_data.csv", 
             "/workspace/gitpod/PyBank/analysis/pybank_analysis.txt")

    data = csv_to_dict(fpath[0])
  
    months = number_of_months(data)
    total = sum_of_profits(data)
    minimum = get_minimum(data)
    maximum = get_maximum(data)
    average = average_change(data)

    output = analysis(months, total, average, maximum, minimum)
    save_analysis(fpath[1], output)
    print(output)


if __name__ == "__main__":
    main()
