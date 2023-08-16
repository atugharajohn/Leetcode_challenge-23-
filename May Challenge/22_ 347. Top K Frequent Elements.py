# problem:
# https://leetcode.com/problems/top-k-frequent-elements/

# solution:
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        N = len(nums)
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1

        for pi in mp.items():
            t = (pi[1], pi[0])
            heappush(heap, t)
            if len(heap) > k:
                heappop(heap)

        ans = []                
        for pi in heap:
            ans.append(pi[1])

        return ans