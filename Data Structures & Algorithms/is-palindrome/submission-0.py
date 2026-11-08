class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = s.strip()
        i = 0
        j = len(stripped) - 1

        while i < j:
            start = stripped[i].casefold()
            end = stripped[j].casefold()
            if not start.isalnum():
                i += 1
                continue
            if not end.isalnum():
                j -= 1
                continue
            
            if start != end:
                return False
            i += 1
            j -= 1
        
        return True
        
        