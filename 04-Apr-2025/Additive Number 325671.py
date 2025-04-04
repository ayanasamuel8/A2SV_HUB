# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def backTrack(self, idx, num, last_one, last_two, into):
        if idx == len(num) and into > 2:
            return True
        elif idx == len(num):
            return False
        if last_two == -inf:
            curr = 0
            for i in range(idx, len(num)):
                curr = curr * 10 + int(num[i])
                if self.backTrack(i + 1, num, curr, last_one,into + 1):
                    return True
                elif curr == 0:
                    return False
        else:
            curr = 0
            for i in range(idx, len(num)):
                curr = curr * 10 + int(num[i])
                if curr == last_one + last_two:
                    if self.backTrack(i + 1, num, curr, last_one, into + 1):
                        return True
                elif curr >= last_one + last_two or curr == 0:
                    return False
        return False

    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        return self.backTrack(0,num,-inf,-inf,0)