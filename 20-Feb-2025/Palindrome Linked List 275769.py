# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        reversed_node = reverse(slow)
        current = head
        while reversed_node:
            if current.val != reversed_node.val: return False
            current = current.next
            reversed_node = reversed_node.next
        return True