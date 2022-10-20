import csv

csvpath = "PyBank/Resoucres/budget_data.csv"
csvpath = "Resources/budget_data.csv"

total_months = 0
pl_total = 0
net_total = 0
previous_net = 0

high_change = 0
high_month = ""

low_change = 0
low_month =""

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # don't need this in a variable unless you're gonna use it
    next(csvreader)

    total_months = 0
    pl_total = 0
    net_total = 0
    
    min_change = 0
    min_month = ""
    
    max_change = 0
    max_month = ""
    
    for row in csvreader:
        pl = int(row[1])
        pl_total += pl
 
        # track the average change
       if total_montsh > 0:
           net_change = pl - previous_net
           net_total += net_change

        previous_net = pl

        if net_change < min_change:
            min_change = net_change
            min_month = row[0]
        
        if net_change > max_change:
            max_change = net_change
            max_month = row[0]

        # count the rows
        total_months += 1 

net_monthly_avg = round(net_total / (total_months - 1), 2)


"""
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: ${total_months}")
print(f"Total: {pl_total}")
print(f"Average Change: ${net_monthly_avg}")
print(f"Greatest Increase in Profits: ${max_change}")
print(f"Greatest Decrease in Profits: ${min_change}")
print("---")
"""

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${pl_total}
Average Change: ${net_monthly_avg}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})
"""

fpath = "pybank.txt"
with open(fpath, "w") as analysis:
    analysis.write(output)

print(output)