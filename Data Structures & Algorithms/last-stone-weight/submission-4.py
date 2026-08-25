import heapq as heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heap.heapify(stones)

        while len(stones)>1:
            first = -heap.heappop(stones)
            second = -heap.heappop(stones)
            diff = first - second
            if diff > 0 :
                heap.heappush(stones,-diff)
        
        leng = len(stones)
        if leng >0:
            return -stones[0]
        else:
            return 0 
            

        