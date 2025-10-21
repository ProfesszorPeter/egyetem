namespace beadando
{
    class Program
    {
        class Szamla
        {
            int _vevokod;
            int _termekkod;
            int _egysegar;
            int _darab;

            public Szamla(int vevokod, int termekkod, int egysegar, int darab)
            {
                vevokod = _vevokod;
                termekkod = _termekkod;
                egysegar = _egysegar;
                darab = _darab;
            }

            public int Szamit(int egysegar, int darab)
            {
                return egysegar * darab;
            }
        }
        static void Main(string[] args)
        {
        }
    }
}

