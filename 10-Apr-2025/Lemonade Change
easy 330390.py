# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)
        n = len(bills)
        for i in range(n):
            if bills[i] == 5:
                dic[5] += 1
            elif bills[i] == 10 and dic[5] >= 1:
                dic[10] += 1
                dic[5] -= 1
            elif bills[i] == 20 and (dic[5] >= 3 or (dic[5] >= 1 and dic[10] >= 1)):
                if dic[10]:
                    dic[10] -= 1
                    dic[5] -= 1
                else:
                    dic[5] -= 3
            else: return False
        return True