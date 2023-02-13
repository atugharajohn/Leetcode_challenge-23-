# problem:
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

# solution:
from typing import List

class Solution:
    def __init__(self):
        self.ans = 0 # to keep track of minimum fuel cost

    # DFS function to traverse the graph and calculate the minimum fuel cost
    def dfs(self, vis: List[int], node: int, seats: int, adj: List[List[int]]):
        vis[node] = 1 # mark node as visited
        count = 1 # initialize count of visited nodes

        # traverse all unvisited neighbors of the node
        for it in adj[node]:
            if not vis[it]:
                count += self.dfs(vis, it, seats, adj)
        
        # calculate the fuel cost required to visit all nodes reached so far
        x = count // seats
        if count % seats: 
            x += 1
        if node != 0: 
            self.ans += x
        
        return count # return the count of visited nodes
    
    # function to return the minimum fuel cost to fly over all cities
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads)
        adj = [[] for _ in range(n+1)] # adjacency list
        vis = [0 for _ in range(n+1)] # visited array
        
        # create adjacency list
        for it in roads:
            adj[it[0]].append(it[1])
            adj[it[1]].append(it[0])
        
        # call the DFS function starting from node 0
        self.dfs(vis, 0, seats, adj)
        
        return self.ans # return the minimum fuel cost