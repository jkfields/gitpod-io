from csv import DictReader
from datetime import date, datetime, timedelta
from pandas.tseries.holiday import USFederalHolidayCalendar

time_off = [ date(2022, 11, 21),
             date(2022, 11, 22),
             date(2022, 11, 23),
             date(2022, 11, 28),
             date(2022, 12, 8),
             date(2022, 12, 15),
             date(2022, 12, 20),
             date(2022, 12, 21),
             date(2022, 12, 22),
             date(2022, 12, 23),
             date(2022, 12, 27),
             date(2022, 12, 28),
             date(2022, 12, 29),
             date(2022, 12, 30),
             date(2022, 12, 20),
             date(2023, 3, 15),
             date(2023, 3, 16),
             date(2023, 3, 17),
             date(2023, 3, 20),
             date(2023, 3, 21),
             date(2023, 3, 22),
             date(2023, 3, 23),
             date(2023, 3, 24),
             date(2023, 3, 27),
             date(2023, 3, 28),
           ]


def get_holidays(start, end):
   return USFederalHolidayCalendar().holidays(start=start.strftime("%Y-%m-%d"),
                                              end=end.strftime("%Y-%m-%d")).tolist()


def get_timeoff(fname):
    try:
        with open(fname, "r") as fh:
            reader = DictReader(fh)

            # grab the data
            return [ row for row in reader ]

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
    return [ day.strftime("%Y-%m-%d for day in days if day.weekday() < 5 ]

def main():
    # datetime for current
    now = date.today()

    # datetime for retirement date
    # retire = get_date()
    retire = date(2023, 3, 28)

    print(now, retire)
    time_off = get_timeoff("./paid-timeoff.csv")
    print(time_off)

    #for day in list_of_days(now, retire):
    #    print(day)
    #print(f"{number_of_business_days(now, retire)} remaining!")

if __name__ == "__main__":
    main()