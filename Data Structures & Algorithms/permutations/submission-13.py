import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [list(p) for p in itertools.permutations(nums)]
        return res
        