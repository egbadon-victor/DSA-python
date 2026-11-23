from collections import defaultdict
class TimeMap:


    def __init__(self):
        self.store = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        store = self.store[key]
        if not store: return ""

        l, r = 0, len(store)-1
        res = ""

        while l<=r:
            m = ((r-l)//2) + l
            curr_timestamp, curr_val = store[m]
            if timestamp == curr_timestamp:
                return store[m][1]
            if curr_timestamp < timestamp:
                res = curr_val
                l = m+1
            else:
                r = m-1
        
        return res
        
