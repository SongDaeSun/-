using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HouseKeepingBook
{
    [Serializable()]
    class DailyBudget
    {
        public string name;
        public int budget;

        public DailyBudget(string inputName, int inputBudget)
        {
            name = inputName;
            budget = inputBudget;
        }

    }


    class ConSumeTage
    {
        public string name;
        public int price;

        public ConSumeTage (string inputName, int inputPrice)
        {
            name = inputName;
            price = inputPrice;
        }
    }

    [Serializable()]
    class GlobalSettings
    {
        public int monthlyIncome = 500000;
        public int emergencyMoney = 0;
        public int weeklyBudget = 100000;
        public List<DailyBudget> dailyBudgetList = new List<DailyBudget>();

        public void AddDailyBudgetList(string name, int budget)
        {
            DailyBudget db = new DailyBudget(name, budget);
            dailyBudgetList.Add(db);
        }

    }
}
