def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def find_duplicate(nums):
    if not nums or isinstance(nums, str) or len(nums) < 2 or not all(
            isinstance(num, int) for num in nums):
        return False
    if min(nums) < 1 or max(nums) > len(nums) - 1:
        return False
    sorted_nums = merge_sort(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1]:
            return sorted_nums[i]
    return False
