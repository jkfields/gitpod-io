from pandas.tseries.holiday import get_calendar, HolidayCalendarFactory
from datetime import date

cal = get_calendar("USFederalHolidayCalendar")
print(cal)
