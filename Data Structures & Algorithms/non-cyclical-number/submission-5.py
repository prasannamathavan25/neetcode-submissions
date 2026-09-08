class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        def get_value(nums):
            sums = 0
            curr = nums
            while curr != 0 : 
                rem = curr % 10 
                sums += rem**2
                curr = curr // 10
            return sums
        while (count< 1001):
            a = get_value(n)
            n = a
            if (n == 1): return True
            count+=1
        return False