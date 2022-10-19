from csv import DictReader

fpath = ( "/workspace/gitpod/PyPoll/Resources/election_data.csv",
          "/workspace/gitpod/PyPoll/analysis/pypoll_analysis.txt"
        )

def read_csv(fpath):
    with open(fpath, "r") as fh:
        data = DictReader(fh)
        return [ ln for ln in data ]

def main():
    data = read_csv(fpath[0])
    print(data[-1])


if __name__ == "__main__":
    main()
