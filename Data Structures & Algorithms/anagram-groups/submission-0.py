class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        result = []

        for s in strs:
            sortedstr = ''.join(sorted(s))
            if sortedstr in map:
                map[sortedstr].append(s)
            else:
                map[sortedstr] = [s]

        for v in map.values():
            result.append(v)
    
        return result