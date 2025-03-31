
import math

def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(n):
    for i in range(1,n+1):
        print(nCr(n-1,i-1),end=" ")
    print()

if __name__ == "__main__":
    n=5
    pascalTriangle(n)

    
    
