using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Globalization;
using System.Reflection;
using Newtonsoft.Json;


namespace SwiftTransferAPI.Models
{
    public class Validation
    {
        public static bool CheckPath(string path)
        {
            if (!File.Exists(@path))
                Console.WriteLine("File doesn't exist!");
            return File.Exists(@path);
        }
        public static bool IsNumber(string value)
        {
            bool result = false;
            ulong num = 0;
            if (value.Contains(","))
                result = value.Count(c => c == ',') == 1 && ulong.TryParse(value.Replace(",", ""), out num);
            else
                result = ulong.TryParse(value, out num) && true;
            if (!result)
                Console.WriteLine($"{value} doesn't look like a number!");
            return result;
        }
        public static bool IsHolder(string value)
        {
            if (!value.Replace(" ", "").All(Char.IsLetter))
                Console.WriteLine($"{value} must consist only letters!");
            if (!(1 == value.Count(c => c == ' ')))
                Console.WriteLine($"Invalid SPACE count in {value}!");
            return value.Replace(" ", "").All(Char.IsLetter) && 1 == value.Count(c => c == ' ');
        }
        public static bool IsCurrency(string value, Type enumType)
        {
            if (value.ToLower() == "invalid")
                return false;
            return Enum.GetNames(enumType).Contains(value.ToLower());
        }
        public static bool IsIban(string value)
        {
            if (!(value.StartsWith("UA")))
                Console.WriteLine($"{value} must starts with UA!");
            if (!(3 == value.Count(c => c == ' ')))
                Console.WriteLine($"Invalid SPACE count in {value}!");
            return value.StartsWith("UA") && 3 == value.Count(c => c == ' ') && IsNumber(value.Replace(" ", "").Replace("UA", "")) && value.Length == 19;
        }
        public static bool IsDate(string value)
        {
            DateTime temp;
            bool result = DateTime.TryParseExact(value, "dd.MM.yyyy 0:00:00", CultureInfo.CreateSpecificCulture("en-US"), DateTimeStyles.None, out temp) && (temp <= DateTime.Now.Date);
            if (!(result))
                Console.WriteLine($"{value} must have dd.MM.yyyy format and <= today!");
            return result;
        }
        public static string IsValidObject<T>(T temp)
        {
            string mes = "";
            bool result = true;
            try
            {
                //T temp = JsonConvert.DeserializeObject<T>(json_obj);
                PropertyInfo[] props = typeof(T).GetProperties(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                for (int i = 0; i < props.Length; i++)
                {
                    if (props[i].Name.ToLower().Contains("currency"))
                        result = IsCurrency(props[i].GetValue(temp).ToString(), typeof(Currency));
                    if (props[i].PropertyType == typeof(int) || props[i].PropertyType == typeof(double))
                        result = IsNumber(props[i].GetValue(temp).ToString()) && true;
                    if (props[i].Name.ToLower().Contains("holder"))
                        result = IsHolder(props[i].GetValue(temp).ToString()) && true;
                    if (props[i].Name.ToLower().Contains("iban"))
                        result = IsIban(props[i].GetValue(temp).ToString()) && true;
                    if (props[i].Name.ToLower().Contains("date"))
                        result = IsDate(props[i].GetValue(temp).ToString()) && true;
                    if (!result)
                    {
                        mes += ($"{props[i].Name} is invalid!\n");
                    }
                }
            }
            catch
            {
                mes += ($"Object below was skipped due to incorrect data!\n{JsonConvert.SerializeObject(temp)}\n");
                Console.Write("\nMake sure:\n\tid: integer>0\n\tamount: num>0\n\tfee_amount: num>0\n\tcurency: eur,usd,uah\n\tiban: UA11 1111 1111 1111\n\tholder: Name Surname\n\tdate: yyyy.MM.dd( <= today)\n");
                //result = false;
                //return result;
                return mes;
            }
            return mes;
        }
    }
}