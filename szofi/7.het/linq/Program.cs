//ebben a file-ban a tanár megoldásai vannak
namespace LINQ_peldak
{
    internal class Program
    {
        static void Main()
        {
            List<int> list = new List<int>()
            {
            1,-3,5,4,-2,-1,0,10,-10
            };
            Console.WriteLine("Kiválasztás:\n");
            //kiválasztás lekérdező kifejezés formátummal
            //(Query Expression Format): a számok négyzetei
            var result = from number in list
                         select number * number;
            foreach (var item in result)
            {
                Console.Write("{0} ", item);
            }
            NyomBill();
            //ugyanez a kiválasztás kiterjesztés metódussal
            //(Extension Format) és lambda kifejezéssel
            var result2 = list.Select(x => x * x);
            foreach (var item in result2)
            {
                Console.Write("{0} ", item);
            }
            NyomBill();
            //Func<int,int> selector=x=>x*x;
            //var result3=list.Select(selector);
            //különbözők kiválasztása
            Console.WriteLine("Kiválasztás: különbözők");
            var result3 = list.Select(x => x * x).Distinct();
            foreach (var item in result3)
            {
                Console.Write("{0} ", item);
            }
            NyomBill();
            //negatív számok szűrése
            Console.WriteLine("Szűrés: negatív számok\n");
            var result4 = from number in list
                          where number < 0
                          select number;
            foreach (var item in result4)
            {
                Console.Write("{0} ", item);
            }
            NyomBill();
            var result5 = list.Where(x => x < 0);
            foreach (var item in result5)
            {
                Console.Write("{0} ", item);
            }
            NyomBill();
            //páros indexű elemek szűrés
            Console.WriteLine("Szűrés: páros indexű elemek\n");
            var result6 = list.Where((number, index) => index % 2 == 0);
            foreach (var item in result6)
            {
                Console.Write("{0} ", item);
            }
            NyomBill();
            //Szűrés: 1-nél nagyobbak 10-szeresei (késleltetés!)
            Console.WriteLine("Szűrés: 1-nél nagyobbak 10-szeresei\n");
            var result7 = from number in list
                          where number > 1
                          select number * 10;
            list.Add(80);
            foreach (var item in result7)//a foreach ciklus váltja
            { //ki a szűrő elindulását
                Console.Write("{0} ", item);
            }
            NyomBill();
        }
        static void NyomBill()
        {
            Console.WriteLine("\nNyomjon meg egy billentyűt!");
            Console.ReadKey(true);
            Console.WriteLine();
        }
    }
}

//namespace LINQ_peldak2
//{
//    class Person
//    {
//        public int ID { get; set; }
//        public string FirstName { get; set; }
//        public string LastName { get; set; }
//        public string PhoneNumber { get; set; }
//        public Person(int id, string fn, string ln, string pn)
//        {
//            ID = id;
//            FirstName = fn;
//            LastName = ln;
//            PhoneNumber = pn;
//        }
//    }
//    internal class Program
//    {
//        static void Main()
//        {
//            List<Person> list = new List<Person>()
//{
//new Person(1,"Lajos","Kis","123-4567"),
//new Person(2,"Béla","Nagy","234-5678"),
//new Person(3,"Miklós","Szabó","345-6789"),
//new Person(4,"Gyula","Kovács","111-2222"),
//new Person(5,"Jenő","Cipész","222-3333"),
//};
//            //Projekció (és szűrés): névtelen osztállyal
//            //a páratlan ID-jű személyek teljes neve és
//            //telefonszáma
//            var result = from person in list
//                         where person.ID % 2 == 1
//                         select new
//                         {
//                             Name = person.LastName + " " + person.FirstName,
//                             PhoneNumber = person.PhoneNumber
//                         };
//            foreach (var person in result)
//            {
//                Console.WriteLine("Név: {0}, Telefon: {1}", person.Name, person.PhoneNumber);
//            }
//            Console.ReadKey();
//        }
//    }
//}
//
//namespace LINQ_peldak3
//{
//    internal class Program
//    {
//        static void Main()
//        {
//            List<string> names = new List<string>()
//{
//"Lajos","Béla","Miklós","Gyula","Jenő",
//"Kálmán","Attila", "Alajos", "Elemér",
//"Edina", "Ede", "Márton"
//};
//            //Rendezés
//            var result = from name in names
//                         orderby name //descending-gel csökkenő
//                         select name;
//            foreach (var item in result)
//            {
//                Console.WriteLine(item);
//            }
//            Console.ReadKey(true);
//            Console.WriteLine();
//            var result2 = names.OrderBy(x => x);
//            //csökkenő sorrend:
//            //var result2 = names.OrderBy(x => x).Reverse();
//            foreach (var item in result2)
//            {
//                Console.WriteLine(item);
//            }
//            Console.ReadKey();
//            Console.WriteLine();
//            //Rendezés: kezdőbetű, majd 2. betű alapján
//            var result3 = from name in names
//                          orderby name[0], name[1]
//                          select name;
//            foreach (var item in result3)
//            {
//                Console.WriteLine(item);
//            }
//            Console.ReadKey(true);
//            Console.WriteLine();
//            var result4 = names.OrderBy(name => name[0])
//            .ThenBy(name => name[1]);
//            foreach (var item in result4)
//            {
//                Console.WriteLine(item);
//            }
//            Console.ReadKey();
//            List<int> list = new List<int>() { 4, 6, 3, 1, 2, 11, 13 };
//            list.Sort((x, y) => ((x % 5).CompareTo(y % 5)));
//            foreach (var item in list)
//            {
//                Console.WriteLine(item);
//            }
//            Console.ReadKey();
//            Console.WriteLine();
//            //csoportosítás
//            var result5 = from name in names
//                          orderby name[0]
//                          group name by name[0]
//            into namegroup
//                          select namegroup;
//            foreach (var group in result5)
//            {
//                Console.WriteLine(group.Key);
//                foreach (var name in group)
//                {
//                    Console.WriteLine("-- {0}", name);
//                }
//            }
//            Console.ReadKey(true);
//            Console.WriteLine();
//            var result6 = names.OrderBy(name => name[0])
//            .ThenBy(name => name)
//            .GroupBy(name => name[0]);
//            foreach (var group in result6)
//            {
//                Console.WriteLine(group.Key);
//                foreach (var name in group)
//                {
//                    Console.WriteLine("-- {0}", name);
//                }
//            }
//            Console.ReadKey(true);
//        }
//    }
//}
//
