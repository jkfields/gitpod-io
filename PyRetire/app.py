from datetime import date, datetime, timedelta
from pandas.tseries.holiday import USFederalHolidayCalendar

key = "e688e99b-4a2c-4474-b4ba-9aa02ff50dfe"
url = "https://holidayapi.com/v1/holidays?pretty&key=e688e99b-4a2c-4474-b4ba-9aa02ff50dfe&country=US&year=2021"

holidays = [ date(2022, 10, 10),
             date(2022, 11, 11),
             date(2022, 11, 24),
             date(2022, 11, 25),
             date(2022, 12, 26),
             date(2023, 1, 2),
             date(2023, 1, 16),
             date(2023, 2, 20),
           ]
time_off = [ date(2022, 9, 21),
             date(2022, 9, 22),
             date(2022, 9, 23),
             date(2022, 9, 26),
             date(2022, 11, 21),
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

def get_date():
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
    return [ day.strftime("%Y-%m-%d")
             for day in days
               if day.weekday() < 5 and
                  day not in holidays and
                  day not in time_off
            ]


def main():
    # datetime for current
    now = date.today()

    # datetime for retirement date
    retire = get_date()
    #retire = date(2023, 3, 28)

    print(now, retire)
    print(type(now), type(retire))

    holidays = USFederalHolidayCalendar().holidays(start=now.strftime("%Y-%m-%d"),
                                                   end=retire.strftime("%Y-%m-%d")).tolist()
    print(holidays)
    #for day in list_of_days(now, retire):
    #    print(day)
    #print(f"{number_of_business_days(now, retire)} remaining!")

if __name__ == "__main__":
    main()