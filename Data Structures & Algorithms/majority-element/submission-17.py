from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        book = Counter(nums)
        ans = book.most_common(1)
        return (ans[0][0])
