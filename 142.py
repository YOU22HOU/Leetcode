# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while(slow != fast):
                    slow = slow.next
                    fast = fast.next
                return fast
        return None