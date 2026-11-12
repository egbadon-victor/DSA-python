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

        required = len(fmp)
        matched = 0
        
        if not idx:
            return ""

        l = 0

        for r in range(len(idx)):
            char = s[idx[r]]
            fmp[char] -= 1

            if fmp[char] == 0:
                matched += 1

            while matched == required:
                substr = s[idx[l]:idx[r]+1]

                if res == "" or len(substr) < len(res):
                    res = substr
                
                prevchar = s[idx[l]]

                if fmp[prevchar] == 0:
                    matched -= 1
                    
                fmp[prevchar] += 1
                l += 1
        
        return res


