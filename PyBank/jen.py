import csv

 

csvpath = "PyBank/Resoucres/budget_data.csv"

 

total_months = 0

pl_total = 0

net_change_list = []

 

with open(csvpath, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

 

    #grabbing the first row of data

    csv_first = next(csvreader)

    previous_net = int(csv_first[1])

    pl_total = int(csv_first[1])

 

    #print(f"CSV Header: {csv_header}")

    #x = csv_header[1]

    # print(x)

    for row in csvreader:

        # count the rows

        total_months += 1

        # sum the rows in column 2

        pl_total += int(row[1])

 

        # track the average change

        net_change = int(row[1])-previous_net

        net_change_list += [net_change]

        previous_net = int(row[1])

        # subtract row from previous row

        # sum differences

        # divide by iterations

 

       

 

net_monthly_avg = round(sum(net_change_list)/len(net_change_list),2)

min_change = min(net_change_list)

max_change = max(net_change_list)

 

print("Financial Analysis")

print("-------------------------")

print(f"Total Months: ${total_months}")

print(f"Total: {pl_total}")

print(f"Average Change: ${net_monthly_avg}")

print(f"Greatest Increase in Profits: ${max_change}")

print(f"Greatest Decrease in Profits: ${min_change}")

print("---")

 

output = f"""

  ```text

  Financial Analysis

  ----------------------------

  Total Months: {total_months}

  Total: ${pl_total}

  Average Change: ${net_monthly_avg}

  Greatest Increase in Profits: Aug-16 (${max_change})

  Greatest Decrease in Profits: Feb-14 ($-{min_change})

  ```

 

"""

file = open("pybank.txt", "w")

file.write(output)

file.close()