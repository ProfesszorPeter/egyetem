//Feladat leírása
//
//Írj egy konzolalkalmazást, amely egy egész számokat tartalmazó listából képes különböző feltételek szerint szűrni az elemeket.
//A szűrést delegate segítségével, illetve lambda-kifejezéssel is el kell tudni végezni.
//Követelmények
//
//    Definiálj egy delegate típust
//        Név: SzuroPredicate
//        Alak: bool SzuroPredicate(int szam)(azaz egy int paramétert fogad, és bool-t ad vissza – igaz, ha a szám megfelel a feltételnek).
//    Írj egy általános szűrő metódust
//        Név: Szures
//        Paraméterek:
//        csharp
//
//    List<int> bemenet, SzuroPredicate feltetel
//
//    Visszatérési érték: List<int> – csak azok a számok, amelyekre feltetel(szam)igaz.
//    A metódus csak a delegate-et használja a döntéshez (ne legyen benne saját logika).
//
//Készíts legalább két konkrét szűrő metódust (amelyek megfelelnek a delegate-nek):
//
//    PárosE – igaz, ha a szám páros.
//    NagyobbMintTíz – igaz, ha a szám > 10.
//
//A Main-ben
//
//    Hozz létre egy List<int> legalább 8-10 elemmel (pl. {3, 12, 7, 20, 5, 14, 9, 11, 4, 18}).
//    Delegate-példányosítással hívd meg a Szures-t a két fenti metódussal, és írd ki az eredményt.
//    Lambda-kifejezéssel is hívd meg a Szures-t legalább két különböző feltétellel (pl. „5 és 15 között”, „3-mal osztható”), és írd ki az eredményeket.
//
//Segédmetódus
//
//    Egy egyszerű Kiir(List<int> lista) metódus, amely szépen kiírja a lista elemeit vesszővel elválasztva.


namespace gyak_delegate
{
    class Program
    {
        Delegate bool SzuroPredicate(int szam);

        public List<int> Szures(

        static void Main(string[] args)
        {

        }

    }
}



