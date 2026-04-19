# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return None
        if head.next is None or head.next.next is None:
            return 
        
        slow , fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp1 = None
        tmp2 = slow.next
        tmp3 = slow.next.next
        slow.next = None
        while tmp2:
            tmp2.next = tmp1
            tmp1 = tmp2
            tmp2 = tmp3
            if tmp3 is not None:
                tmp3 = tmp3.next
        # temp = tmp1
        # while temp:
        #     print(temp.val)
        #     temp = temp.next
        first = head
        second = tmp1
        tmp1 = first.next
        tmp2 = second.next
        while first and second:
            first.next = second
            first = tmp1
            if tmp1 is not None:
                tmp1 = tmp1.next
            second.next = first
            second = tmp2
            if tmp2 is not None:
                tmp2 = tmp2.next
        






        
