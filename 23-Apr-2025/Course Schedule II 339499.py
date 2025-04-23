# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+= 1
        
        ans = []
        noPre = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                ans.append(i)
                noPre.append(i)
        
        while noPre:
            u = noPre.popleft()
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    noPre.append(v)
                    ans.append(v)
        
        return ans if len(ans) == numCourses else []
