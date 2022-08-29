class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def deleteNode(self, head: ListNode):

        slow = head  # 慢指针
        fast = head  # 快指针


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)


if __name__ == '__main__':
    a = ListNode(14, ListNode(23, ListNode(10, ListNode(35, ListNode(56, ListNode(59,ListNode(12,)))))))
    obj = Solution()
    Node = obj.deleteNode(a)
    
    
# 结果为 35
