# O(logn) | O(logn)
def recursive_order_agnostic_search(sorted_array, start, end, target):
    if len(sorted_array) == 0:
        return -1

    # checking is array is acending or decending
    is_ascending = sorted_array[start] < sorted_array[end]

    if start <= end:
        middle = start + (end - start) // 2
        if sorted_array[middle] == target:
            return middle
        
        if is_ascending:
            if target < sorted_array[middle]:
                return recursive_order_agnostic_search(sorted_array, start, middle-1, target)
            else:
                return recursive_order_agnostic_search(sorted_array, middle+1, end, target)
        else:
            if target > sorted_array[middle]:
                return recursive_order_agnostic_search(sorted_array, start, middle-1, target)
            else:
                return recursive_order_agnostic_search(sorted_array, middle+1, end, target)
    return -1


array = [40, 10, 5, 2, 1]
target = 10
print(recursive_order_agnostic_search(sorted_array=array, start=0, end=len(array) - 1, target=target)) # 1

array = [1, 2, 5, 10, 40]
target = 10
print(recursive_order_agnostic_search(sorted_array=array, start=0, end=len(array) - 1, target=target)) # 3