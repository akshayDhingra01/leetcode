class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            if not stack or stack[-1][1] >= value:
                stack.append((index,value))
            else:
                while stack and value > stack[-1][1]:
                    res[stack[-1][0]] = index - stack[-1][0]  
                    stack.pop()
                stack.append((index,value))
        return res
