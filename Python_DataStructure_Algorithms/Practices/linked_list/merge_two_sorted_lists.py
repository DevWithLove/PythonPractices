"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
		cur = ListNode(0)
		ans = cur
		
		while(l1 and l2):
			if(l1.val>l2.val):
				cur.next = l2
				l2 = l2.next
			else:
				cur.next = l1
				l1 = l1.next
			cur = cur.next
			
		while(l1):
			cur.next = l1
			l1 = l1.next
			cur = cur.next
		
		while(l2):
			cur.next = l2
			l2 = l2.next
			cur = cur.next
		return ans.next


l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_4 = ListNode(4)

l1_1.next = l1_2
l1_2.next = l1_4

l2_1 = ListNode(1)
l2_3 = ListNode(3)
l2_4 = ListNode(4)

l2_1.next = l2_3
l2_3.next = l2_4

ans = mergeTwoLists(l1_1,l2_1)

while ans != None:
	print(ans.val)
	ans = ans.next
