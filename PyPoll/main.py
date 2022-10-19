from csv import DictReader

fpath = ( "/workspace/gitpod/PyPoll/Resources/election_data.csv",
          "/workspace/gitpod/PyPoll/analysis/pypoll_analysis.txt"
        )


def calculate_percentage(numerator, denominator, precision=3):
    """
    Convert 2 integers to a percentage.

    :param numerator: integer
    :param denominator: integer
    :param precision: integer specifying the number of decimal places; default=3
    :raises: ValueError, TypeError, ZeroDivisionError
    :returns: percentage to as many as 3 decimal places
    :return type: float
    """
    try:
        return round(float(numerator) / denominator * 100, precision)

    except (ValueError, TypeError, ZeroDivisionError):
        raise


def get_candidates(data):
    """
    Generate a list of candidates found in the data.

   :param data: list, data ingested from csv file.
   :raises: None
   :returns: list of candidates identified
   :return type: set
    """
    candidates = [ row.get("Candidate") for row in data ]

    # set removes duplicates
    return set(candidates)


# number of votes in the input
def number_of_votes(data):
    return len(data)


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

             
def save_analysis(fpath, output):
    with open(fpath, "w") as fh:
        fh.write(output)


def votes_by_candidate(data, candidate):
    return len([row.get("BallotId") for row in data if row.get("Candidate") == candidate ])


def main():
    data = read_csv(fpath[0])
    total_votes = number_of_votes(data)

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
    save_analysis(fpath[1], output)


if __name__ == "__main__":
    main()
