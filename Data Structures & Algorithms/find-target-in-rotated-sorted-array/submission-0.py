class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums) -1

        while l < r:
            m = ((r-l)//2) + l

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        if target > nums[len(nums) -1]:
            r = l -1
            l = 0
        else:
            r = len(nums) - 1

        while l <= r:
            m = ((r-l)//2) + l

            if target == nums[m]: return m

            if target > nums[l]:
                l = m+1
            else:
                r = m-1

        return -1

        