import csv

csvpath = "Resoucres/election_data.csv"

rows = 0
#dict
votes = {}

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#sum the number of rows minus the header
    for row in csvreader:
        rows +=1
        #row,column 3
        candidate =row[2]
#number of rows not including header = total votes

        if candidate in votes.keys():
            votes[candidate] +=1
        else:
            votes[candidate] =1
            print("Election Results")
print("-------------------------")
print(f"Total Votes: {rows}")
print("-------------------------")
for runner in votes.keys():
    print(F"{runner}: {round(100*votes[runner]/rows,3)}% ({votes[runner]})")



#use dict to get the number of votes per runner



#use dict to get max votes for the winner
winner = max(votes, key=votes.get)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output = f"""
  ```text
  Election Results
  ----------------------------
  Total Votes: {rows}
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: {winner}
  -------------------------
  ```

"""
file = open("pypoll.txt", "w")
file.write(output)
file.close()