class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        result = [0] * N
        stack = [] # [temperature, index]
        for i,v in enumerate(temperatures):
            while len(stack) > 0 and v > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            else:
                stack.append([v, i])
        return result
            

        