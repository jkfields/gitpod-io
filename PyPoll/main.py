import csv

fpath = ( "/workspace/gitpod/PyPoll/Resources/election_data.csv",
          "/workspace/gitpod/PyPoll/analysis/pypoll_analysis.txt"
        )


def main():
    with open(fpath[0], "r") as ifh:
        print(ifh.readlines()[-1])


if __name__ == "__main__":
    main()