class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count_map = {}
        maxi = 0
        starts = []

        for num in nums:
            if num in count_map:
                count_map[num] + 1
            else:
                count_map[num] = 1
        
        for num in nums:
            if num-1 not in count_map:
                starts.append(num)

        for start in starts:
            acc = count_map[start]
            ele = start

            while ele + 1 in count_map:
                acc += count_map[ele + 1]
                ele += 1
            maxi = max(acc, maxi)
        
        return maxi