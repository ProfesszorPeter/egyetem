namespace Filekezeles
{
    class Program
    {
        static void Main(string[] arg)
        {
            StreamReader olvaso = new StreamReader("/home/dev/mnt/szofi/3.gyak/allomany/allatok.txt");

            while(!olvaso.EndOfStream)
            {
                Console.WriteLine(olvaso.ReadLine());
            }
            olvaso.Close();

            StreamWriter iro = new StreamWriter("/home/dev/mnt/szofi/3.gyak/allomany/allatok.txt"); #második paraméternek bool -> hozzá fűz vagy felü ír
            iro.WriteLine("tigris");
            iro.Flush();
            iro.Close();
            Console.WriteLine("\nBetettük a tigrist a sor végére\n");

            StreamReader ki = new StreamReader("/home/dev/mnt/szofi/3.gyak/allomany/allatok.txt");

            while(!ki.EndOfStream)
            {
                Console.WriteLine(ki.ReadLine());
            }
        }
        
    }
    
}

