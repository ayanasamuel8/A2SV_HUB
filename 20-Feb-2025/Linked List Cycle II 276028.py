# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None
        slow = head
        fast = head.next.next

        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        
        if fast == slow:
            fast = head
            slow = slow.next.next
            while fast != slow:
                fast = fast.next
                slow = slow.next

        return slow if fast == slow else None