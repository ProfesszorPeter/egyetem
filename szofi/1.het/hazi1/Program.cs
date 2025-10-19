namespace hazi
{
    class Pont
    {
        public double X {get;set;}
        public double Y {get;set;}

        public Pont(double x, double y)
        {
            X = x;
            Y = y;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            List<Pont> pontok = new List<Pont>
            {
                new Pont(3,1),
                new Pont(1,1),
                new Pont(1,9),
                new Pont(4,8),
            };
        }
    }
}

