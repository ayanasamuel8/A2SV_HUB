# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left = l1
        right = l2
        carry = 0
        result = ListNode()
        current = result
        prev = None

        while left and right:
            total = left.val + right.val + carry
            node = ListNode(total % 10)
            current.next = node
            prev = current
            current = current.next
            carry = total // 10
            left = left.next
            right = right.next
        while left:
            total = left.val + carry
            node = ListNode(total % 10)
            current.next = node
            prev = current
            current = current.next
            carry = total // 10
            left = left.next
        while right:
            total = right.val + carry
            node = ListNode(total % 10)
            current.next = node
            prev = current
            current = current.next
            carry = total // 10
            right = right.next
        while carry:
            node = ListNode(carry)
            current.next = node
            current = current.next
            carry //= 2
        return result.next
