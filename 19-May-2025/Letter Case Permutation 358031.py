# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = [i for i, c in enumerate(s) if c.isalpha()]
        result = []
        n = len(letters)

        for i in range(1 << n):
            lst = list(s)
            for j in range(n):
                if i & (1 << j):
                    idx = letters[j]
                    lst[idx] = lst[idx].swapcase()
            result.append(''.join(lst))
        return result