using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Globalization;
using System.Reflection;
using Newtonsoft.Json;


namespace Task1
{
    class Validation
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
            if (value.Length > 10)
                value = value.Remove(10);
            if (!(DateTime.TryParseExact(value, "dd.MM.yyyy", null, DateTimeStyles.None, out temp) && (temp <= DateTime.Now.Date)))
                Console.WriteLine($"{value} must have dd.MM.yyyy format and <= today!");
            return DateTime.TryParseExact(value, "dd.MM.yyyy", null, DateTimeStyles.None, out temp) && (temp <= DateTime.Now.Date);
        }
        public static bool IsValidObject<T>(string json_obj)
        {
            bool result = true;
            try
            {
                T temp = JsonConvert.DeserializeObject<T>(json_obj);
                PropertyInfo[] props = typeof(T).GetProperties(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                for (int i = 0; i < props.Length; i++)
                {
                    if (!result)
                    {
                        Console.WriteLine($"{props[i - 1].GetValue(temp)} is invalid!");
                        return false;
                    }
                    if (props[i].PropertyType.IsEnum)
                        result = IsCurrency(props[i].GetValue(temp).ToString(), props[i].PropertyType);
                    if (props[i].PropertyType == typeof(int) || props[i].PropertyType == typeof(double))
                        result = IsNumber(props[i].GetValue(temp).ToString()) && true;
                    if (props[i].Name.ToLower().Contains("holder"))
                        result = IsHolder(props[i].GetValue(temp).ToString()) && true;
                    if (props[i].Name.ToLower().Contains("iban"))
                        result = IsIban(props[i].GetValue(temp).ToString()) && true;
                    if (props[i].Name.ToLower().Contains("date"))
                        result = IsDate(props[i].GetValue(temp).ToString()) && true;
                }
            }
            catch
            {
                Console.WriteLine($"Object below was skipped due to incorrect data!\n{json_obj}");
                Console.Write("\nMake sure:\n\tid: integer>0\n\tamount: num>0\n\tfee_amount: num>0\n\tcurency: eur,usd,uah\n\tiban: UA11 1111 1111 1111\n\tholder: Name Surname\n\tdate: yyyy.MM.dd( <= today)\n");
                result = false;
                return result;
            }
            return result;
        }
    }
}
