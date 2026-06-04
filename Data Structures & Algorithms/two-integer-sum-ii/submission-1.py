class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        book = dict()

        for loop in range(len(numbers)):
            rem = target - numbers[loop]
            if rem in book : 
                return [book[rem] + 1 , loop+ 1]
            book[numbers[loop]]  = loop

        