# problem:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# solution:
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dic={}
        def fun(i,j):
            if (i,j) in dic:
                return dic[i,j]
            if i>len(prices)-1:
                return 0
            if j==0:
                dic[i,j]=max(fun(i+1,1)-prices[i]-fee,fun(i+1,0))
                return dic[i,j]
            if j==1:
                dic[i,j]=max(fun(i+1,0)+prices[i],fun(i+1,1))
                return dic[i,j]
        return fun(0,0)
            