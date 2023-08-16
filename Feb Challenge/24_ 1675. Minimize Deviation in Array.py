# problem:
# https://leetcode.com/problems/minimize-deviation-in-array/

# solution:
import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        mi=float('inf')
        for i in range(len(nums)):
            
            if nums[i]%2!=0:
                nums[i]=-(nums[i]*2)
                mi=min(mi,-nums[i])
            else:
                nums[i]=-nums[i]
                mi=min(mi,-nums[i])
        res=float('inf')
        heapq.heapify(nums)
        while len(nums)>0:
            top=(-heapq.heappop(nums))
            res=min(res,top-mi)
            if top%2!=0:
                break
            mi=min(mi,top//2)
            heapq.heappush(nums,-(top//2))
        return res