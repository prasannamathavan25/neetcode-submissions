import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # Loop through all possible subset lengths (from 0 to n)
        for r in range(len(nums) + 1):
            # Generate combinations of length r
            for combo in itertools.combinations(nums, r):
                result.append(list(combo))
                
        return result
