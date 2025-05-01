# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(start, proc, idx) for idx, (start, proc) in enumerate(tasks)])
        
        ans = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)
        
        while i < n or heap:
            while i < n and tasks[i][0] <= time:
                start, proc, idx = tasks[i]
                heappush(heap, (proc, idx))
                i += 1
            
            if heap:
                proc, idx = heappop(heap)
                time += proc
                ans.append(idx)
            else:
                time = tasks[i][0]
        
        return ans
