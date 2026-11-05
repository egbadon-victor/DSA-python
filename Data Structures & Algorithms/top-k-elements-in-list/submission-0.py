class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        sorted_map = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_map[:k]]