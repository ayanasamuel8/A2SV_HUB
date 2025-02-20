# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node, not_to):
            prev = not_to
            while node and node != not_to:
                next =node.next
                node.next = prev
                prev = node
                node = next
            return prev
        dummy = ListNode(0,head)
        current = head
        curernt_dummy = dummy

        while current:
            left = current
            i = k
            while current and i:
                i -= 1
                current = current.next
            if not i:
                new_node = reverse(left, current)
                curernt_dummy.next = new_node
                curernt_dummy = left
        return dummy.next