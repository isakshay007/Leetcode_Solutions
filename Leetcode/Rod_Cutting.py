import heapq

def rodCutting(price):
    n = len(price)  # Length of the rod
    max_profit = [0] * (n + 1)  # DP array for max profit
    heap = []  # Max-Heap to track the best cuts

    for i in range(1, n + 1):
        max_val = 0
        for j in range(i):
            current_val = price[j] + max_profit[i - (j + 1)]
            if current_val > max_val:
                max_val = current_val
                best_cut = (j + 1, i - (j + 1))  # (cut, remaining length)
        
        max_profit[i] = max_val
        heapq.heappush(heap, (-max_val, best_cut))  # Store negative for max-heap behavior
    
    return -heap[0][0]  # Return max value stored in heap

# Test Cases
price1 = [1, 5, 8, 9, 10, 17, 17, 20]
print(rodCutting(price1))  # Expected Output: 22

price2 = [3, 5, 8, 9, 10, 17, 17, 20]
print(rodCutting(price2))  # Expected Output: 24

price3 = [1, 10, 3, 1, 3, 1, 5, 9]
print(rodCutting(price3))  # Expected Output: 40