# 快慢指针
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:

        slow = head  # 慢指针
        fast = head  # 快指针

        while k+1 > 0:
            fast = fast.next
            k -= 1

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        while head is not None:
            print(head.val)
            head = head.next

if __name__ == '__main__':
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,)))))
    obj = Solution()
    Node = obj.kthToLast(a, 2)

    
    # 结果为 1，2，4，5
