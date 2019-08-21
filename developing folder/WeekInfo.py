import DayInfo

class WeekInfo ():
    def __init__ (self, year, month, startingDay):
        self.year = year
        self.month = month
        self.days = list()

        for i in range(0,7):
            self.days.append(DayInfo.DayInfo(self.year, self.month, startingDay))
            startingDay += 1

"""
test = WeekInfo(2019, 8, 4)

for i in range(0,7):
    print(test.days[i].weekday())
"""