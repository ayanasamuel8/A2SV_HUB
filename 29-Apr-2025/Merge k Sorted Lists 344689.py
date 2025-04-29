# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedList = ListNode()
        current = mergedList
        n = len(lists)
        heap = []
        for i in range(n):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while heap:
            minValue, curr_idx = heappop(heap)
            current.next = ListNode(minValue)
            current = current.next
            if lists[curr_idx]:
                heappush(heap, (lists[curr_idx].val , curr_idx))
                lists[curr_idx] = lists[curr_idx].next

        return mergedList.next
