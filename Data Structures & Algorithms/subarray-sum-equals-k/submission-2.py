class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0 
        book = {0:1}
        cur_sum = 0 

        for n in nums : 
            cur_sum = cur_sum + n 
            diff = cur_sum - k 
            ans = ans + book.get(diff,0)

            book[cur_sum] = 1 + book.get(cur_sum,0)
        
        return ans
            

        