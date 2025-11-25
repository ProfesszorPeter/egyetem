namespace LINQ_peldak
{
    internal class Program
    {
        static void Main()
        {
            List<string> names = new List<string>()
            {
                "Lajos","Béla","Miklós","Gyula","Jenő","Kálmán","Attila","Alajos",
                "Elemér","Edina", "Ede", "Márton"
            };
            var result = from name in names
                         orderby name
                         select name;

            foreach (var name in result)
            {
                Console.WriteLine(name);
            }

            Console.WriteLine($"\n2. feladat");
            var result2 = names.OrderBy(x => x);
            //csökkenő sorrend:
            //var result2 = names.OrderBy(x => x).Reverse();
            foreach (var item in result2)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine($"\n3. feladat");
            var result3 = from name in names
                          orderby name == null ? '0' : name[0],name == null ? '0' : name[1]
                          select name;

            foreach (var item in result3)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine($"\n4.feladat");
            var result4 = names.OrderBy(name => name[0]).ThenBy(name => name[1]);
            foreach (var item in result3)
            {
                Console.WriteLine(item);
            }


            Console.WriteLine($"\n5.feladat");
            List<int> list = new List<int>() {4,6,3,1,2,11,13};
            list.Sort((x,y) => ((x%5).CompareTo(y%5)));
            foreach (var item in result3)
            {
                Console.WriteLine(item);
            }

            Console.WriteLine($"\n5.feladat");
            var result6 = from name in names
                          orderby name[0]
                          group name by name[0]
                          into namegroup
                          select namegroup;

            foreach (var item in result6)
            {
                Console.WriteLine($"Kezdőbetű: {group.Key}");
            }

        }
    }
}
