# problem:
# https://leetcode.com/problems/gas-station/

# solution:
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost): return -1
        ind =tank = 0
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            if tank<0:
                tank=0
                ind = i+1

        #referred from: https://leetcode.com/problems/gas-station/solutions/3011271/python-3-2-6-lines-w-explanation-and-example-t-m-99-98/

        return ind
        