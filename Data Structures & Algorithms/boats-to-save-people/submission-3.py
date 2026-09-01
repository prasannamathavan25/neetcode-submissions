class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        
        left = 0 
        right = len(people)-1 
        count = 0 
        while left <= right:
            cur = people[right] + people[left]

            if cur <= limit : 
                count = count + 1 
                right = right -1 
                left = left + 1 
            else:
                count = count + 1 
                right = right -1 

        return count
        