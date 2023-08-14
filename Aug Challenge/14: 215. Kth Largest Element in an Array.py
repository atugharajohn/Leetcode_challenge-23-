# problem:
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# solution:
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap=[]
        count=0
        for num in nums:
            heappush(minheap,num)
            count+=1
            if count>k:
                heappop(minheap)
                count-=1
        return minheap[0]