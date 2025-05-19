# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = set([s])
        n = len(s)
        for i in range(2 << n):
            lst = list(s)
            changed = False
            for j in range(n):
                if i & (1 << j):
                    if lst[j].isalpha():
                        changed = True
                        lst[j] = lst[j].swapcase()
            if changed:
                result.add(''.join(lst))
        return list(result)