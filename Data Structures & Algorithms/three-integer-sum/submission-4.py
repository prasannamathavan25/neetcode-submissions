class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        ans = []
        nums.sort()

        for i,x in enumerate(nums):
            if i > 0 and x == nums[i-1]:
                continue

            l = i + 1
            r = len(nums)-1 
            while l < r : 
                sums = x + nums[l] + nums[r]

                if sums > 0 : 
                    r = r-1 
                elif sums < 0 : 
                    l = l + 1 
                else: 
                    ans.append([x,nums[l],nums[r]])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1
            
        return ans

            
