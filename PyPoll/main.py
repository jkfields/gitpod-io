from csv import DictReader

fpath = ( "/workspace/gitpod/PyPoll/Resources/election_data.csv",
          "/workspace/gitpod/PyPoll/analysis/pypoll_analysis.txt"
        )


def calculate_percentage(numerator, denominator, precision=3):
    """
    Calculate the percentage from 2 integers.

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
    
    :param data: list representing the data ingested from csv file.
    :raises: None
    :returns: list of candidates identified
    :return type: set
    """
    candidates = [ row.get("Candidate") for row in data ]

    # set removes duplicates
    return set(candidates)


# number of votes in the input
def number_of_votes(data):
    """
    Calculate the  number of votes case in the election.

    :param data: list representing the data ingested from csv file.
    :raises: None
    :returns: total number of votes 
    :return type: set
    """
    return len(data)


def read_csv(fpath):
    """
    Ingest the data from the specific csv file.

    :param: fpath, str representing the path to the  csv file.
    :raises: IOError, OSError
    :returns: list of dict representing the rows in the file 
    :return type: list
    """    
    try:
        with open(fpath, "r") as fh:
            data = DictReader(fh)
            return [ ln for ln in data ]

    except (IOError, OSError):
        raise


def get_results(total_votes, results, winner):
    """
    Generate the analysis of the data.

    :param: total_vote integer
    :raises: None
    :returns :detailed analysis of the data 
    :return type: str
    """
    results = "\n".join(results)
    output = f"""
        Election Results
        -------------------------
        Total Votes: {total_votes}
        -------------------------
        {results}
        -------------------------
        Winner: {winner}
        -------------------------
        """

    #return "\n".join([ ln.strip() for ln in output.split("\n") ])
    return output
             
def save_analysis(fpath, output):
    """
    Save the analysis gerated from the data to file.

    :param: fpath, str representing the path to save.
    :param: output, multi-line str representing the analysis
    :raises: IOerror, OSError
    :returns: boolean representing succes or failure; false  
    :return type: str
    """
    try:
        with open(fpath, "w") as fh:
            fh.write(output)

    except (IOError, OSError):
        raise

    else:
        return True


def votes_by_candidate(data, candidate):
    """
    Calculate the number of votes for the specified candidate.

    :param: data, list representing the data ingested from csv file.
    :param: candidate, string representing the candidate's name
    :raises: None
    :returns: detailed analysis of the data 
    :return type: str
    """
    return len([ row.get("BallotId") for row in data if row.get("Candidate") == candidate ])


def main():
    """
    drive the action
    """
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
