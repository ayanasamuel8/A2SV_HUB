# Problem: Maximum Number of Achievable Transfer Requests - https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        exchange = [0] * n
        max_taken = 0
        def backtrack(i, taken):
            nonlocal max_taken
            if i >= len(requests):
                if len(set(exchange)) == 1 and exchange[0] == 0:
                    max_taken = max(max_taken, taken)
                return
            
            from_, to = requests[i]
            backtrack(i + 1, taken)
            exchange[from_] -= 1
            exchange[to] += 1
            backtrack(i + 1, taken + 1)
            exchange[from_] += 1
            exchange[to] -= 1
        backtrack(0, 0)
        
        return max_taken