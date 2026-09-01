class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ele in asteroids:
            # Flag to track if the current asteroid is destroyed
            destroyed = False
            
            # A collision only happens if stack top is moving RIGHT (+) 
            # and current element is moving LEFT (-)
            while stack and stack[-1] > 0 and ele < 0:
                if stack[-1] < abs(ele):
                    stack.pop()  # Positive asteroid is destroyed, keep checking stack
                    continue
                elif stack[-1] == abs(ele):
                    stack.pop()  # Both asteroids destroy each other
                    destroyed = True
                    break
                else:
                    destroyed = True  # Positive asteroid is bigger; current one is destroyed
                    break
            
            # If the asteroid wasn't destroyed in a collision, add it to stack
            if not destroyed:
                stack.append(ele)
                
        return stack
