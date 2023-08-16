# problem:
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

# solution:
class Solution:
    def average(self, salary: List[int]) -> float:
        mi = salary[0]
        ma = salary[0]
        n=len(salary)
        sm = salary[0]
        for i in salary[1:]:
            sm+=i
            if i<mi: mi=i
            if i>ma: ma=i
        return (sm-mi-ma)/(n-2)