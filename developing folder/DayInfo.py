import copy
import calendar

class DayInfo():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def weekday(self):
        return calendar.weekday(self.year, self.month, self.day)