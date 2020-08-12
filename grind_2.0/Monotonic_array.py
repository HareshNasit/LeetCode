class Solution:
    # Time Complexity O(N), Space Complexity O(1)
    # https://leetcode.com/problems/monotonic-array/
    def isMonotonic(self, A: List[int]) -> bool:
        is_mono_inc = True
        is_mono_dec = True

        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                is_mono_inc = False
            if A[i] < A[i+1]:
                is_mono_dec = False
        return is_mono_dec or is_mono_inc
        # count_increasing = 1
        # count_decreasing = 1
        # for i in range(len(A) - 1):
        #     # print(A[i])
        #     if A[i] <= A[i + 1]:
        #         count_increasing += 1
        #     if A[i] >= A[i + 1]:
        #         count_decreasing += 1
        # if count_decreasing == len(A) or  count_increasing == len(A):
        #     return True
        # return False
        # is_monotonic = True
        # for i in range(len(A) - 1):
        #     if A[i] > A[i+1]:
        #         is_monotonic = False
        #         break
        # if is_monotonic:
        #     return True
        # else:
        #     is_monotonic = True
        #     for i in range(len(A) - 1):
        #         if A[i] < A[i+1]:
        #             is_monotonic = False
        #             break
        #     return is_monotonic
