class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        n = len(A)
        if n == 1:
            if A[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        left = 0
        right = n - 1
        lower = -1
        upper = -1
        # Find lower bound
        while left <= right:
            mid = (left + right) / 2
            if mid < n - 1 and A[mid + 1] == target and A[mid] < target:
                lower = mid + 1
                break
            elif A[mid] == target and mid == 0:
                lower = mid
                break
            elif target <= A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Find upper bound
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) / 2
            if mid < n - 1 and A[mid + 1] > target and A[mid] == target:
                upper = mid
                break
            elif A[mid] == target and mid == n - 1:
                upper = mid
                break
            elif target < A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return [lower, upper]
