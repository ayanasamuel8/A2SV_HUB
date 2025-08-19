# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            while lst:
                heappush(heap, lst.val)
                lst = lst.next
        if not heap: return None
        ans = ListNode(heappop(heap))
        curr = ans
        while heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next
        
        return ans