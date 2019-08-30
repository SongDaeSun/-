class DailyBudget ():
    def __init__ (self, name, budget):
        self.name = name
        self.budget = budget

class ConsumeTag():
    def __init__ (self, name, price):
        self.name = name
        self.price = price

class GlobalSetting ():

    def __init__ (self):
        self.monthlyIncome = 500000
        self.emergencyMoney = 0   
        self.weeklyBudget = 100000 
        self.dailyBudgetList = list()

    def WriteGlobal (self):
        f = open("GlobalVariables.txt", 'w')
        self.monthlyIncome = input("월수입을 입력하세요: ")
        f.write("monthlyIncome: " + str(self.monthlyIncome)+"\n")
        self.emergencyMoney = input("보유 비상금을 입력하세요: ")
        f.write("emergencyMoney: "+ str(self.emergencyMoney)+"\n")
        self.weeklyBudget = input ("주간 예산을 입력하세요: ")
        f.write("weeklyBudget: "+str(self.weeklyBudget)+"\n")
        f.close()

    def ReadGlobal (self):
        f = open ("GlobalVariables.txt", 'r')
        substring = f.readline()
        self.monthlyIncome = int (substring[16:])
        print(self.monthlyIncome)

        substring = f.readline()
        self.emergencyMoney = int (substring[16:])
        print(self.emergencyMoney)

        substring = f.readline()
        self.weeklyBudget = int (substring[14:])
        print(self.weeklyBudget)

        f.close()

    def WriteDailyBudget (self, name, price):
        f = open("DailyBudgets.txt", 'a')
        f.write(str(name)+ "#" + str(price)+"\n")
        f.close()

    def UpdateDailyBudget (self):
        self.dailyBudgetList = list()
        f = open("DailyBudgets.txt", 'r')

        while True:
            substringLine = f.readline()
            if not substringLine: break
            
            substring = substringLine.split('#')
            self.dailyBudgetList.append(DailyBudget(substring[0], int(substring[1])))

        f.close()

    def ReadDailyBudget (self):
        for dailyBudget in self.dailyBudgetList:
            print(dailyBudget.name + str(dailyBudget.budget))

"""
test = GlobalSetting ()

test.WriteGlobal()
test.ReadGlobal()

test.WriteDailyBudget ("실험", "2000")
test.UpdateDailyBudget ()
test.ReadDailyBudget ()
"""