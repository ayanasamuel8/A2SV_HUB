# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def divide(self, left, right, instructions):
        if left == right:
            return [instructions[left]]
        mid = (left + right) // 2

        left_half = self.divide(left, mid, instructions)
        right_half = self.divide(mid + 1, right, instructions)
        return self.merge(left_half, right_half)

    def merge(self, left_half, right_half):
        merged_arr = []
        left = right = 0
        n,m = len(left_half), len(right_half)

        while left < n and right < m:
            if left_half[left][0] <= right_half[right][0]:
                merged_arr.append(left_half[left])
                left += 1
            else:

                self.counter_left[right_half[right]] += (n - left)
                merged_arr.append(right_half[right])
                right += 1
       
        merged_arr.extend(left_half[left:])
        merged_arr.extend(right_half[right:])
        return merged_arr

    def createSortedArray(self,instructions):
        n = len(instructions)
        MOD = int(1e9 + 7)
        instructions = [(instructions[i], i) for i in range(n)]

        self.counter_left = defaultdict(int)
        instructions = self.divide(0, n - 1, instructions)
        counter_right = defaultdict(int)
        freq = defaultdict(int)

        for i in range(n):
            counter_right[instructions[i]] = instructions[i][1] - self.counter_left[instructions[i]] - freq[instructions[i][0]]
            freq[instructions[i][0]] += 1

        number_op = 0

        for instruction in instructions:

            number_op =(number_op + min(counter_right[instruction], self.counter_left[instruction])) % MOD
        return number_op % MOD
