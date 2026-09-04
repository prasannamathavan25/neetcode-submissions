class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
            window = set()
            lp = 0 

            for rp in range(len(nums)):
                if rp - lp > k : 
                    window.remove(nums[lp])
                    lp = lp + 1
                if nums[rp] in window : 
                    return True 
                window.add(nums[rp])
            return False
                

            
            



            