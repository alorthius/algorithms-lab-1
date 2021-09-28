"""Module with selection sort implementation."""


def selection_sort(array: list) -> (list, int):
    """Sort the array in ascending order with selecton sort algorithm."""
    comparisons = 0
    
    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            # print(i, j, min_index, array[j])
            if array[min_index] > array[j]:
                min_index = j
            comparisons += 1

        array[i], array[min_index] = array[min_index], array[i]

    return array, comparisons


if __name__ == '__main__':
    array = [25, 64, 22, 11, 12]
    print(selection_sort(array))
