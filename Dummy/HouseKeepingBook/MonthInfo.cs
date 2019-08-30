using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Globalization;

namespace HouseKeepingBook
{
    class MonthInfo
    {
        public int year, month, day;
        public DateTime dateTime;

        public MonthInfo(int inputYear, int inputMonth, int inputDay)
        {
            dateTime = new DateTime(inputYear, inputMonth, inputDay, new GregorianCalendar());
        }
    }
}
