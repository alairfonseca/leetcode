# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        carry = 0
        summ = 0
        
        while l1 or l2 or carry:
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next

            summ += carry
            cursor = result
            while cursor.next:
                cursor = cursor.next

            cursor.next = ListNode(summ % 10)
            
            carry = summ // 10
            summ = 0
                
        return result.next