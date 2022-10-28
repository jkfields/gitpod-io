from csv import DictReader
from datetime import date, datetime, timedelta
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas import read_csv, bdate_range
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday


class TimeOffCalendar(AbstractHolidayCalendar):
    """
    Custom calendar for Paid Time Off
    """
    def __ini__(self):
        self.rules = [
         Holiday("Paid Time Off", year=2022, month=11, day=18),
         Holiday("Paid Time Off", year=2022, month=11, day=22),
         Holiday("Paid Time Off", year=2022, month=11, day=23),
         Holiday("Floating Holiday", year=2022, month=11, day=25),
         Holiday("Paid Time Off", year=2022, month=12, day=2),
         Holiday("Paid Time Off", year=2022, month=12, day=9),
         Holiday("Paid Time Off", year=2022, month=12, day=16),
         Holiday("Paid Time Off", year=2022, month=12, day=20),
         Holiday("Paid Time Off", year=2022, month=12, day=21),
         Holiday("Paid Time Off", year=2022, month=12, day=22),
         Holiday("Paid Time Off", year=2022, month=12, day=23),
         Holiday("Paid Time Off", year=2022, month=12, day=27),
         Holiday("Paid Time Off", year=2022, month=12, day=28),
         Holiday("Paid Time Off", year=2022, month=12, day=29),
         Holiday("Paid Time Off", year=2022, month=12, day=30),
         Holiday("Paid Time Off", year=2023, month=3, day=6),
         Holiday("Terminal Leave", year=2023, month=3, day=13),
         Holiday("Terminal Leave", year=2023, month=3, day=14),
         Holiday("Terminal Leave", year=2023, month=3, day=15),
         Holiday("Terminal Leave", year=2023, month=3, day=16),
         Holiday("Terminal Leave", year=2023, month=3, day=17),
         Holiday("Terminal Leave", year=2023, month=3, day=20),
         Holiday("Terminal Leave", year=2023, month=3, day=21),
         Holiday("Terminal Leave", year=2023, month=3, day=22),
         Holiday("Terminal Leave", year=2023, month=3, day=23),
         Holiday("Terminal Leave", year=2023, month=3, day=24),
     ]


def get_holidays(start, end):
   return USFederalHolidayCalendar().holidays(start=start.strftime("%Y-%m-%d"),
                                              end=end.strftime("%Y-%m-%d")).tolist()


def get_timeoff(fname):
    try:
        return read_csv(fname, header=0, index_col=0)
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
    business_days = CustomBusinessDay(calendar=USFederalHolidayCalendar() and TimeOffCalendar())
    return bdate_range(start, end, freq=business_days)

    # days = (start + timedelta(x + 1) for x in range((end - start).days))
    # return [ day.strftime("%Y-%m-%d") for day in days if day.weekday() < 5 ]


def try_two():
    start = date.today()
    end = date(2023, 3, 2)

    for day in get_timeoff("./paid-timeoff.csv"):
        print(day)

def try_one():
    # datetime for current
    now = date.today()

    # datetime for retirement date
    # retire = get_date()
    retire = date(2023, 3, 24)

    print(now, retire)
    time_off = get_timeoff("./paid-timeoff.csv")
    #print(time_off)
    #print(time_off.index)

    # holidays = get_holidays(now, retire)
    # work_days = bdate_range(now, retire)
    # actual = [ day for day in work_days if day not in time_off or day not in holidays ]
    actual = list_of_days(now, retire)
    num_days = len(actual)
    for day in actual:
        print(day.strftime("%Y-%m-%d"))

    print(f"Days remaining is {num_days}!")        
    #for day in list_of_days(now, retire):
    #    print(day)
    #print(f"{number_of_business_days(now, retire)} remaining!")

    pto = TimeOffCalendar().holidays()
    print(pto)


def main():
    try_two()


if __name__ == "__main__":
    main()