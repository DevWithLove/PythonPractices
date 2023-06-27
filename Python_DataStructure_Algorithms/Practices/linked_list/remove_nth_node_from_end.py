"""
19. Remove Nth Node From End of List
Medium
16.1K
673
Companies
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n) -> ListNode:
        temp = head 
        length = 0
        while temp is not None: 
            length += 1
            temp = temp.next
        if length == n: 
            # if length is same n which means remove the head, so we return the next node of the head
            return head.next
        # find out which node need to be removed, for example if length is 5, n is 2
        # get position we want to remove the node at.
        length -= (n+1)
        first = head
        # we will get the before node of the remvoing node
        while length > 0:
            first = first.next
            length -= 1
        first.next = first.next.next
        return head
    
    """
    
    N =2 
    null -> 1 ->2 ->3 ->4 ->5-> null

    second         first 

    """
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        first = ans
        second = ans
        # n +2 because the range will stop before end, which will be n+1
        for i in range(1,n+2):
            first = first.next
        
        while (first is not None):
            first = first.next
            second = second.next

        second.next = second.next.next
        return ans.next

