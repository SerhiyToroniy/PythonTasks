using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Reflection;


namespace Task1
{
    class Program
    {
        static void Main(string[] args)
        {
            Collection<SwiftTransfer> arr = new Collection<SwiftTransfer>();
            Console.Write("FileName: ");
            var path = Console.ReadLine();
            while (!Validation.CheckPath(Path.Combine(Directory.GetParent(Environment.CurrentDirectory).Parent.FullName, path)))
            {
                Console.Write("FileName: ");
                path = Console.ReadLine();
            }
            path = Path.Combine(Directory.GetParent(Environment.CurrentDirectory).Parent.FullName, path);
            FileManager.ReadFromFile(path, ref arr);
            Menu.ShowMenu();
            string choice = Console.ReadLine();
            while (true)
            {
                Menu.DoMenuOption(choice, ref arr, path);
                Console.Write("Select menu option: ");
                choice = Console.ReadLine();
            }
        }
    }
}
