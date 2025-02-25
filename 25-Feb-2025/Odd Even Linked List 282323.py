# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return head
        next = head.next
        current = left = head

        while current and current.next and current.next.next:
            current = current.next
            left.next = current.next
            current.next = left.next.next
            left.next.next = next
            left = left.next
        
        return head
