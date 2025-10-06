namespace delagate
{
    class Proba{
        public static int Negyzet(int szam)
        { return szam*szam; }

        public int Ketszeres (int szam)
        { return 2*szam; }

        public int Haromszoros(int szam)
        {
            Console.WriteLine("Haromszoros");
            return 3*szam;
        }

        public void Egyszeres(int szam)
        { Console.WriteLine(szam); }

        public void Kettoszoros(int szam)
        {Console.WriteLine(2*szam);}
    }
    class Program
        {
            delagate int Muvelet(int s);

            delagate void Meghiv(int k);

            static void Main()
            {
                Muvelet f = Proba.Negyzet;
                Console.WriteLine(f(5));

                Proba p = new Proba();
                Muvelet g = p.Ketszeres;

                g+= p.Haromszoros;


                Console.WriteLine(g(5));
            }

        }
    
}

