# Problem: Alien Dictionary - https://practice.geeksforgeeks.org/problems/alien-dictionary/1

class Solution:
    def findOrder(words):
        
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for word in words:
            for char in word:
                if char not in indeg:
                    indeg[char] = 0
                    
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return ''
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].append(words[i + 1][j])
                    indeg[words[i + 1][j]] += 1
                    break
        q = deque()
        for key in indeg.keys():
            if indeg[key] == 0:
                q.append(key)
        toposorted = []
        while q:
            front = q.popleft()
            toposorted.append(front)
            for v in graph[front]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(toposorted) != len(indeg):
            return ''
        return toposorted