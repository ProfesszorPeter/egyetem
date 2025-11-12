namespace gyak_delegate
{
    delegate void UdvKozles(string nev);
    class Program
    {
        static void KoszontMagyar(string nev)
        {
            Console.WriteLine($"Szia {nev} !");
        }

        static void KoszontAngol(string nev)
        {
            Console.WriteLine($"Hello {nev} !");
        }

        static void UdvKozlesHivas(UdvKozles udv, string nev)
        {
            udv(nev);
        }

        static void Main()
        {
            UdvKozles udv = KoszontMagyar;
            udv("Anna");

            udv = KoszontAngol;
            udv("John");

            UdvKozlesHivas(KoszontMagyar, "Sára");
            UdvKozlesHivas(KoszontAngol, "Tom");


        }
    }
    
}

