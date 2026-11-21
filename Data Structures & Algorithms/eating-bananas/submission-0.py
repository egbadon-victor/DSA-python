class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateTime(k):
            time = 0
            for p in piles:
                time += math.ceil(p/k)
            return time

        t = max(piles)
        b = 1
        res = math.inf

        while b <=  t:
            m = ((t-b) // 2) + b
            time = calculateTime(m)

            if time > h:
                b = m+1
            else:
                res = min(res, m)
                t = m - 1
        return res

