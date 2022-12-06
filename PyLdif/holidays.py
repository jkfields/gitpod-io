from pandas.tseries.holiday import get_calendar, HolidayCalendarFactory, GoodFriday
from datetime import date

def get_timeoff():
    holidays = [ Holiday(),
               ]


def main():
    cal = get_calendar("USFederalHolidayCalendar")
    print(cal)  
    print(type(GoodFriday()))


if __name__ == "__main__":
    main()
