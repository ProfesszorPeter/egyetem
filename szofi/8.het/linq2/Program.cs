namespace LINQ_peldak2
{
    class Person
    {
        public int ID { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string PhoneNumber { get; set; }

        public Person(int id, string fn, string ln, string pn)
        {
            ID = id;
            FirstName = fn;
            LastName = ln;
            PhoneNumber = pn;
        }
    }
    internal class Program
    {
        static void Main()
        {
            List<Person> list = new List<Person>()
            {
                new Person(1,"Lajos","Kis","123-4567"),
                new Person(2,"Béla","Nagy","234-5678"),
                new Person(3,"Miklós","Szabó","345-6789"),
                new Person(4,"Gyula","Kovács","111-2222"),
                new Person(5,"Jenő","Cipész","222-3333"),
            };

            var result = from person in list where person.ID % 2 != 0 select new 
            {
                Name = person.FirstName + " " + person.LastName,
                PhoneNumber = person.PhoneNumber

            };

            foreach (var person in result)
            {
                Console.WriteLine($"név: {person.Name}, telefon: {person.PhoneNumber}");
                
            }

        }
    }
}
