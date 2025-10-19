namespace Filekezeles
{
    class Program
    {
        static void Main(string[] arg)
        {
            StreamReader be = new StreamReader("/home/dev/mnt/szofi/3.gyak/allomany/proba.txt");
            while(!be.EndOfStream)
            {
                be.ReadLine();
                Console.WriteLine(be.ReadLine());
            }
        }
        
    }
    
}

