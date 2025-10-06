
using System;
using System.IO;
namespace Listazo //paraméterként szövegfájl; kivételkezeléses
{
    internal class Program
    {
        static void Main(string[] args)
        {
            try
            {
                if (args.Length == 0) throw new Exception("Paraméterként meg " +
                "kell adni egy fájlnevet!");
                else
                {
                    FileStream fs = new FileStream(args[0], FileMode.Open);
                    StreamReader sr = new StreamReader(fs);
                    Console.WriteLine();
                    try
                    {
                        string sor;
                        byte szamlalo = 0;
                        while ((sor = sr.ReadLine()) != null)
                        {
                            szamlalo++;
                            if (szamlalo % 2 == 0) Console.ForegroundColor = ConsoleColor.Green;
                            else Console.ForegroundColor = ConsoleColor.White;
                            Console.WriteLine(sor);
                            if (szamlalo == 20)
                            {
                                Console.ForegroundColor = ConsoleColor.Gray;
                                Console.WriteLine("\nA továbblapozáshoz nyomjon meg egy billentyűt!");
                                Console.ReadKey(true);
                                szamlalo = 0;
                            }//if
                        }//while
                    }//try
                    catch (Exception kiv)
                    {
                        Console.WriteLine("A beolvasás alatt hiba történt.\n{0}", kiv);
                    }
                    finally
                    {
                        sr.Close();
                        fs.Close();
                    }
                }//else
            }//try
            catch (FileNotFoundException)
            {
                Console.WriteLine("Nem található a fájl: {0}", args[0]);
            }
            catch (DirectoryNotFoundException)
            {
                Console.WriteLine("Nem található az alkönyvtár.");
            }
            catch (Exception kiv)
            {
                Console.WriteLine("Hiba történt! {0}", kiv.Message);
            }
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("\nNyomjon meg egy bill.-t!");
            Console.ReadKey(true);
        }//Main
    }
}

