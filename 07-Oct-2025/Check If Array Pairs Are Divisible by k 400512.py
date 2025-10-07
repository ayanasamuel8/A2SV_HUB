# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = defaultdict(int)
        for i in arr:
            mods[((i % k) + k) % k] += 1
        for key, val in mods.items():
            rev_mod = k - key
            if (rev_mod not in mods or mods[rev_mod]!= val) and (key != 0 or val % 2 == 1):
                return False
        return True