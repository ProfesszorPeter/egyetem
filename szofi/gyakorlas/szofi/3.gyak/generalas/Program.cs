namespace Filekezeles
{
    class Program
    {
        static void Main(string[] arg)
        {
            StreamWriter ki = new StreamWriter("/home/dev/mnt/szofi/3.gyak/allomany/generaltszamok.txt");
            Random ran = new Random();
            for (int i = 1; i < 101; i++)
            {
                ki.WriteLine($"{i} {ran.Next(0,1000)}");
            }
            ki.Close();
        }
    }
}

