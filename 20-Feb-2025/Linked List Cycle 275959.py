# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        slow = head
        fast = head.next.next
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        
        return fast == slow and fast and fast.next