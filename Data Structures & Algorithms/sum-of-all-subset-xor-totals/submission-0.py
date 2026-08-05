class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, total):
            if i == len(nums):
                return total
            ans1 = dfs(i+1 , total ^ nums[i])
            ans2 = dfs(i + 1 , total)
            return ans1 + ans2

        return dfs(0,0)
        