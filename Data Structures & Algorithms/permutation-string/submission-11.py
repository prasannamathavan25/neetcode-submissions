class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):          # FIX: Handle the edge case where s1 is longer than s2
            return False

        book1 = [0]*26 
        book2 = [0]*26

        for i in range(len(s1)):
            ind = ord(s1[i]) - ord('a')
            book1[ind] = book1[ind] + 1 
        
        l , r = 0 , len(s1) - 1

        for i in range(len(s1)):
            ind = ord(s2[i]) - ord('a')
            book2[ind] = book2[ind] + 1 

        while r < len(s2)-1:
            if book1 == book2 : 
                return True 
            left_ind = ord(s2[l]) - ord('a')
            book2[left_ind] -= 1
            l = l + 1 
            r = r + 1 
            right_ind = ord(s2[r]) - ord('a')
            book2[right_ind] +=1 
            
            
        return book1 == book2 



        

            
        
        