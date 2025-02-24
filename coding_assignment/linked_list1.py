class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_position(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        pos = 0
        cur = self.head
        while cur is not None and pos + 1 != index:
            pos += 1
            cur = cur.next

        if cur is not None:
            new_node.next = cur.next
            cur.next = new_node
        else:
            print("Index not present")

    def delete_at_position(self, index):
        if self.head is None:
            print("List is empty.")
            return
        cur = self.head
        pos = 0
        if index == 0:
            self.head = self.head.next
            return
        while cur is not None and pos < index - 1:
            pos += 1
            cur = cur.next
        if cur is None or cur.next is None:
            print("Index not present")
        else:
            cur.next = cur.next.next

    def printLL(self,head):
         if head is None:
            print("list is empty")
            return
         self.printLL(head.next) 
         print(head.data)

llist = LinkedList()

while True:
    ch = int(input("Enter 1- insert, 2- delete, 3- display, 4- exit: "))        
    if ch == 1:
        data = int(input("Enter the data of the node: "))
        index = int(input("Enter the index where the data has to be inserted: "))
        llist.add_at_position(data, index)
    elif ch == 2:
        index = int(input("Enter the index where the data has to be deleted: "))
        llist.delete_at_position(index)
    elif ch == 3:
        print("Current Linked List:")
        llist.printLL()
    elif ch == 4:
        break
    else:
        print("Invalid option. Please try again.")
