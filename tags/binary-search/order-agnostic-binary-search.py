# https://www.geeksforgeeks.org/order-agnostic-binary-search/

# O(logn) | O(1)
def order_agnostic_search(sorted_array, target):
    start = 0
    end = len(sorted_array) - 1

    # check array is ascending order or descending
    is_ascending = sorted_array[start] < sorted_array[end]

    while start <= end:
        middle = start + (end - start) // 2
        if sorted_array[middle] == target:
            return middle
        
        if is_ascending:
            # if the target is smaller(<) than mid, ignore the right half
            if target < sorted_array[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            # if the target is greater(>) than mid, ignore the right half
            if target > sorted_array[middle]:
                end = middle - 1
            else:
                start = middle + 1

    return -1

array = [40, 10, 5, 2, 1]
target = 10
print(order_agnostic_search(sorted_array=array, target=target)) # 1

array = [1, 2, 5, 10, 40]
target = 10
print(order_agnostic_search(sorted_array=array, target=target)) # 3