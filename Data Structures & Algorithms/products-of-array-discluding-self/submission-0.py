class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        result = []

        for n in nums:
            if n == 0:
                zero_count += 1
                continue
            product *= n
            

        for n in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                result.append(0) if n != 0 else result.append(product)
            else:
                result.append(int(product/n))

        return result
        