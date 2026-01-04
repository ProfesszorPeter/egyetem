namespace probadb
{

    internal class Tanulo
    {
        public int TanuloID { get; set; }
        public string VezNev { get; set; }
        public string KerNev { get; set; }
        public DateTime Szulido { get; set; }
        public string Hobbi { get; set; }
        public int Magassag { get; set; }
        public Osztaly Osztaly { get; set; }
    }

    internal class Osztaly
    {
        public Osztaly()
        {
            Tanulok = new List<Tanulo>();
        }

        public int osztalyID { get; set; }
        public string OsztalyNev { get; set; }
        public string OsztalyFonok { get; set; }
        public byte Teremszam { get; set; }
        public IList<Tanulo> Tanulok { get; set; }
    }

    internal class IskolaContext : DbContext
    {
        public DbSet<Tanulo> Tanulok { get; set; }
        public DbSet<Osztaly> Osztalyok { get; set; }
        protected override void Onconfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer("Server=(localdb)\\msmysqllocaldb;");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            using (var context = new IskolaContext())
            {
                var oszt = new Osztaly
                {
                    OsztalyNev = "12.A",
                    OsztalyFonok = "Menet Elek",
                    Teremszam = 12
                };
                conttext.Osztalyok.Add(oszt);
                var tan = new Tanulo()
                {
                    VezNev = "Könyök",
                    KerNev="Ödön",
                    Szulido=new DateTime(2005,12,10),
                    Hobbi = "Biciklizés",
                    Magassag = 184,
                    Osztaly = oszt
                }
                context.Tanulo.Add(tan);
                context.SaveChanges();
                var stud = context.Tanulok.Where(s=>s.KerNev"Ödön").Select(s=> new {
                        Tanulo = s,
                        Osztaly = s.Osztaly,
                        Ofo = s.Osztaly.OsztalyFonok
                        }).FirstOrDefault();
                Console.WriteLine(stud.Ofo);
            }
        }
    }
}

