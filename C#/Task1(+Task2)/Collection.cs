using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using System.Globalization;
using Newtonsoft.Json;

namespace Task1
{
    class Collection<T>
    {
        private List<T> data { get; set; }

        public Collection()
        {
            data = new List<T>();
        }
        public int Length()
        {
            return this.data.Count;
        }
        public T this[int key]
        {
            get => data[key];
            set => data[key] = value;
        }
        public void Add(T obj)
        {
            data.Add(obj);
        }
        public void CreateAndAdd()
        {
            int size = data.Count;
            string json_obj = "{";
            PropertyInfo[] props = typeof(T).GetProperties();
            for (int i = 0; i < props.Length; i++)
            {
                Console.Write($"{props[i].Name}:");
                if (props[i].PropertyType == typeof(int) || props[i].PropertyType == typeof(double))
                    json_obj += $"'{props[i].Name}':{Console.ReadLine()},";
                else
                    json_obj += $"'{props[i].Name}':'{Console.ReadLine()}',";
            }
            json_obj = json_obj.Remove(json_obj.Length - 1);
            json_obj += "}";
            if (Validation.IsValidObject<T>(json_obj))
                data.Add(JsonConvert.DeserializeObject<T>(json_obj));
            if (data.Count > size)
                Console.WriteLine("Successfully added!");
        }

        public override string ToString()
        {
            Console.WriteLine("\nCollection:");
            string _data = "";
            for (int i = 0; i < data.Count; i++)
            {
                _data += Convert.ToString(data[i]);
            }
            return _data;
        }

        public void Search(string value)
        {
            List<T> suitable = new List<T>();
            PropertyInfo[] props = typeof(T).GetProperties();
            for (int i = 0; i < data.Count; i++)
            {
                bool flag = false;
                for (int j = 0; j < props.Length; j++)
                {
                    if (Convert.ToString(props[j].GetValue(data[i])).ToLower().Contains(value.ToLower()))
                        flag = true;
                    if (flag)
                        break;
                }
                if (flag)
                    suitable.Add(data[i]);
            }
            if (suitable.Count != 0)
                foreach (var item in suitable)
                {
                    Console.WriteLine(item);
                }
            else
                Console.WriteLine($"No one item in collection contains {value}!");
        }

        public void Sort(string attr)
        {
            bool already_sorted = false;
            PropertyInfo[] props = typeof(T).GetProperties();
            for (int i = 0; i < props.Length; i++)
            {
                if (props[i].Name.ToLower().Contains(attr.ToLower()))
                {
                    data = data.OrderBy(d => props[i].GetValue(d, null)).ToList();
                    already_sorted = true;
                    break;
                }
            }
            if (already_sorted)
                Console.WriteLine("Successfully sorted!");
            else
                Console.WriteLine("Collection hasn't changed!");
        }

        public void Delete(string id)
        {
            PropertyInfo[] props = typeof(T).GetProperties();
            int size = data.Count;
            while (!Validation.IsNumber(id))
            {
                Console.Write("Input number: ");
                id = Console.ReadLine();
            }
            for (int i = 0; i < data.Count; i++)
            {
                for (int j = 0; j < props.Length; j++)
                {
                    if (props[j].Name.ToLower().Contains("id") && Convert.ChangeType(id, props[j].PropertyType).Equals(props[j].GetValue(data[i])))
                    {
                        data.RemoveAt(i);
                        break;
                    }
                }
            }
            if (data.Count < size)
                Console.WriteLine("Successfully deleted!");
            else
                Console.WriteLine("Collection hasn't changed!");
        }

        public void Edit(string id)
        {
            PropertyInfo[] props = typeof(T).GetProperties();
            while (!Validation.IsNumber(id))
            {
                Console.Write("Input number: ");
                id = Console.ReadLine();
            }
            for (int i = 0; i < data.Count; i++)
            {
                for (int k = 0; k < props.Length; k++)
                {
                    if (props[k].Name.ToLower().Contains("id") && Convert.ChangeType(id, props[k].PropertyType).Equals(props[k].GetValue(data[i])))
                    {
                        for (int j = 1; j < props.Length; j++)
                        {
                            try
                            {
                                Console.Write($"{props[j].Name}: ");
                                if (props[j].PropertyType.IsEnum)
                                    props[j].SetValue(data[i], Enum.Parse(props[j].PropertyType, Console.ReadLine()));
                                else
                                    props[j].SetValue(data[i], Convert.ChangeType(Console.ReadLine(), props[j].PropertyType));
                            }
                            catch (Exception)
                            {
                                Console.WriteLine($"Oops, {props[j].Name} isn't valid! Try edit item again..");
                                return;
                            }
                        }
                        Console.WriteLine("Successfully edited!");
                        break;
                    }
                }
            }
        }
    }
}
