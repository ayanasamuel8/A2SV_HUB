# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        sum_stack = [0]
        index_stack = [n]
        MOD = int(1e9 + 7)
        for i in range(n - 1, -1, -1):
            curr_sum = arr[i]
            while index_stack[-1] != n and arr[index_stack[-1]] >= arr[i]:
                index_stack.pop()
                sum_stack.pop()
            curr_sum += (index_stack[-1] - i - 1) * arr[i]
            curr_sum += sum_stack[-1]
            sum_stack.append(curr_sum)
            index_stack.append(i)
            total += curr_sum
        return total % MOD