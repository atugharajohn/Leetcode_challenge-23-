# problem:
# https://leetcode.com/problems/reducing-dishes/

# solution:
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        presum ,res =0,0
        for dish in satisfaction:
            presum += dish
            if presum < 0:
                break
            res += presum
        return res