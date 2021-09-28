"""Module with shellsort implementation."""


def shellsort(array: list) -> (list, int):
    """Sort the array in ascending order with shellsort algorithm."""
    comparisons = 0
    interval = len(array) // 2

    while interval > 0:
        comparisons += 1

        index = interval
        while index < len(array):
            temp_elem = array[index]
            reversive_index = index

            while reversive_index >= interval and array[reversive_index - interval] > temp_elem:
                comparisons += 2
                array[reversive_index] = array[reversive_index - interval]
                reversive_index -= interval

            array[reversive_index] = temp_elem
            index += 1

        interval = interval // 2

    return array, comparisons


if __name__ == '__main__':
    my_array = [25, 64, 22, 11, 12, -10, -100, 0, 32]
    print(shellsort(my_array))
