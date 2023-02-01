# problem:
# hhttps://leetcode.com/problems/data-stream-as-disjoint-intervals/

# solution:
class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        seen = set()
        for num in self.nums:
            if num in seen: 
                continue

            left = num
            while left - 1 in self.nums:
                left -= 1
                seen.add(left)

            right = num
            while right + 1 in self.nums:
                right += 1
                seen.add(right)
            
            intervals.append([left, right])
        return sorted(intervals)
