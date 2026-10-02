class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            # If stack exists and temp bigger then do res[]
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append([temp, index])
        
        return res

        
        