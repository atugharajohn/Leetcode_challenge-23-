# problem:
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

# solution:
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events,n=sorted(events, key=lambda e:e[1]), len(events)
        events_start_sorted = sorted([(e[0], i) for i,e in enumerate(events)])
        preceding,j = [-1]*n,0
        for start, index in events_start_sorted:            
            while events[j][1]<start:
                j+=1
            preceding[index]=j-1

        dp,res = [0]*n,0
        for j in range(1, k+1):
            max_value=-1
            dp_next=[-1]*n            
            for i in range(n):
                if j==1:
                    max_value=max(max_value, events[i][2])                    
                elif preceding[i]>=0 and dp[preceding[i]]>=0:
                    max_value=max(max_value, dp[preceding[i]]+events[i][2])
                dp_next[i]=max_value                
            dp=dp_next
            res=max(res, max_value)
        
        return res
        