namespace events
{
    class Pelda
    {
        public delegate void EsemenykezeloDelegate(string szoveg);
        public event EsemenykezeloDelegate AllapotvaltozasEsemeny;
        int szam;

        public int Szam{
            get {return szam;}
            set { szam = value;
                Allapotvaltozas();
        }

    }

        private void Allapotvaltozas()
        {
            if (AllapotvaltozasEsemeny != null) {AllapotvaltozasEsemeny ("Megváétozott a dolog");}
        }

    class Program
    {
        static void Esemenykezelo (string szoveg)
        {
            Console.WriteLine(szoveg);
        }

        static void Main(string[] args)
        {
            Pelda p = new Pelda();
            p.AllapotvaltozasEsemeny += Esemenykezelo;
            p.szam = 12;
        }
        
    }
    
}
}

