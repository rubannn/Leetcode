from datetime import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dt = datetime.date(year, month, day)
        return dt.strftime('%A')
