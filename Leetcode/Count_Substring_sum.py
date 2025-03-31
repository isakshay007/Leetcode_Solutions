def count_sub(arr,index,target,):
    if target == 0:
        return 1
    if index<0 or target<0:
        return 0
    
    include = count_sub(arr,index-1,target-arr[index])
    exclude = count_sub(arr,index-1,target)

    return include+exclude

def find_subset_count(arr, target):
    return count_sub(arr, len(arr) - 1, target)

arr = [5, 2, 3, 10, 6, 8]
target = 10
print(find_subset_count(arr, target))