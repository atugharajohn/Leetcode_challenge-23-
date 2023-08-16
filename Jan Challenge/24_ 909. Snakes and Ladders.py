# problem:
# https://leetcode.com/problems/snakes-and-ladders/

# solution:
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        board.reverse()                                     
        for i in range(1,len(board),2): board[i].reverse()
        arr = [None]+list(chain(*board))                     
        n, queue, seen, ct = len(arr)-1, deque([1]), {1}, 0               

        while queue:                                        
            lenQ = len(queue)

            for _ in range(lenQ):                           
                cur = queue.popleft()
                if cur == n: return ct

                for i in range(cur+1, min(cur+7,n+1)):    
                    nxt = arr[i] if arr[i]+1 else i         
                    if nxt in seen: continue               
                    seen.add(nxt)
                    queue.append(nxt)                       
            ct += 1                    
        
        return -1