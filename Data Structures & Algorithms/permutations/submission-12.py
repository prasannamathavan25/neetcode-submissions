import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =  list(itertools.permutations(nums))
        res = [list(p) for p in res]
        return res