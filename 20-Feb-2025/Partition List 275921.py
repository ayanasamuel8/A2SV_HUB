# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not(head and head.next): return head
        dummy = ListNode()
        dummy.next = head
        left = right = dummy

        while left and left.next and left.next.val < x:
            left = left.next
            right = right.next

        while left and right and right.next:
            while right and right.next and right.next.val >= x:
                right = right.next
            if right and right.next:
                tobe_shifted = right.next
                right.next = right.next.next
                tobe_shifted.next = left.next
                left.next = tobe_shifted
                left = left.next
        return dummy.next