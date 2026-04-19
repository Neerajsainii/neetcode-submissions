# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = temp2 = ListNode()
        temp1.next = temp2.next = head
        count = 0
        while temp1.next:
            temp1 = temp1.next
            count += 1
        c = count - n
        temp1 = temp2
        while c:
            temp2 = temp2.next
            c -= 1
        temp2.next =  temp2.next.next
        return temp1.next
