namespace adatbazis
{
    class Program
    {
        public static void Main()
        {
            using (var db= new LiteDatabase("Szemely.db"))
            {
                var contacts = db.GetCollection<Contact>();
                var person = new Contact
                {
                    Name = "Teszt Elek",
                    Phone = "xxxxxxxxx",
                    Email = "xxxxxxxx@xxxxxx.xxx"
                };
                contacts.Inster(person);
            }
        }
    }
}
