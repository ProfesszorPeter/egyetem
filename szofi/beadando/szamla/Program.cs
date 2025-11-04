using Newtonsoft.Json;
namespace beadando
{
    class Program
    {
        class Szamla
        {
            public int vevokod;
            public int termekkod;
            public int egysegar;
            public int darab;

            public Szamla(int vevokod, int termekkod, int egysegar, int darab)
            {
                this.vevokod = vevokod;
                this.termekkod = termekkod;
                this.egysegar = egysegar;
                this.darab = darab;
            }

            public int Szamit()
            {
                return egysegar * darab;
            }

            public override string ToString()
            {
                return $"vevokod : {vevokod}, termekkod: {termekkod}, egysegar: {egysegar}, darab: {darab}";
            }
        }
        static void Main(string[] args)
        {
            List<Szamla> szamlak = new List<Szamla>();
            Szamla szamla = new Szamla(12345,12,1325,10);

            Console.WriteLine(szamla.ToString());

            StreamReader file = new StreamReader("adatok.txt");

            while (!file.EndOfStream)
            {
                string sor = file.ReadLine();
                string[] szamok = sor.Split();
                szamlak.Add(new Szamla(Convert.ToInt32(szamok[0]), Convert.ToInt32(szamok[1]), Convert.ToInt32(szamok[2]), Convert.ToInt32(szamok[3])));
            }

            foreach(var elem in szamlak)
            {
                Console.WriteLine(elem.ToString());
            }

            StreamWriter ki = new StreamWriter("json_adatok.txt");

            string jsonstring = JsonConvert.SerializeObject(szamlak, Formatting.Indented);

            Console.WriteLine(jsonstring);

            ki.WriteLine(jsonstring);
        }
    }
}

