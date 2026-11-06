class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        preindex_product = 1
        for i in range(0, length):
            result[i] = preindex_product
            preindex_product *= nums[i]

        
        postindex_product = 1
        for i in range(length - 1, -1, -1):
            result[i] *= postindex_product
            postindex_product *= nums[i]

        return result
        