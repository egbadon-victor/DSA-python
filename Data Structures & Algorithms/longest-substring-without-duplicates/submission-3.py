class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        l,r = 0,1 
        seen = {s[0]: True}
        maxSub = 1

        while r < len(s):

            if s[r] not in seen:
                maxSub = max(r-l + 1, maxSub)
                seen[s[r]] = True
                r += 1
            else:
                seen.pop(s[l])
                l += 1
            
        return maxSub
            


        