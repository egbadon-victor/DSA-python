from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # Always binary search the smaller array so j = half - i never goes out of bounds
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = (total + 1) // 2

        # l and r represent the COUNT of elements taken from A (0 to len(A) inclusive)
        l, r = 0, len(A)

        while l <= r:
            i = (l + r) // 2  # count from A
            j = half - i      # count from B

            A_left  = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i]     if i < len(A) else float("inf")
            B_left  = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j]     if j < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                # Valid partition found
                if total % 2 == 1:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                r = i - 1  # A_left is too big; take fewer elements from A
            else:
                l = i + 1  # B_left is too big; take more elements from A