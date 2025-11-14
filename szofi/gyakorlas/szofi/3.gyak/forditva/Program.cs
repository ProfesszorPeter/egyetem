namespace Filekezeles
{
    class Program
    {
        static void Main(string[] arg)
        {
            List<string> sorok = new List<string>();
            List<string> forditottszamok = new List<string>();

            StreamReader be = new StreamReader("/home/dev/mnt/szofi/3.gyak/allomany/szamok.txt");
            StreamWriter ki = new StreamWriter("/home/dev/mnt/szofi/3.gyak/allomany/forditva.txt");
            {
                while (!be.EndOfStream)
                {
                    string sor = be.ReadLine();
                    List<string> szamok = sor.Split(" ").ToList();
                    forditottszamok.Add(szamok.Reverse());
                }
            }
        }
    }
}

