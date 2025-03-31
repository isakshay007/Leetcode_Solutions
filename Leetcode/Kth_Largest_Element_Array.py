from typing import List

class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1

        nums[left], nums[r] = nums[r], nums[left]
        return r

    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        kth = 0
        while True:
            idx = self.partition(nums, left, right)
            if idx == k - 1:
                kth = nums[idx]
                break
            if idx < k - 1:
                left = idx + 1
            else:
                right = idx - 1

        return kth


nums = [12, 3, 5, 7, 4, 19, 26]
k = 1
solution = Solution()
print(solution.findKthLargest(nums,k))
