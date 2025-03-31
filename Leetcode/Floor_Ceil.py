def floor(arr,n,x):
    low = 0
    high = n-1
    ans=-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]<=x:
            ans = arr[mid]
            low = mid+1
        else:
            high = mid-1
    return ans



def ceil(arr,n,x):
    low = 0
    high = n-1
    ans=-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]>x:
            ans = arr[mid]
            high = mid-1
        else:
            low = mid+1
    return ans

    

def find(arr,n,x):
    f= floor(arr,n,x)
    c= ceil(arr,n,x)
    return (f,c)



arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = find(arr, n, x)
print(ans)