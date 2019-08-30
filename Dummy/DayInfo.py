import copy
import calendar
from GlobalSettings import DailyBudget, ConsumeTag

class DayInfo():
    def __init__(self, year, month, day, affiliatedWeek = None):
        self.year = year
        self.month = month
        self.day = day
        self.affiliatedWeek = affiliatedWeek

        self.budget = None
        self.isUnderLimitation = True
        self.consumeList = list()
        self.totalConsumePrice = 0
        self.budgetLimitation = 0

        self.currentBudget = self.budgetLimitation - self.totalConsumePrice

    def weekday(self):
        return calendar.weekday(self.year, self.month, self.day)

    def SetBudget (self, budget):
        self.budget = budget
        #print(budget.budget)
        self.budgetLimitation = self.budget.budget
        self.affiliatedWeek.budget - self.budget.budget

    def AddConsume (self, name, price):
        self.consumeList.append(ConsumeTag(name, price))
        self.totalConsumePrice += price
        self.currentBudget = self.budgetLimitation - self.totalConsumePrice
        if self.currentBudget < 0:
            self.isUnderLimitation = False

"""
testBudget = DailyBudget("테스트", 20000)
testDayInfo = DayInfo(2019, 8, 21)
testDayInfo.SetBudget(testBudget)
testDayInfo.AddConsume("쇼핑", 2000)
print(testDayInfo.totalConsumePrice)
"""