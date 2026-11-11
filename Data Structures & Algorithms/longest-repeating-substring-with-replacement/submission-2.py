class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        mp = defaultdict(int)
        l = 0
        res = 0
        replacements = k
        max_count = 0

        for r in range(len(s)):
            left = s[l]
            right = s[r]

            mp[right] += 1
            max_count = max(mp[right], max_count)
            window_size = r - l + 1 

            if window_size > max_count + k:
                mp[left] -= 1
                l += 1
            else:
                res = max(res, window_size)
                   
        return res