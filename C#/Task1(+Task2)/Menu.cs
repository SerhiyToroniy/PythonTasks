using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Task1
{
    class Menu
    {
        public static void ShowMenu()
        {
            Console.Write("\nPlease, choose an option below:\n1 - search\n2 - sort\n3 - add\n4 - delete\n5 - edit\n6 - print\n7 - exit\nYour choise: ");
        }
        public static void DoMenuOption<T>(string choice, ref Collection<T> container, string PathToFile)
        {
            while (!Validation.IsNumber(choice))
            {
                Console.Write("Input number: ");
                choice = Console.ReadLine();
            }
            switch (Convert.ToInt32(choice))
            {
                case 1:
                    if (container.Length() == 0)
                    {
                        Console.WriteLine("Collection is empty!");
                        break;
                    }
                    Console.Write("Search: ");
                    container.Search(Console.ReadLine());
                    break;
                case 2:
                    if (container.Length() == 0)
                    {
                        Console.WriteLine("Collection is empty!");
                        break;
                    }
                    Console.Write("Sort: ");
                    container.Sort(Console.ReadLine());
                    FileManager.ClearFile(PathToFile);
                    FileManager.WriteToFile(PathToFile, container);
                    break;
                case 3:
                    container.CreateAndAdd();
                    FileManager.ClearFile(PathToFile);
                    FileManager.WriteToFile(PathToFile, container);
                    break;
                case 4:
                    if (container.Length() == 0)
                    {
                        Console.WriteLine("Collection is empty!");
                        break;
                    }
                    Console.Write("Id: ");
                    container.Delete(Console.ReadLine());
                    FileManager.ClearFile(PathToFile);
                    FileManager.WriteToFile(PathToFile, container);
                    break;
                case 5:
                    if (container.Length() == 0)
                    {
                        Console.WriteLine("Collection is empty!");
                        break;
                    }
                    Console.Write("Id: ");
                    container.Edit(Console.ReadLine());
                    FileManager.ClearFile(PathToFile);
                    FileManager.WriteToFile(PathToFile, container);
                    break;
                case 6:
                    Console.WriteLine(container);
                    break;
                case 7:
                    Environment.Exit(0);
                    break;
                default:
                    Console.Write("Make sure, your choice is in the 1-6 range and try again!");
                    break;
            }
        }
    }
}
