# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for u,v in prerequisites:
            graph[u].append(v)
            indeg[v] += 1
        
        zeroIndeg = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                zeroIndeg.append(i)
        
        ancestors = [set() for _ in range(numCourses)]

        while zeroIndeg:
            u = zeroIndeg.popleft()
            for v in graph[u]:
                ancestors[v].update(ancestors[u])
                ancestors[v].add(u)
                indeg[v] -= 1
                if indeg[v] == 0:
                    zeroIndeg.append(v)
        result = []
        for u,v in queries:
            result.append(u in ancestors[v])
        
        return result