class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ele in asteroids:
            if not stack:
                stack.append(ele)
                continue
            if ele > 0 :
                stack.append(ele)
                continue
            if stack[-1] > 0 :
                # --- BUG FIXES START HERE ---
                # Loop to destroy smaller positive asteroids
                while stack and stack[-1] > 0 and stack[-1] < abs(ele):
                    stack.pop()
                
                # Check what is left on top of the stack after the loop
                if stack and stack[-1] > 0:
                    if stack[-1] == abs(ele):
                        stack.pop()  # Equal size: both destroy each other
                    # If stack[-1] > abs(ele), current element is destroyed (do nothing)
                    continue
                else:
                    # Stack is empty or top is negative, so current negative element survives
                    stack.append(ele)
                    continue
                # --- BUG FIXES END HERE ---
            else:
                stack.append(ele)
                continue
        return stack
