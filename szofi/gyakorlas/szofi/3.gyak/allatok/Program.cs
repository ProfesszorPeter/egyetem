namespace Filekezeles
{
    class Program
    {
        static void Main(string[] arg){
            FileStream fs = new FileStream("/home/dev/mnt/szofi/3.gyak/allomany/allatok.txt", FileMode.Open);
            StreamReader olvaso = new StreamReader(fs);

            while(!olvaso.EndOfStream)
            {
                Console.WriteLine(olvaso.ReadLine());
            }
        }
        
    }
    
}

