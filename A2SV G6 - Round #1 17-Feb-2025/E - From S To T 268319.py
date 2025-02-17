# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

size = int(input())

def check(s,t):
    flag=False
    for i in s:
        if i in t:
            t=t[t.index(i)+1:]
        else:
            flag=True
            break
    return flag


while size:
    size-=1
    s,t,p=input(),input(),input()
    if len(s)>len(t):
        print("NO")
    else:
        f=check(s,t)
        if f:
            print('NO')
            continue
        map_for_t={}
        for i in t:
            if i in map_for_t:
                map_for_t[i]+=1
            else:
                map_for_t[i]=1
        map_for_s={}
        for i in s:
            if i in map_for_s:
                map_for_s[i]+=1
            else:
                map_for_s[i]=1
        for key,value in map_for_t.items():
            if  key in map_for_s and map_for_s[key]>value:
                print('NO')
                break
        else:
            for i in p:
                if i in map_for_s:
                    map_for_s[i]+=1
                else:
                    map_for_s[i]=1
            flag=True
            for key,value in map_for_t.items():
                if not key in map_for_s or map_for_s[key]<value:
                    flag =False
                    break
            if(flag): print('YES')
            else: 
                print('NO')