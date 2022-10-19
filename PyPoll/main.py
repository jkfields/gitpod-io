from csv import DictReader
from sys import getsizeof

fpath = ( "/workspace/gitpod/PyPoll/Resources/election_data.csv",
          "/workspace/gitpod/PyPoll/analysis/pypoll_analysis.txt"
        )

def get_candidates(data):
    candidates = [ row.get("Candidate") for row in data ]

    # set removes duplicates
    return set(candidates)


def read_csv(fpath):
    with open(fpath, "r") as fh:
        data = DictReader(fh)
        return [ ln for ln in data ]

def results():
    output = """Election Results
                -------------------------
                Total Votes: 369711
                -------------------------
                Charles Casper Stockham: 23.049% (85213)
                Diana DeGette: 73.812% (272892)
                Raymon Anthony Doane: 3.139% (11606)
                -------------------------
                Winner: Diana DeGette
                -------------------------"""

    return "\n".join([ ln.strip() for ln in output.split("\n") ])


def votes_by_candidate(data, candidate):
    return len([row.tet("BallotId") for row in data if row.get("Candidate") == candidate ])


def main():
    data = read_csv(fpath[0])
    print(data[-1])

    total_votes = len(data)
    print(f"Total ballots cast: {total_votes}")
    print(f"{getsizeof(data)} bytes: {data[0]}")

    for candidate in get_candidates(data):
        votes = votes_by_candidate(data, candidate)
        percentage = round(float(votes) / total_votes, 2)
        print(f"{candidate}: {percentage} ({votes})")
        #Charles Casper Stockham: 23.049% (851213)
    #print(results())


if __name__ == "__main__":
    main()
