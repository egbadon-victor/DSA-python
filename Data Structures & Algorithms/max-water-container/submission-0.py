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
                k = i + 1
                while k < j:
                    if heights[k] > l_height:
                        break
                    k += 1
                i = k
            else:
                k = j - 1
                while k > i:
                    if heights[k] > r_height:
                        break
                    k -= 1
                j = k
        return g_max

        