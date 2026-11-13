from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque()

        for r in range(len(nums)):

            while len(q) and q[0][1] < r-k + 1:
                q.popleft()

            while len(q) and nums[r] > q[-1][0]:
                q.pop()
            q.append((nums[r], r))

            if r + 1  >= k:
                res.append(q[0][0])

        return res
        