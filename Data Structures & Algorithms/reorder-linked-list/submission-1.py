# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        lis = []
        temp = head
        while temp:
            lis.append(temp)
            temp = temp.next
        n = len(lis)
        temp = head
        j = 0
        k = 0
        for i in range(n):
            if i % 2 == 0:
                temp.next = lis[n - 1 - j]
                j += 1
            else:
                temp.next = lis[k+1]
                k += 1
            temp = temp.next
        temp.next = None
            
        # if n > 0: