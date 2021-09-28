"""Module with merge sort implementation."""


def merge_sort(array: list, comparisons: int = 0) -> (list, int):
    """Sort list in ascneding order using merge sort algorithm."""

    if len(array) < 2:
        return array, 1

    middle_index = len(array) // 2
    left_array, c1 = merge_sort(array[:middle_index], comparisons)
    right_array, c2 = merge_sort(array[middle_index:], comparisons)

    new_array, more_comparisons = merge_two_arrays(
        left_array, right_array, comparisons)
    comparisons += more_comparisons + c1 + c2

    return new_array, comparisons


def merge_two_arrays(left_array: list, right_array: list, comparisons: int) -> (list, int):
    """Merge two arrays."""
    left_length = len(left_array)
    right_length = len(right_array)

    if not left_length or not right_length:
        return left_array or right_array

    merged = []
    left_ind, right_ind = 0, 0

    while (len(merged) < left_length + right_length):
        comparisons += 2

        if left_array[left_ind] < right_array[right_ind]:
            merged.append(left_array[left_ind])
            left_ind += 1
        else:
            merged.append(right_array[right_ind])
            right_ind += 1

        if left_ind == left_length or right_ind == right_length:
            merged.extend(left_array[left_ind:] or right_array[right_ind:])
            break

    return merged, comparisons


if __name__ == '__main__':
    array = [25, 64, 22, 11, 12]
    print(merge_sort(array))
