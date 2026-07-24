class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_t , stack_i = stack.pop()
                res[stack_i] = (i - stack_i)
            stack.append([temp , i])
        return res

















        