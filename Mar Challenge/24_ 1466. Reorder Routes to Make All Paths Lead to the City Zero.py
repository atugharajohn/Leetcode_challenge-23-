# problem:
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

# solution:
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add((b, True))
            graph[b].add((a, False))
        
        queue = deque([(0, False)])
        ans = 0
        visited = set()
        while queue:
            city, needs_flipped = queue.popleft()
            visited.add(city)
            if needs_flipped:
                ans += 1
            for neighbour in graph[city]:
                if neighbour[0] not in visited:
                    queue.append(neighbour)
        return ans
