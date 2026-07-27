class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mybook = dict()
        ans = [None]
        for i,num in enumerate(nums):
            if num in mybook:
                ans = [mybook[num] , i]
            mybook[num] = i
        
        if ans == [None]:
            return False
        
        mag = abs(ans[0] - ans[1])
        if mag <=k:
            return True
        else:
            return False

        