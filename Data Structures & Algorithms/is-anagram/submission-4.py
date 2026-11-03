class Solution:
    def toObjectMap(self, str) -> dict:
        result = {}
        for char in str:
            result[char] = result.get(char, 0) + 1

        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_map = self.toObjectMap(s)
        t_map = self.toObjectMap(t)

        if len(s_map) != len(t_map):
            return False
        else:
            for key in s_map:
                if s_map[key] != t_map.get(key):
                    return False
            return True
