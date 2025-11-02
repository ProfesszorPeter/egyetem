class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self,data):
        self.head = None
        self.tail = None

    def InsertBegginig(self, data):
        new_node = Node(data)
        self.head = new_node
        if self.tail == None:
            self.tail = self.head

    def PrintList(self):
        tmp = self.head
        while tmp:



list = LinkedList()

list.InsertBegginig("lofasz")



