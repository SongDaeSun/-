import copy
import calendar
import WeekInfo
import DayInfo    

class MonthInfo():
    def __init__ (self,year,month):
        self.startingDay = DayInfo.DayInfo(year, month, 1)
        self.weeks = list()
        currentDay = copy.deepcopy(self.startingDay)

        while currentDay.weekday() != 6:
            currentDay.day += 1
        
        #i=0
        while currentDay.day <= calendar.monthrange(year, month)[1]:
            self.weeks.append(WeekInfo.WeekInfo(currentDay.year, currentDay.month, currentDay.day))
            #print(self.weeks[i].days[3].day) 
            #i+=1
            currentDay.day+=7

#test = MonthInfo(2019, 8)