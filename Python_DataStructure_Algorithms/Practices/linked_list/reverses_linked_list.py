# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
prev = null
next = 2
1.next = null

  head
   1         2        3 
"""
def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

newNode = reverseList(head)

while newNode != None:
    print(newNode.val)
    newNode = newNode.next 
