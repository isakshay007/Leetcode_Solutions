import heapq
class Solution:
    def maxSumCombination(self,A,B,C):
        A.sort(reverse = True)
        B.sort(reverse= True)

        heap = [(-(A[0]+B[0]),0,0)]

        result=[]

        visited = set((0,0))

        while heap and len(result)<C:

            current_sum,i,j = heapq.heappop(heap)
            result.append(-current_sum)

            if i+1<len(A) and (i+1,j) not in visited:
                heapq.heappush(heap,(-(A[i+1]+B[j]),i+1,j))
                visited.add((i+1,j))


            if j+1<len(B) and (i,j+1) is not visited:
                heapq.heappush(heap,(-(A[i]+B[j+1]),i,j+1))
                visited.add((i,j+1))
        return result
    

A = [3, 2]
B = [1, 4]
C = 2
sol = Solution()
print(sol.maxSumCombination(A,B,C))
