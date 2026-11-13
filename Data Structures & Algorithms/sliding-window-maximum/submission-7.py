class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)
        res.append(-h[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(h,(-nums[i], i))

            while h[0][1] < i-k+1:
                heapq.heappop(h)
            
            res.append(-h[0][0])
        
        return res
        