# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        t = dummy
        overflow = 0

        while l1 and l2:
            result = l1.val + l2.val + overflow
            if result > 9:
                overflow = 1
                result %= 10
            else:
                overflow = 0
            t.next = ListNode(result)
            t = t.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            result = l1.val + overflow
            if result > 9:
                overflow = 1
                result %= 10
            else:
                overflow = 0
            t.next = ListNode(result)
            t = t.next
            l1 = l1.next

        while l2:
            result = l2.val + overflow
            if result > 9:
                overflow = 1
                result %= 10
            else:
                overflow = 0
            t.next = ListNode(result)
            t = t.next
            l2 = l2.next

        if overflow:
            t.next = ListNode(overflow)

        return dummy.next