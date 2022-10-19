from csv import DictReader
from sys import getsizeof

fpath = ( "/workspace/gitpod/PyPoll/Resources/election_data.csv",
          "/workspace/gitpod/PyPoll/analysis/pypoll_analysis.txt"
        )

def calculate_percentage(numerator, denominator, precision=3):
    try:
        return round(float(numerator) / denominator * 100, precision)
    except (ValueError, TypeError, ZeroDivisionError):
        raise


def get_candidates(data):
    candidates = [ row.get("Candidate") for row in data ]

    # set removes duplicates
    return set(candidates)

def read_csv(fpath):
    with open(fpath, "r") as fh:
        data = DictReader(fh)
        return [ ln for ln in data ]


def get_results(total_votes, results, winner):
    results = "\n".join(results)
    output = f"""Election Results
                 -------------------------
                 Total Votes: {total_votes}
                 -------------------------
                 {results}
                 -------------------------
                 Winner: {winner}
                 -------------------------"""

    return "\n".join([ ln.strip() for ln in output.split("\n") ])


def votes_by_candidate(data, candidate):
    return len([row.get("BallotId") for row in data if row.get("Candidate") == candidate ])


def main():
    data = read_csv(fpath[0])
    total_votes = len(data)

    win = 0
    results = []
    for candidate in get_candidates(data):
        votes = votes_by_candidate(data, candidate)
        
        # who is he winner?
        if votes > win:
            winner = candidate
            win = votes
        elif votes == win:
            winner = f"TIE: {winner} and  {candidate}"
                        
        percentage = round(float(votes) / total_votes * 100, 3)
        results.append(f"{candidate}: {calculate_percentage(votes, total_votes)}% ({votes})")
        output = get_results(total_votes, results, winner)
        print(output)


if __name__ == "__main__":
    main()
