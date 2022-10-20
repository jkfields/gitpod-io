from csv import reader
from os import linesep

csvpath = "PyPoll/Resources/election_data.csv"

# my path; to use yours main.py must be executed
# from outsite PyPoll; you can just get rid of these
# 4 lines
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

# string of results for each candidate
results = []

# calculate percentage and results for each candidate
for candidate in votes:
    # pull this out of the string so that the algorithm is easily read
    percentage = round(100 * votes[candidate] /num_rows, 3)
    results.append(f"{candidate}: {percentage}% ({votes[candidate]})")

winner = max(votes, key=votes.get)

output = f"""
Election Results
----------------------------
Total Votes: {num_rows}
----------------------------
{linesep.join(results)}
-------------------------
Winner: {winner}
-------------------------
"""

# supposed to go in the analysis folder per assignment setup
with open("analysis/pypoll.txt", "w") as fh:
    fh.write(output)

print(output)
