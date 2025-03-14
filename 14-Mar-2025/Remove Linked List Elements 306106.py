# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeVal(self, head, val):
        if not head or not head.next: return
        if head.next.val == val:
            head.next = head.next.next
        else:
            head = head.next
        self.removeVal(head, val)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        self.removeVal(dummy, val)
        return dummy.next