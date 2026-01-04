class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp, end=" ")
            if tmp:
                print("-->", end=" ")

        print()

    def insertAtBeggining(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node
        if self.tail == None:
            self.tail = self.head

    def instertAtPosition(self, data, n):
        new_Node = Node(data)
        if self.head == None or n <= 1:
            self.head.next = new_Node
            new_Node = self.head


lista = LinkedList()
lista.insertAtBeggining(2)
lista.printList()




