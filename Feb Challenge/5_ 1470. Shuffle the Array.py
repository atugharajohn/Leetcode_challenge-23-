# problem:
# https://leetcode.com/problems/shuffle-the-array/description/

# solution:
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        for i,j in zip(nums[:n],nums[n:]):
            l.extend([i,j])
        return l