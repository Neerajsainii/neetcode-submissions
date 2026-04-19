# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 ,temp2 = l1, l2
        carry = 0
        while temp1.next and temp2.next:
            temp1.val = temp1.val + temp2.val + carry
            carry = 0
            if temp1.val >= 10 :
                temp1.val -= 10
                carry = 1
            temp1 = temp1.next
            temp2 = temp2.next
        temp1.val = temp1.val + temp2.val + carry
        carry = 0
        if temp1.val >= 10 :
            temp1.val -= 10
            carry = 1
        if temp1.next is not None and temp2.next is None:
            temp1 = temp1.next
            while carry and temp1.next:
                temp1.val = temp1.val + carry
                carry = 0
                if temp1.val == 10:
                    temp1.val = 0
                    carry = 1
                temp1 = temp1.next
            if temp1.val + carry == 10:
                temp1.val = 0
                carry = 1
                newHead = ListNode()
                newHead.val = 1
                temp1.next = newHead
            else:
                temp1.val += carry
        elif temp1.next is None and temp2.next is not None:
            temp1.next = temp2.next
            temp1 = temp1.next
            while carry and temp1.next:
                temp1.val = temp1.val + carry
                carry = 0
                if temp1.val == 10:
                    temp1.val = 0
                    carry = 1
                temp1 = temp1.next
            if temp1.val + carry == 10:
                temp1.val = 0
                carry = 1
                newHead = ListNode()
                newHead.val = 1
                temp1.next = newHead
        elif carry == 1:
            newHead = ListNode()
            newHead.val = 1
            temp1.next = newHead
        return l1