class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lp = 0 
        rp = len(nums) - 1 

        while lp <= rp :
            if nums[lp] != val:
                lp = lp + 1
                continue
            if nums[rp] == val:
                rp = rp - 1
                continue
            nums[lp] = nums[rp]
            rp = rp -1
            lp = lp + 1
        
        return rp + 1

            
            
            


