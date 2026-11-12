class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        w_size = len(s1)
        f_map = defaultdict(int)
        s1_count = w_size
        l = 0

        for s in s1:
            f_map[s] += 1

        for i in range(w_size):
            f_map[s2[i]] -= 1

        def is_match():
                return all(val == 0 for val in f_map.values())
            
        if is_match():
            return True

        for r in range(w_size, len(s2)):

            f_map[s2[r]] -= 1
            f_map[s2[r - w_size]] += 1
            
            if is_match():
                return True

        return False




        

        

        