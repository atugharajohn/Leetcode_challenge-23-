# problem:
# https://leetcode.com/problems/shortest-path-with-alternating-colors/

# solution:
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in redEdges: graph[a].append((b, "r"))
        for u, v in blueEdges: graph[u].append((v, "b"))
        ans = [-1]*n
        queue = deque([(0, 0, None)])
        visited = set()
        while queue:
            node, dist, prevEdge = queue.popleft()
            visited.add((node, prevEdge))
            if ans[node] == -1:
                ans[node] = dist
            else:
                ans[node] = min(ans[node], dist)
            for neighbour, edge in graph[node]:
                if (neighbour, edge) not in visited and prevEdge != edge:
                    queue.append((neighbour, dist+1, edge))
        return ans