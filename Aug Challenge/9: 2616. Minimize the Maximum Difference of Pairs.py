# problem:
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

# solution:
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def check(mid):
            cnt = 0
            parity = 0
            for i in range(1,len(nums)):
                if parity:
                    parity = 0
                    continue
                if nums[i]- nums[i-1] <= mid:
                    parity = 1
                    cnt+=1
            return cnt >= p
        l = 0 
        h = nums[-1] - nums[0]
        ans = float('inf')
        while l <= h :
            mid = (l+h)//2

            if check(mid):
                ans = mid
                h = mid-1
            else : l = mid + 1
        
        return ans
