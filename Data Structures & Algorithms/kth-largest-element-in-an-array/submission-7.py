import heapq as hp

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        hp.heapify(nums)
        for _ in range(k-1):
            hp.heappop(nums)
        ans = hp.heappop(nums)
        return -ans


        
        