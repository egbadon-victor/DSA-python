class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        result = []

        for n in nums:
            counts[n] += 1
        
        for number, count in counts.items():
            freq[count].append(number)
        

        for i in range(len(nums), -1, -1):
            if freq[i]:
                for f in freq[i]:
                    if len(result) == k: return result
                    result.append(f)

        return result