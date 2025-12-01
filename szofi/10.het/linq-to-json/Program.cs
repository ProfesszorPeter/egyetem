using Newtonsoft.Json;
namespace Linq
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamReader szovFajl = new StreamReader("../adatok.json");
            string json = szovFajl.ReadToEnd();
            JArray tanuloArray = JArray.Parse(json);
        }
    }
    
}

