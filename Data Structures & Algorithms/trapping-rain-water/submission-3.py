class Solution:
    def trap(self, height: List[int]) -> int:

        length  = len(height)
        gti = [0] * length
        lti = [0] * length
        total = 0

        for i in range(0, length):
            ltindex = max(0, i-1)
            gtindex = min(length-1, length - i)

            lti[i] = max(lti[ltindex], height[i])
            gti[length - i -1] = max(gti[gtindex], height[length - 1 - i])

        for i in range(0, length):
            total += min(lti[i],gti[i]) - height[i]

        return total



        