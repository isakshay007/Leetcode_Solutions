class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i= m-1
        j=n-1
        k=m+n-1

        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        
        while j>=0:
            nums1[k] = nums2[j]
            j-=1
            k-=1



if __name__ == '__main__':
    arr1 = [1,2,3,0,0,0]
    arr2 = [2, 3, 9]
    m = 3
    n = 3
    solution = Solution()
    result = solution.merge(arr1, m, arr2, n)
    print(arr1)
