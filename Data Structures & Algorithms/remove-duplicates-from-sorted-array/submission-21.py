class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ori_len= len(nums)
        book = list(set(nums))
        book.sort()
        new_len = len(book)
        print(ori_len, new_len)

        for i in range(new_len):
            nums[i] = book[i]
        
        for _ in range(ori_len - new_len):
            nums.pop()
        return new_len
        

        

    

        
        

            



        

        