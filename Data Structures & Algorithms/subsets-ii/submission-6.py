import itertools

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()  # FIX: put equal values together and canonicalize order

        for i in range(len(nums) + 1):
            combos = [
                tuple(combo)
                for combo in itertools.combinations(nums, i)
            ]

            combos = list(set(combos))

            res.extend([list(combo) for combo in combos])

        return res