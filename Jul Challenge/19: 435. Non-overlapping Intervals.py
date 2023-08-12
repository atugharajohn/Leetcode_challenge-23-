# problem:
# https://leetcode.com/problems/non-overlapping-intervals/

# solution:
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])

        lastInterval = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            #if start time of current interval is less than end time
            #of last interval that we kept, we need to remove currentInterval
            if intervals[i][0] < lastInterval[1]:
                res += 1
            else:
                lastInterval = intervals[i]
        return res
        