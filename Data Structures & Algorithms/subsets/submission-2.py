import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        for r in range(n+1): 
            for item in itertools.combinations(nums , r):
                result.append(list(item))

        return result 
            
    