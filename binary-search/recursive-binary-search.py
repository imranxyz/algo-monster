# https://www.geeksforgeeks.org/binary-search/

# O(logn) | O(logn)
def recursive_search(sorted_array, start, end, target):
    # if array is empty
    if len(sorted_array) == 0:
        return -1
    
    # breaking into smaller
    if start <= end:
        mid = start + (end - start) // 2

        if sorted_array[mid] == target:
            return mid 
        
        if target > sorted_array[mid]:
            return recursive_search(sorted_array, mid+1, end, target)
        else:
            return recursive_search(sorted_array, start, mid-1, target)
    else:
        return -1


sorted_array = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
target = 150
print(recursive_search(sorted_array, 0, len(sorted_array)-1, target)) # -1

target = 110
print(recursive_search(sorted_array, 0, len(sorted_array)-1, target)) # 6

sorted_array = [10]
print(recursive_search(sorted_array, 0, len(sorted_array)-1, 10)) # 0


