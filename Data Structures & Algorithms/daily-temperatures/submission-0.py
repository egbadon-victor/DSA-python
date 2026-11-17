class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [(temperatures[-1], len(temperatures) - 1)]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-2, -1, -1):
            temp = temperatures[i]

            while stack and temp >= stack[-1][0]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1][1] - i
            else:
                res[i] = 0
            stack.append((temp, i))
        
        return res

        