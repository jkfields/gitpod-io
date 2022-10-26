from csv import DictReader
from datetime import date, datetime, timedelta
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas import read_csv, bdate_range


def get_holidays(start, end):
   return USFederalHolidayCalendar().holidays(start=start.strftime("%Y-%m-%d"),
                                              end=end.strftime("%Y-%m-%d")).tolist()


def get_timeoff(fname):
    try:
        return read_csv(fname, index_col=0)
        """
        with open(fname, "r") as fh:
            reader = DictReader(fh)

            # grab the data
            return [ row for row in reader ]
        """

    except (IOError, OSError):
        pass


def get_retirement_date():
    while True:
        dt = input("Retirement date (yyyy-mm-dd): ").strip()
        try:
            dt = datetime.strptime(dt, "%Y-%m-%d").date()

        except ValueError as ex:
            print(str(ex))

        else:
            return dt


def number_of_business_days(start, end):
    days = list_of_days(start, end)
    return len(days)


def list_of_days(start, end):
    days = (start + timedelta(x + 1) for x in range((end - start).days))
    return [ day.strftime("%Y-%m-%d") for day in days if day.weekday() < 5 ]


def main():
    # datetime for current
    now = date.today()

    # datetime for retirement date
    # retire = get_date()
    retire = date(2023, 3, 28)

    print(now, retire)
    time_off = get_timeoff("./paid-timeoff.csv")
    print(time_off)
    print(time_off.index)

    for day in bdate_range(now, retire)).tolist():
        print(day.strftime("%Y-%m-%d"))
        
    #for day in list_of_days(now, retire):
    #    print(day)
    #print(f"{number_of_business_days(now, retire)} remaining!")

if __name__ == "__main__":
    main()