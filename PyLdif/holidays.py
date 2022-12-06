from pandas.tseries.holiday import get_calendar, Holiday, AbstractHolidayCalendar, HolidayCalendarFactory, GoodFriday
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas import read_csv, bdate_range
from datetime import date

def get_timeoff():
    days = [ Holiday("Paid Time Off", year=2022, month=12, day=9),
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
    return days


def main():
    cal = get_calendar("USFederalHolidayCalendar")
  
    print(get_timeoff())


if __name__ == "__main__":
    main()
