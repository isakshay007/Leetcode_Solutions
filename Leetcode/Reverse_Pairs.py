from typing import List

class Solution:
    def merge(self, nums: List[int], low: int, mid: int, high: int) -> None:
        temp = []  
        left, right = low, mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    def countPairs(self, nums: List[int], low: int, mid: int, high: int) -> int:
        count = 0
        right = mid + 1

        for left in range(low, mid + 1):
            while right <= high and nums[left] > 2 * nums[right]:
                right += 1
            count += (right - (mid + 1))

        return count

    def mergeSort(self, nums: List[int], low: int, high: int) -> int:
        if low >= high:
            return 0

        mid = (low + high) // 2
        count = self.mergeSort(nums, low, mid)  # Count in left half
        count += self.mergeSort(nums, mid + 1, high)  # Count in right half
        count += self.countPairs(nums, low, mid, high)  # Count cross pairs
        self.merge(nums, low, mid, high)  # Merge the two halves

        return count

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1, 3, 2, 3, 1]
    print("Number of reverse pairs (Example 1):", solution.reversePairs(nums1))  
    
    nums2 = [2, 4, 3, 5, 1]
    print("Number of reverse pairs (Example 2):", solution.reversePairs(nums2))  
