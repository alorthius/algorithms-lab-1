"""Module with selection sort implementation."""


def selection_sort(array: list) -> (list, int):
    """Sort the array in ascending order with selecton sort algorithm."""
    comparisons = 0
    ind_1 = 0

    while ind_1 < len(array):
        min_index = ind_1

        ind_2 = ind_1 + 1
        while ind_2 < len(array):
            if array[min_index] > array[ind_2]:
                min_index = ind_2
            comparisons += 1
            ind_2 += 1

        array[ind_1], array[min_index] = array[min_index], array[ind_1]
        ind_1 += 1

    return array, comparisons


if __name__ == '__main__':
    my_array = [25, 64, 22, 11, 12]
    print(selection_sort(my_array))
