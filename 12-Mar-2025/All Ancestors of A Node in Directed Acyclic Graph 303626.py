# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)] 
        indegree = [0] * n
        for parent,  child in edges:
            adj[parent].append(child)
            indegree[child] += 1
        roots = deque()
        for i in range(n):
            if not indegree[i]:
                roots.append(i)
        ancestors = [set() for _ in range(n)]

        while roots:
            root = roots.pop()
            for nbr in adj[root]:
                ancestors[nbr].update(ancestors[root])
                ancestors[nbr].add(root)
                indegree[nbr] -= 1
                if not indegree[nbr]:
                    roots.append(nbr)
        for i in range(n):
            ancestors[i] = sorted((ancestors[i]))
        return ancestors