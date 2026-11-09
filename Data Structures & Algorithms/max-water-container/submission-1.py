class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j = 0, len(heights) - 1
        g_max = 0

        while i < j:
            l_height = heights[i]
            r_height = heights[j]
            capacity = (j - i) * min (l_height, r_height)
            g_max = max(g_max, capacity)

            if l_height <= r_height:
                i += 1
            else:
                j -= 1
        return g_max

        