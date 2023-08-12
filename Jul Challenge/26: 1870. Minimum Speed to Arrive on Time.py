# problem:
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

# solution:
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right = 1, 10000000
        while left + 1 < right:
            mid = (left + right) // 2
            curr_hour = self.checkTime(dist, mid)
            if curr_hour <= hour:
                right = mid
            else:
                left = mid
        
        if self.checkTime(dist, left) <= hour:
            return left
        elif self.checkTime(dist, right) <= hour:
            return right
        else:
            return -1
    
    def checkTime(self, distance, speed: int) -> float:
        curr_hour = 0.0
        for dist in distance[:-1]: # exclude last element, since the arrival time doesn't need to be integer
            curr_hour += ceil(dist / speed) # get ceiling integer of a float
        curr_hour += distance[-1] / speed # calculate the last distance's travel time
        return curr_hour