# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
array1 = list(map(int,input().split()))
m = int(input())
array2 = list(map(int,input().split()))

left = right = 0
n_size = n
m_size = m
f= True
while left<n and right<m:
    if array1[left] == array2[right]:
        left+=1
        right+=1
        continue
    if left<n-1 and array1[left]<array2[right]:
        array1[left+1] += array1[left]
        n_size -=1
        left +=1
    elif left == n-1 and array1[left]<array2[right]: 
        left += 1
        f= False
    elif right<m-1 and array1[left]>array2[right]:
        array2[right+1]+=array2[right]
        m_size -= 1
        right +=1
    elif right == m-1 and array1[left]>array2[right]: 
        right +=1
        f=False
if not f: print(-1)
elif left == n and right == m: print(min(m_size,n_size))
else: print (-1)