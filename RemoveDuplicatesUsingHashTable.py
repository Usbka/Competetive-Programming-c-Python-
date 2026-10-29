
def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


nums = [3, 5, 3, 2, 5, 7, 2]
print(remove_duplicates(nums))
