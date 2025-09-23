# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n, m = len(v1), len(v2)
        max_len = max(n, m)
        v1 += [0] * (max_len - n)
        v2 += [0] * (max_len - m)
        # v1 = '.'.join(map(str, version1))
        # v2 = '.'.join(map(str, version2))

        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
        return 0