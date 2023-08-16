# problem:
# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

# solution:
class Solution:
    def maximumRequests(self, n: int, req: List[List[int]]) -> int:
        tot = len(req)
        for i in range(tot, 0, -1):
            comb = list(itertools.combinations([j for j in range(tot)], i))
            for c in comb:
                net = [0 for j in range(n)]
                for idx in c:
                    net[req[idx][0]] -= 1
                    net[req[idx][1]] += 1
                if net == [0 for j in range(n)]:
                    return i
        return 0