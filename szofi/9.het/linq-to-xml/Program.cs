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
            foreach (var szemely in szemelyek)
            {
                Console.WriteLine(szemely.Element("Nev").Value);
            }

            //Console.WriteLine("3.feladat\n");
            //var ferfiak = from item in szemelyek
            //              where string()item.Element("Nem") == "férfi"
            //              select item;
            //

            //5.feladat
            Console.WriteLine("\n5.feladat");
            var pecsiek = from item in szemelyek
                          where (string)item.Element("Lakcim").Element("Helyseg") == "Pécs"
                          select item;

            foreach (var pecsi in pecsiek)
            {
                Console.WriteLine(pecsi.Element("Nev").Value);
            }


            //6.feladat
            Console.WriteLine("\n6.feladat");
            Console.WriteLine("Irányítószámok: ");
            foreach (var item in xelement.Descendants("IrSzam"))
            {
                Console.WriteLine(item.Value);
            }


            //7.feladat
            Console.WriteLine("\n7.feladat");
            var irszamok = from item in szemelyek
                           let irszam = item.Element("Lakcim").Element("IrSzam").Value
                           orderby irszam
                           select irszam;
            foreach (var irszam in irszamok)
            {
                Console.WriteLine(irszam);
            }


            //8.feladat
            Console.WriteLine("\n8.feladat");
            var sz_ek = szemelyek.Skip(1).Take(2).Reverse();
            foreach (var szemely in sz_ek)
            {
                Console.WriteLine(szemely.Element("Nev").Value);
            }


            //10.feladat
            Console.WriteLine("\n10.feladat");
            XDocument xDoc = new XDocument(
                    new XDeclaration("1.0", "UTF-16", null),
                    new XElement("Szemelyek",
                        new XElement("Szemely",
                            new XComment("Most csak 3 elem"),
                            new XElement("Azon", "1"),
                            new XElement("Nev", "Béla"),
                            new XElement("Nem", "férfi")
                            )
                        )
                    );

        }
    }
}
