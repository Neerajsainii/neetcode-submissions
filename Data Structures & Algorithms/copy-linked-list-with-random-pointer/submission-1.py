"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newSet = {None:None}
        temp1 = head
        while temp1:
            copy = Node(temp1.val)
            newSet[temp1] = copy
            temp1 = temp1.next
        temp1 = head
        while temp1:
            copy = newSet[temp1]
            copy.next = newSet[temp1.next]
            copy.random = newSet[temp1.random]
            temp1 = temp1.next
        return newSet[head]
            
            
        