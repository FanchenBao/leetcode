#! /usr/bin/env python3
# from typing import *

"""08/13/2019

Very easy problem. Just need to make sure the computation of all leap years is
correct.
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        leap_years = {
            year
            for year in range(1900, 2020)
            if (year % 400 == 0) or (year % 4 == 0 and year % 100)
        }
        days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        if year in leap_years:
            days_of_month[2] = 29
        return sum(days_of_month[1:month]) + day


sol = Solution()
print(sol.dayOfYear("2004-03-01"))
