# problem:
# https://leetcode.com/problems/jump-game-iv/

# solution:
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        indices = defaultdict(list)
        for i in range(n):
            indices[arr[i]].append(i)
        
        storeIndex = deque()
        visited = [False] * n
        storeIndex.append(0)
        visited[0] = True
        steps = 0
        
        while storeIndex:
            size = len(storeIndex)
            while size > 0:
                currIndex = storeIndex.popleft()
                size -= 1
                if currIndex == n - 1:
                    return steps
                
                jumpNextIndices = indices[arr[currIndex]]
                jumpNextIndices.append(currIndex - 1)
                jumpNextIndices.append(currIndex + 1)
                for jumpNextIndex in jumpNextIndices:
                    if 0 <= jumpNextIndex < n and not visited[jumpNextIndex]:
                        storeIndex.append(jumpNextIndex)
                        visited[jumpNextIndex] = True
                jumpNextIndices.clear()
            steps += 1
        return -1