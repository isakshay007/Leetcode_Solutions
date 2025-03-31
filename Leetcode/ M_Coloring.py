class Solution:
    def isSafe(self, node, color, graph, N, col):
        for k in range(N):
            if k != node and graph[k][node] == 1 and color[k] == col:
                return False
        return True  

    def solve(self, node, color, m, N, graph):
        if node == N:  
            return True
        
        for i in range(1, m + 1):
            if self.isSafe(node, color, graph, N, i):
                color[node] = i  
                
                if self.solve(node + 1, color, m, N, graph):  
                    return True

                color[node] = 0
        return False 

    def graphColoring(self, graph, m, N):
        color = [0] * N
        return self.solve(0, color, m, N, graph)


if __name__ == '__main__':
    N = 4  
    m = 3 
    obj = Solution()

    graph = [[0] * N for _ in range(N)]

    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1  

    print(1 if obj.graphColoring(graph, m, N) else 0)
