from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        book = Counter(nums)
        ans = book.most_common(1)
        ans = ans[0][0]
        return ans
            

            