class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        stk = []
        mp = {
        '}': '{',
        ')': '(',
        ']': '[',
        }

        for c in s:
            if c in mp:
                if len(stk) and stk[-1] == mp[c]:
                    stk.pop()
                    continue
                else:
                    return False
            stk.append(c)
         
        return False if len(stk) else True

        