class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: 

    def __init__(self):
        self.head = None

    def delete(self, data):
        temp = self.head
        if temp is None:
            return
        if temp.data == data:
            self.head = temp.next
            temp = None
            return
        while temp is not None:
            temp_next = temp.next
            if temp_next is None:
                continue
            if temp_next.data == data:
                temp.next = temp.next.next
                temp_next = None
                break
            temp = temp.next

    def insert(self, index, data):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            return
        prev = self.__getPrev(index)
        node.next = prev.next
        prev.next = node
        
    def __getPrev(self, index):
        temp = self.head
        count = 1
        while (count < index and temp.next is not None):
            temp = temp.next
            count += 1
        return temp
        
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next



linkedList = LinkedList()
linkedList.insert(0,1)
linkedList.insert(0,2)
linkedList.insert(1,3)
# linkedList.head = Node(1)
# linkedList.head.next = Node(2)
# linkedList.head.next.next = Node(3)

#linkedList.delete(1)

linkedList.printList()

