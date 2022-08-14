# classic binary search
# O(logn) | O(1)
def binary_search(sorted_array, target):
    start_index = 0
    end_index = len(sorted_array) - 1

    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2

        if sorted_array[mid_index] == target:
            return mid_index
        
        # when middle element is greater, ignore right half
        if target < sorted_array[mid_index]:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    
    # when target not in array
    return -1


sorted_array = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
target = 150
print(binary_search(sorted_array, target)) # -1

target = 110
print(binary_search(sorted_array, target)) # 6

print(binary_search([], 15)) # -1