class Solution:
    def count_of_students(self, arr, max_pages):
        students = 1
        current_pages = 0
        for pages in arr:
            if current_pages + pages > max_pages:
                students += 1
                current_pages = pages
                if current_pages > max_pages:
                    return float('inf')  
            else:
                current_pages += pages
        return students

    def book_allocation(self, arr, n, m):
        if m > n:
            return -1  
        
        low = max(arr)  
        high = sum(arr) 
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            required_students = self.count_of_students(arr, mid)
            
            if required_students <= m:
                result = mid  
                high = mid - 1
            else:
                low = mid + 1  
        
        return result
    
arr = [25, 46, 28, 49, 24]
n = len(arr)  
m = 4  
solution = Solution()
ans = solution.book_allocation(arr, n, m)
print(ans) 
