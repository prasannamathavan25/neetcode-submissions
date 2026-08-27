import heapq as hp 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        hp.heapify(nums)
        ans = []

        for _ in range(len(nums)):
            item = hp.heappop(nums)
            ans.append(item)
        
        return ans


        
        


        
        
        