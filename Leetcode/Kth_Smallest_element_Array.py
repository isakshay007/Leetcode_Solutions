from typing import List

class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]  # Choose the leftmost element as the pivot
        l, r = left + 1, right
        while l <= r:
            if nums[l] > pivot and nums[r] < pivot:
                nums[l], nums[r] = nums[r], nums[l]  # Swap elements
                l += 1
                r -= 1
            if nums[l] <= pivot:
                l += 1  # Move l to the right
            if nums[r] >= pivot:
                r -= 1  # Move r to the left
        nums[left], nums[r] = nums[r], nums[left]  # Place the pivot in its correct position
        return r

    def findKthSmallest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while True:
            idx = self.partition(nums, left, right)
            if idx == k - 1:
                return nums[idx]  # Found the k-th smallest element
            elif idx < k - 1:
                left = idx + 1  # Search in the right subarray
            else:
                right = idx - 1  # Search in the left subarray


if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [7, 10, 4, 3, 20, 15]
    k1 = 3
    print(solution.findKthSmallest(nums1, k1))  # Output: 7
    
    nums2 = [2, 3, 1, 20, 15]
    k2 = 4
    print(solution.findKthSmallest(nums2, k2))  # Output: 15