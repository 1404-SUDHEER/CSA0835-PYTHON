def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
# Test cases
print(find_missing_number([3, 0, 1]))  # Output: 2
print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8