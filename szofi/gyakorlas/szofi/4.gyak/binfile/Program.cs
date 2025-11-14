namespace binfile
{
    internal class Program
    {
        static void Main(string[] args)
        {
            BinaryWriter bw = new BinaryWriter(File.Create("file.bin"));
            for (int i = 0; i < 100; i++)
            {
                bw.Write(i);
            }
            bw.Flush();
            bw.Close();

            BinaryReader br = new BinaryReader(File.Open("file.bin", FileMode.Open));

            while (br.PeekChar() != 1)
            {
                Console.WriteLine(br.ReadInt32());
            }
            br.Close();
        }
    }
}

