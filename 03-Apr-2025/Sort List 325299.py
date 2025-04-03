# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):
        root = ListNode()
        curr = root
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        else:
            curr.next = right
        return root.next

    def divide(self, head):
        if not head:
            return None
        if not head.next:
            return ListNode(head.val)
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        left = self.divide(slow.next)
        slow.next = None
        right = self.divide(head)
        return self.merge(left, right)
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.divide(head)