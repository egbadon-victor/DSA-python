class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        res = ""
        idx = []
        fmp = defaultdict(int)
        w_size = len(t)

        for c in t:
            fmp[c] += 1

        for i in range(len(s)):
            if s[i] in fmp:
                idx.append(i)
        
        if not idx:
            return ""

        def allGood():
            return all(val <= 0 for val in fmp.values())

        if allGood():
            l = idx[0]
            r = idx[w_size-1]
            res = s[l:r+1]

        l = 0

        for r in range(len(idx)):
            char = s[idx[r]]
            fmp[char] -= 1

            while allGood():
                substr = s[idx[l]:idx[r]+1]

                if res == "" or len(substr) < len(res):
                    res = substr
                
                prevchar = s[idx[l]]
                fmp[prevchar] += 1
                l += 1
        
        return res


