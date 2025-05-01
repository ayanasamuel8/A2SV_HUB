# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0] * n

        group_graph = defaultdict(set)
        group_indeg = defaultdict(set)

        start = n
        for i in range(n):
            if group[i] == -1:
                group[i] = start
                start += 1

        for i in range(n):
            for j in beforeItems[i]:
                graph[j].append(i)
                indeg[i] += 1
                if group[i] != group[j]:
                    group_graph[group[j]].add(group[i])
                    group_indeg[group[i]].add(group[j])
        
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        if len(topo) != n:
            return []

        q = deque()
        groups = set(group)
        for i in groups:
            if len(group_indeg[i]) == 0:
                q.append(i)
        
        topo_sorted = []
        while q:
            u = q.popleft()
            topo_sorted.append(u)
            for v in group_graph[u]:
                group_indeg[v].remove(u)
                if len(group_indeg[v]) == 0:
                    q.append(v)
        if len(topo_sorted) < len(groups):
            return []
        groupping = defaultdict(list)
        for i in topo:
            groupping[group[i]].append(i)
        ans = []
        for i in topo_sorted:
            ans.extend(groupping[i])
        return ans