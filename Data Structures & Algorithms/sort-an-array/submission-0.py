class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def combine(a,b):
            i = 0 
            j = 0 
            ans = []
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    ans.append(a[i])
                    i = i + 1 
                else: 
                    ans.append(b[j])
                    j = j + 1 
            
            while i < len(a):
                ans.append(a[i])
                i = i + 1 
            while j < len(b):
                ans.append(b[j])
                j = j + 1 

            return ans 

        
        if len(nums)<=1 :
            return nums
        
        mid = len(nums) // 2 

        arr_left = nums[:mid]
        arr_right = nums[mid:]

        sort_left = self.sortArray(arr_left)
        sort_right = self.sortArray(arr_right)

        return combine(sort_left , sort_right)

        


        
        
        