namespace json
{
    class Auto
    {
        public string marka;
        public string rendszam;
        public byte ajtok;
        public bool muszaki_erv;
        public List<string> szinek;

        public Auto(string m, string r, byte a, bool m_e, List<string> l)
        {
            marka = m;
            rendszam = r;
            ajtok = a;
            muszaki_erv = m_e;
            szinek = l;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Auto auto = new Auto("Audi", "ABC-123", 5, true, new List<string>() { "kék", "fehér" });

            string json
        }
    }
}

