### (Dad) only import what you need
### from csv import reader
import csv

### (Dad) Path is wrong; should be "Resources" based on
### the challenge setup; and the path needs to be defined
### based on where "main.py" is being called of the full
### path to the file
csvpath = "PyPoll/Resources/election_data.csv"

rows = 0
#dict
### (Dad) you don't need the above comment; it is obvious
### that is a dict; a good comment would be the structure
### you plan to put in it!
votes = {}

with open(csvpath, encoding='utf-8') as csvfile:
    ### (Dad) if you import as above, ths becomes:
    ### csvreader = reader(csvfile, delimiter=","
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#sum the number of rows minus the header
    ### (Dad) indent comments to the line they go with; like this one
    for row in csvreader:
        ### (Dad) keep spacing consistent; if you add a space before "+="
        ### (and you should), you need to add a space after, like:
        ### rows += 1
        rows +=1

        ### (Dad) put a blank like before a comment; code should always be
        ### easily readable; even more so when submitting for a grade.
        #row,column 3
        candidate =row[2]
#number of rows not including header = total votes
        ### (Dad) indent comments to the line they go with; like this one; also,
        ### same comment as above about spacing
        if candidate in votes.keys():
            ### (Dad) votes[candidate] += 1
            votes[candidate] +=1
        else:
            votes[candidate] =1
          
            ### (Dad) This is going to print 3 times; you only want it to print once
            ### If you're going to do it like this, you need to print the top part of
            ### the analysis before you start this loop, but you don't have all the
            ### data yet so this won't work.abs(x)
            print("Election Results")
### (Dad) Again, spacing; a single blank line when you leave a block (indented) of code
print("-------------------------")
print(f"Total Votes: {rows}")
print("-------------------------")
for runner in votes.keys():
    print(F"{runner}: {round(100*votes[runner]/rows,3)}% ({votes[runner]})")


### (Dad) too many blank lines; as a rule of thumb, a single blank lines between blocks
### of code; 2 blank lines between classes and functions!  For example,
###
### 
### def add(x, y):
###     return x + y
###
###
### def divide(x, y):
###     if y == 0:
###         raise ZeroDivisionError(f"y cannot be {y}")
###     else:
###        return x / y
###
###
### x = 2
### y = 3
###
### z = add(x, y)
### print(f"{x} + {y} = {z}")
###
### d = divide(x, y)
### print(f"{x} / {y} = {d}")
##

#use dict to get the number of votes per runner



#use dict to get max votes for the winner
winner = max(votes, key=votes.get)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

### (Dad) Better way to do the output, but
### you'll need to use a data structure (list, dict, etc)
### to hold the candidate data so that you can generate
### that output and hold the info to determine the winner, etc.
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

### (Dad) use a "with" for this like you did with the csv file
file = open("pypoll.txt", "w")
file.write(output)
file.close()