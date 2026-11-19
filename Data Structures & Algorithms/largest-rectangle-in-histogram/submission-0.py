class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_stack = []
        max_area = 0
        n = len(heights)

        for i,h in enumerate(heights):
            while max_stack and h < heights[max_stack[-1]]:
                ind = max_stack.pop()
                width = i - max_stack[-1] - 1 if max_stack else i
                max_area = max(max_area, width * heights[ind])
            
            max_stack.append(i)
        

        while max_stack:
            ind = max_stack.pop()
            width = n - max_stack[-1] - 1 if max_stack else n
            max_area = max(max_area, width * heights[ind])

        return max_area

