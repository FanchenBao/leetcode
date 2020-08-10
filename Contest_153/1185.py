#! /usr/bin/env python3
from datetime import datetime

"""09/10/2019

Solution1:
This is a hack, using python's built-in datetime module. It cannot count as a
true solution, but I think it is okay to use in a real competition scenario.

This solution clocked in at 36ms, 69%


Solution2:
This is the real solution. It uses 1971-01-01 as the bench mark day, computes
the total number of days between the bench mark and the date of intereset, and
modulo 7 to find out what day of the week is the date of interest. The only
tricky part is the handling of leap years, and use the number of days in between
bench mark and date of interest (i.e. there is a minus 1 to num_day at the end)
to perform modulo.

This solution clocked in at 40 ms, 29%

"""


class Solution1:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime(year, month, day).strftime("%A")


class Solution2:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # bench mark day is 1971-01-01, which is a Friday
        days = [
            "Friday",
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
        ]
        months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_months = [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_years = set(
            y
            for y in range(1971, 2101)
            if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)
        )

        num_day = 0
        for y in range(1971, year):
            num_day += 366 if y in leap_years else 365
        for m in range(1, month):
            num_day += leap_months[m] if year in leap_years else months[m]
        num_day += day
        return days[(num_day - 1) % 7]


sol1 = Solution1()
sol2 = Solution2()
day = 1
month = 3
year = 1999
print(sol1.dayOfTheWeek(day, month, year))
print(sol2.dayOfTheWeek(day, month, year))
