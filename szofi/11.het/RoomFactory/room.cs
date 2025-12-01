namespace RoomFactory
{

    public class room
    {

    }

    public class DataReader : IdateReader
    {
        public List<Room> rooms = new List<Room>();
        XElement xdoc = new XElement.Load("room.xml");
        var item from item in xdoc.Descendants("oneRoom")
    }



    public static class RoomCreator
    {
        public static char[,] CreateRoom(string roomId, IDataReader daraSource)
        {
            Room r = daraSource.GetRooms().Find(room=>roomId==room.Id);
            char [,] cin = new char[r.Height,r.Width];
            for (int i = 0; i <cin.GetLength(0); i++)
            {
                for (int j = 0; j<cin.GetLength(1); j++)
                {
                    cin[i,j] = 'O';
                }
            }
            return cin;
        }
    }
}
