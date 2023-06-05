"""
LL: Partition List ( ** Interview Question)
You are given a singly linked list implementation in Python that does not have a tail pointer (which will make this method simpler to implement).

You are tasked with implementing a method partition_list(self, x) that will take an integer x and partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

You need to implement this method as a method of the LinkedList class. The method should take an integer x as input. If the linked list is empty, the method should return None.

To implement this method, you should create two new linked lists. These two linked lists will be made up of the original nodes from the linked list that is being partitioned, one for nodes less than x and one for nodes greater than or equal to x.  None of the nodes from the linked list should be duplicated.

The creation of a limited number of new nodes is allowed (e.g., dummy nodes to facilitate the partitioning process).

You should then traverse the original linked list and append each node to the appropriate new linked list.

Finally, you should connect the two new linked lists together.



Let's consider the list 2 -> 8 -> 1 -> 4 -> 3 -> 7, and we'll partition around the value 4.



Before

2 -> 8 -> 1 -> 4 -> 3 -> 7


After

After calling the partition_list(4), we have:

2 -> 1 -> 3 -> 8 -> 4 -> 7


Explanation:

The partition_list method separates the nodes into two lists, one for nodes with values less than x and the other for nodes with values equal to or greater than x. The function then concatenates these two lists.

In the above example, the nodes with values less than 4 (i.e., 2, 1, and 3) come before the nodes with values equal to or greater than 4 (i.e., 8, 4, and 7).  The relative order of the nodes is preserved.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def partition_list(self, x):
        # Return if list is empty
        if not self.head:
            return None
 
        # Create two dummy nodes
        dummy1 = Node(0)  # Head for nodes < x
        dummy2 = Node(0)  # Head for nodes >= x
 
        # Pointers for the last node in both lists
        prev1 = dummy1
        prev2 = dummy2
 
        # Start at the head of the original list
        current = self.head

        # Traverse the original list
        while current:
            # If current node's value is less than x
             if current.value < x:
                # Add it to the end of the <x list
                prev1.next = current
                # Update prev1 to the new last node
                prev1 = current
             else:
                # If not, add it to the end of the >=x list
                prev2.next = current
                # Update prev2 to the new last node
                prev2 = current
             # Move to the next node
             current = current.next
 
        # Detach the last nodes of both lists
        prev1.next = None
        prev2.next = None
 
        # Link the end of the <x list to the start of the >=x list
        prev1.next = dummy2.next
 
        # Set head to the start of the partitioned list
        self.head = dummy1.next

    def partition_list_1(self, x):
        lessList = LinkedList(None)
        lessList.make_empty()
        moreList = LinkedList(None)
        moreList.make_empty()
        temp = self.head
        while temp is not None:
            if temp.value < x:
                lessList.append(temp.value)
            else:
                moreList.append(temp.value)
            temp = temp.next
        
        if lessList.head == None or moreList.head == None:
            return
        self.make_empty()
        temp = lessList.head
        while temp is not None:
            self.append(temp.value)
            temp = temp.next
        
        temp = moreList.head
        while temp is not None:
            self.append(temp.value)
            temp = temp.next
    
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
