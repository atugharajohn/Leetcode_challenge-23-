# problem:
# https://leetcode.com/problems/smallest-number-in-infinite-set/

# solution:
class SmallestInfiniteSet:

    def __init__(self):
        self.positive=[]
        for i in range(1,1001):
            heapq.heappush(self.positive,i)

    def popSmallest(self) -> int:
        if self.positive:
           return heapq.heappop(self.positive)

    def addBack(self, num: int) -> None:
        if num not in self.positive:
           heapq.heappush(self.positive,num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)