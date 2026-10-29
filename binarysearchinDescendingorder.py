
def binary_search_descending(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


scores = [90, 75, 60, 45, 30]
target = 60
print(binary_search_descending(scores, target))
