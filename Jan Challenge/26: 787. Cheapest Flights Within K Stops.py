# problem:
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# solution:
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        
        q = [(src, 0)]
        minCost = [float('inf') for _ in range(n)]
        stops = 0
        
        while q and stops <= k:
            size = len(q)
            for i in range(size):
                currNode, cost = q.pop(0)
                for neighbour, price in adj[currNode]:
                    if price + cost >= minCost[neighbour]:
                        continue
                    minCost[neighbour] = price + cost
                    q.append((neighbour, minCost[neighbour]))
            stops += 1
        
        return -1 if minCost[dst] == float('inf') else minCost[dst]