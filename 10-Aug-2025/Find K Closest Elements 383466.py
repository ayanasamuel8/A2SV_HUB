# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        n = len(arr)
        if idx > n - 1:
            return arr[-k:]
        if idx < 0:
            return arr[: k]
        if arr[idx] == x:
            left = idx
            right = idx + 1
        else:
            left = idx - 1
            right = idx
        
        ans = []

        while len(ans) < k:
            if left < 0:
                ans.append(arr[right])
                right += 1
                continue
            if right >= n:
                ans.append(arr[left])
                left -= 1
                continue
            if abs(arr[left] - x) <= abs(arr[right] - x):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        return sorted(ans)
