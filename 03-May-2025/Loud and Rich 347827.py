# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * (len(quiet))

        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque()

        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)
        
        ancestors = [set() for _ in range(len(quiet))]

        while queue:
            node = queue.popleft()

            for child in graph[node]:
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)

                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        result = []
        for x in range(len(quiet)):
            _min = quiet[x]
            val = x
            for y in ancestors[x]:
                if quiet[y] < _min:
                    _min = quiet[y]
                    val = y
            result.append(val)
        
        return result