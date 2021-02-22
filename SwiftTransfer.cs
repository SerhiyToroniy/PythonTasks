using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using System.Globalization;


namespace Task1
{
    [Serializable]
    public class SwiftTransfer
    {
        public int id { get; set; }
        public double amount { get; set; }
        public double fee_amount { get; set; }
        public Currency currency { get; set; }
        public string iban { get; set; }
        public string holder { get; set; }
        public DateTime date { get; set; }

        public SwiftTransfer(int i, double a, double f, string c, string iban, string h, string d)
        {
            id = i;
            amount = a;
            fee_amount = f;
            currency = (Currency)Enum.Parse(typeof(Currency), c);
            this.iban = iban;
            holder = h;
            DateTime _date;
            DateTime.TryParseExact(d, "yyyy.MM.dd", null, DateTimeStyles.None, out _date);
            date = _date;
        }
        public SwiftTransfer(SwiftTransfer x)
        {
            this.id = x.id;
            this.amount = x.amount;
            this.currency = x.currency;
            this.date = x.date;
            this.iban = x.iban;
            this.fee_amount = x.fee_amount;
            this.holder = x.holder;
        }
        public SwiftTransfer()
        {
            this.id = 0;
            this.amount = 0.0;
            this.currency = new Currency();
            this.date = new DateTime();
            this.iban = "";
            this.fee_amount = 0.0;
            this.holder = "";
        }

        public override string ToString()
        {
            string result = "\n";
            FieldInfo[] myField = this.GetType().GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
            PropertyInfo[] props = this.GetType().GetProperties(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
            for (int i = 0; i < myField.Length; i++)
            {
                if (props[i].Name.Contains("date"))
                {
                    result += $"{props[i].Name}: {Convert.ToString(myField[i].GetValue(this)).Remove(10)}\n";
                    continue;
                }
                result += $"{props[i].Name}: {myField[i].GetValue(this)}\n";
            }
            return result;
        }
    }
}
