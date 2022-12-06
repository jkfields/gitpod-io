from pandas.tseries.holiday import get_calendar, HolidayCalendarFactory, GoodFriday
from datetime import date

cal = get_calendar("USFederalHolidayCalendar")
print(cal)
print(type(GoodFriday()))
