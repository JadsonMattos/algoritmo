def merge_sort(string):
    if len(string) <= 1:
        return string
    middle = len(string) // 2
    left = merge_sort(string[:middle])
    right = merge_sort(string[middle:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ('', '', False)
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        return (first_string, second_string, False)
    first_string = first_string.lower()
    second_string = second_string.lower()
    first_string_sorted = ''.join(merge_sort(list(first_string)))
    second_string_sorted = ''.join(merge_sort(list(second_string)))
    return (first_string_sorted, second_string_sorted, first_string_sorted ==
            second_string_sorted)
