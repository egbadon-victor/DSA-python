class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0, 1

        while i < len(nums) - 1:
            while j < len(nums):
                result = nums[i] + nums[j]
                if result == target: return [i, j]
                j += 1
            i += 1
            j = i+1
        return [] 
