# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t = int(input())
while t:
    t -= 1
    n = int(input())
    string = input()
    elements = set(string)
    ans = float('inf')
    for i in elements:
        count = 0
        left, right = 0, len(string)-1
        f = True
        while left < right:
            if string[left] != string[right]:
                count += 1
                if string[left] == i : left +=1
                elif string[right] == i: right -= 1
                else:
                    f = False 
                    break
            else:
                left += 1
                right -= 1
        if f :
            ans = min(ans, count)
    print(ans if ans != float('inf') else -1)