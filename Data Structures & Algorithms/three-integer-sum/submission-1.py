class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        ans = []
        for loop in range(len(nums)):
            target = 0 - nums[loop]
            book = dict()
            for loop1 in range(loop+1 , len(nums)):
                rem = target - nums[loop1]
                if rem in book : 
                    val = [nums[loop] , nums[loop1] , rem]
                    val.sort()
                    ans.append(tuple(val))
                book[nums[loop1]] = loop1
        print(ans)
        ans = list(set(ans))
        print(ans)
        
        return ans
