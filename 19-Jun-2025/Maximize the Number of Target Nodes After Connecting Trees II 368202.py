# Problem: Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def dfsCount(self, take, node, graph, visited):
        count = int(take)
        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                count += self.dfsCount(not take, v, graph, visited)
        return count
    
    def groupEven(self, take, node, graph, visited, group1, group2, count):
        if take:
            group1.add(node)
            count[0] += 1
        else:
            group2.add(node)
            count[1] += 1

        for v in graph[node]:
            if not visited[v]:
                visited[v] = True
                self.groupEven(not take, v, graph, visited, group1, group2, count)
            

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        furtherCount = [0] * (n:=(len(edges1) + 1))
        m = len(edges2) + 1
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
       
        for u,v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
       
        for u,v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
        
        visited = [False] * m
        visited[0] = True
        for_zero = self.dfsCount(True, 0, graph2, visited)
        
        visited = [False] * m
        visited[0] = True
        for_zeros_child = self.dfsCount(False, 0, graph2, visited)
        
        max_further = max(for_zero, for_zeros_child)
        
        group1 = set()
        group2 = set()
        count = [0, 0]
        visited = [False] * n
        visited[0] = True
        
        self.groupEven(True, 0, graph1, visited,group1, group2, count)

        ans =[max_further] * n
        for i in group1:
            ans[i] += count[0]
        for i in group2:
            ans[i] += count[1]




        return ans