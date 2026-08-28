class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # 1. Build prefix products
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        # 2. Build suffix products
        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
            
        # 3. Combine prefix and suffix
        ans = [prefix[i] * suffix[i] for i in range(n)]
        return ans