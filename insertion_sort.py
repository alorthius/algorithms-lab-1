"""Module with indertion sort implementation."""


def insertion_sort(array: list) -> (list, int):
    """Sort the array in ascneding order with insertion sort algorithm."""
    comparisons = 0
    for index in range(1, len(array)):

        current_element = array[index]
        predicessor = index - 1
        comparisons += 1

        while predicessor >= 0 and current_element < array[predicessor]:
            # make space to insert the element
            array[predicessor + 1] = array[predicessor]
            predicessor -= 1
            comparisons += 2

        array[predicessor + 1] = current_element

    return array, comparisons


if __name__ == '__main__':
    array = [25, 64, 22, 11, 12]
    array = [1, 2, 3, 55, 5, 6, 8, 7, 9, 111]
    print(insertion_sort(array))
