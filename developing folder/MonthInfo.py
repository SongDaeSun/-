import copy
import calendar

class Time ():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def weekday(self):
        return calendar.weekday(self.year, self.month, self.day)

class MonthInfo():
    def __init__ (self,year,month):
        self.primeTime = Time(year, month, 1)
        self.startingDays = list()
        currentDay = copy.deepcopy(self.primeTime)

        while currentDay.weekday() != 6:
            currentDay.day += 1
        
        while currentDay.day <= calendar.monthrange(year, month)[1]:
            print(currentDay.day)
            self.startingDays.append(copy.deepcopy(currentDay))
            currentDay.day+=7

test = MonthInfo(2019, 8)