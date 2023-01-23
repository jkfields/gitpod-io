from csv import DictReader
from datetime import date, datetime, timedelta
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from pandas import read_csv, bdate_range
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday, USMartinLutherKingJr, USPresidentsDay, USMemorialDay, USLaborDay, USColumbusDay, USThanksgivingDay


class TimeOffCalendar(AbstractHolidayCalendar):
    """
    Custom calendar for Paid Time Off
    """
    def __init__(self):
        self.rules = [
            Holiday("New Years Day", month=1, day=1, observance=nearest_workday),
            USMartinLutherKingJr,
            USPresidentsDay,
            USMemorialDay,
            Holiday("July 4th", month=7, day=4, observance=nearest_workday),
            USLaborDay,
            USColumbusDay,
            Holiday("Veterans Day", month=11, day=11, observance=nearest_workday),
            USThanksgivingDay,
            Holiday("Christmas", month=12, day=25, observance=nearest_workday),
            Holiday("TimeOff1118", month=11, day=18, observence=nearest_workday),
            Holiday("TimeOff1122", month=11, day=22, observence=nearest_workday),
            Holiday("TimeOff1123", month=11, day=23, observence=nearest_workday),
            Holiday("FloatingHoliday2", month=11, day=25, observence=nearest_workday),
            Holiday("TimeOff1202", month=12, day=2, observence=nearest_workday),
            Holiday("TimeOff1209", month=12, day=9, observence=nearest_workday),
            Holiday("TimeOff1216", month=12, day=16, observence=nearest_workday),
            Holiday("TimeOff1220", month=12, day=20, observence=nearest_workday),
            Holiday("TimeOff1221", month=12, day=21, observence=nearest_workday),
            Holiday("TimeOff1222", month=12, day=22, observence=nearest_workday),
            Holiday("TimeOff1223", month=12, day=23, observence=nearest_workday),
            Holiday("TimeOff1227", month=12, day=27, observence=nearest_workday),
            Holiday("TimeOff1228", month=12, day=28, observence=nearest_workday),
            Holiday("TimeOff1229", month=12, day=29, observence=nearest_workday),
            Holiday("TimeOff1230", month=12, day=30, observence=nearest_workday),
            Holiday("TimeOff0306", month=3, day=6, observence=nearest_workday),
            Holiday("FloatingHoliday1", month=3, day=10, observence=nearest_workday),
            Holiday("TimeOff0313", month=3, day=13, observence=nearest_workday),
            Holiday("TimeOff0314", month=3, day=14, observence=nearest_workday),
            Holiday("TimeOff0315", month=3, day=15, observence=nearest_workday),
            Holiday("TimeOff0316", month=3, day=16, observence=nearest_workday),
            Holiday("TimeOff0317", month=3, day=17, observence=nearest_workday),
            Holiday("TimeOff0320", month=3, day=20, observence=nearest_workday),
            Holiday("TimeOff0321", month=3, day=21, observence=nearest_workday),
            Holiday("TimeOff0322", month=3, day=22, observence=nearest_workday),
            Holiday("TimeOff0323", month=3, day=23, observence=nearest_workday),
            Holiday("TimeOff0324", month=3, day=24, observence=nearest_workday),
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

    pto = get_timeoff("./paid-timeoff.csv")
    print(pto)
    print(type(pto))


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
    # datetime for current
    now = date.today()

    # datetime for retirement date
    # retire = get_date()
    retire = date(2023, 3, 24)

    print(now, retire)   
    work_days = list_of_days(now, retire)
    print(work_days)
    print(f"number of workdays remaining is {len(work_days)}!")
    

if __name__ == "__main__":
    main()