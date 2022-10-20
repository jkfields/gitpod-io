from csv import reader
from os import linesep

csvpath = "PyPoll/Resources/election_data.csv"
csvpath = "Resources/election_data.csv"

num_rows = 0

# candates name and number of votes received
votes = {}

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        num_rows += 1
        candidate = row[2]
        
        if candidate in votes.keys():
            votes[candidate] += 1
        else:
            votes[candidate] = 1

results = []
for candidate in votes.keys():
    results.append(f"{candidate}: {round(100 * votes[candidate] /num_rows, 3)}% ({votes[candidate]})")

winner = max(votes, key=votes.get)

output = f"""
  ```text
  Election Results
  ----------------------------
  Total Votes: {num_rows}
  ----------------------------
  {linesep.join([row for row in results]}
  -------------------------
  Winner: {winner}
  -------------------------
  ```

"""

# supposed to go in the analysis folder per assignment setup
with open("analysis/pypoll.txt", "w") as fh:
    fh.write(output)

print(output)
