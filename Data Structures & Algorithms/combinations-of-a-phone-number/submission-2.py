import itertools

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # 1. Gather the letter sets for each digit, e.g., ["abc", "def"] for "23"
        groups = [mapping[d] for d in digits]

        # 2. Unpack groups into itertools.product to get all combinations
        return ["".join(combo) for combo in itertools.product(*groups)]