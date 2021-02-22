using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Reflection;
using System.Globalization;
using Newtonsoft.Json;


namespace Task1
{
    class FileManager
    {
        public static void ReadFromFile<T>(string PathToFile, ref Collection<T> container)
        {
            string[] lines = File.ReadAllLines(PathToFile);
            for (int i = 0; i < lines.Length; i++)
            {
                if (Validation.IsValidObject<T>(lines[i]))
                {
                    container.Add(JsonConvert.DeserializeObject<T>(lines[i]));
                }
            }
        }

        public static void WriteToFile<T>(string PathToFile, in Collection<T> container)
        {
            string[] lines = new string[container.Length()];
            for (int i = 0; i < lines.Length; i++)
            {
                lines[i] = JsonConvert.SerializeObject(container[i]);
            }
            File.AppendAllLines(PathToFile, lines);
        }

        public static void ClearFile(string PathToFile)
        {
            File.WriteAllText(PathToFile, string.Empty);
        }
    }
}
