def binary_search_with_upper_bound(arr, value):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == value:
            upper_bound = arr[mid]
            left = mid + 1
        elif arr[mid] < value:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None and len(arr) > 0:
        upper_bound = -1  
    return iterations, upper_bound

arr = [0.5, 1.2, 3.4, 5.6, 7.8, 9.0]
value = 4.5
result = binary_search_with_upper_bound(arr, value)
print(f"Ітерацій: {result[0]}, Верхня межа: {result[1]}")