using System.Xml.Linq;
namespace Linq
{
    class Program
    {
        static void Main()
        {
            //1.f/a
            XElement xelement = XElement.Load("../szemelyek.xml");
            IEnumerable<XElement> szemelyek = xelement.Elements();

            foreach (var szemely in szemelyek)
            {
                Console.WriteLine(szemely);
            }

            //1.f/b
            XDocument xdocument = XDocument.Load("../szemelyek.xml");
            IEnumerable<XElement> szemelyek2 = xdocument.Root.Elements();
            foreach (var szemely in szemelyek2)
            {
                Console.WriteLine(szemely);
            }
            Console.WriteLine("\n");

            //2.feladat
            foreach(var szemely in szemelyek)
                {
                    Console.WriteLine(szemely.Element("Nev").Value);
                }

            Console.WriteLine("3.feladat\n");
            var ferfiak = from item in szemelyek
                          where string()item.Element("Nem") == "férfi"
                          select item;
        }
    }
}
