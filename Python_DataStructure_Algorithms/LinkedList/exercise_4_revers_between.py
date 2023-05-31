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
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def reverse_between(self, m, n):
        if self.length <= 1:
            return
    
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
    
        for i in range(m):
            prev = prev.next
    
        current = prev.next
    
        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
    
        self.head = dummy.next
        
"""
This code implements a function reverse_between to reverse a section of a linked list between the nodes at the 0-based indices m and n (inclusive).



If the linked list is empty (self.length is <= 1), return.

Create a dummy node with value 0 and set its next pointer to the head of the linked list. The purpose of the dummy node is to handle cases when the head of the list is also reversed.

Initialize a pointer prev to the dummy node.

Iterate from 0 to m (exclusive), moving the prev pointer forward in the list. After the loop, prev will point to the node just before the m-th node in a 0-based index linked list. In other words, prev will be at the position m-1 in the 0-based index.

For example, if m = 2, the loop will execute 2 times, and prev will point to the node at index 1 (0-based), which is just before the node at index m.

Set the current pointer to the node next to prev (i.e., the node at index m).

Iterate from 0 to n - m (exclusive) to reverse the section of the linked list between indices m and n. In each iteration:

Set temp to the node next to current (i.e., the next node to be reversed). The temp pointer holds the next node that will be moved to the beginning of the reversed section.

Update the next pointer of the current node to point to the node next to temp. This step detaches temp from its current position and connects the current node to the remaining part of the sublist that is yet to be reversed.

Update the next pointer of the temp node to point to the node currently next to prev. This step is for placing the temp node at the beginning of the reversed section.

Update the next pointer of the prev node to point to temp. This step connects the temp node, now at the beginning of the reversed section, to the part of the list that comes before the reversed section.

After each iteration, the current node remains the same, but the sublist between the current node and the n-th node (inclusive) is gradually reversed.

After the loop, the section of the linked list between indices m and n is reversed. Update the head of the linked list to the node next to the dummy node. This step ensures that if the head of the list was reversed, the new head will be correctly assigned.



In summary, this code reverses the sublist between the nodes at indices m and n (inclusive) in a linked list, assuming 0-based indexing. It does so by iteratively updating pointers within the sublist and connecting it back to the original list correctly. The use of a dummy node simplifies edge cases when the head of the list is part of the reversed section.





Code with inline comments:



def reverse_between(self, m, n):
    # Return if the list is empty or has one node
    if self.length <= 1:
        return
 
    # Create a dummy node and set it before head
    dummy = Node(0)
    dummy.next = self.head
    prev = dummy
 
    # Move prev to the node at index m-1
    for i in range(m):
        prev = prev.next
 
    # Set current to the node at index m
    current = prev.next
 
    # Reverse the sublist between indices m and n
    for i in range(n - m):
        # Set temp to the next node to be reversed
        temp = current.next
        # Detach temp and connect current to next node
        current.next = temp.next
        # Place temp at the beginning of the reversed section
        temp.next = prev.next
        # Connect temp to the part before the reversed section
        prev.next = temp
 
    # Update the head of the list if necessary
    self.head = dummy.next
"""
        
      
    


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
