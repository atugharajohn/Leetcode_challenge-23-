# problem:
# https://leetcode.com/problems/single-number-ii/

# solution:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        for i in nums:
            dic[i]+=1
        for i in dic:
            if dic[i] == 1:
                return i