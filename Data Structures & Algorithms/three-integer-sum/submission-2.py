class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        ans = []
        nums.sort()
        for loop in range(len(nums)):
            target = 0 - nums[loop]
            if loop <len(nums)-1:
                if nums[loop] == nums[loop+1]:
                    pass
            book = dict()
            for loop1 in range(loop+1 , len(nums)):
                rem = target - nums[loop1]
                if rem in book : 
                    val = [nums[loop] , nums[loop1] , rem]
                    val.sort()
                    ans.append(tuple(val))
                book[nums[loop1]] = loop1

        ans = list(set(ans))

        
        return ans
