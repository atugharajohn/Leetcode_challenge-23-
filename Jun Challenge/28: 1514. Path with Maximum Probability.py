# problem:
#https://leetcode.com/problems/path-with-maximum-probability/

# solution:
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]

        for i in range(len(edges)):
            u,v = edges[i]
            p = succProb[i]

            adj[u].append((v,p))
            adj[v].append((u,p))

        dis = [0.0] * n
        dis[start] = 1.0

        q = deque([start])

        while q:
            curr = q.popleft()
            for node,p in adj[curr]:
                newProb = dis[curr] * p
                if newProb > dis[node]:
                    dis[node] = newProb
                    q.append(node)

        return dis[end] 