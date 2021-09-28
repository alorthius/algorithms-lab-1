from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shellsort import shellsort
import random
import logging
import time
import json
from pprint import pprint


def generate_random_array(length: int, ascending=False, descending=False, values_list: list = None) -> list:
    if values_list is None:
        values_list = [num for num in range(- (length // 2), length // 2 + 1)]

    generated_list = [random.choice(values_list) for _ in range(length)]

    if ascending:
        return sorted(generated_list)
    elif descending:
        return sorted(generated_list, reverse=True)
    return generated_list


def test(task: str, algorithms: list, num_repetitions=5, ascending=False, descending=False, values_list: list = None):
    results_dict = {algorithm.__name__: {} for algorithm in algorithms}

    for length_pow in range(7, 16):
        array_size = 2 ** length_pow

        for algorithm in algorithms:
            average_time = 0
            average_comparisons = 0

            for repetition in range(1, num_repetitions + 1):
                array = generate_random_array(array_size, ascending=ascending, descending=descending, values_list=values_list)

                start = time.time()
                new_array, comparisons = algorithm(array)
                end = time.time()

                average_time += end - start
                average_comparisons += comparisons

            average_time = average_time / 5
            average_comparisons = average_comparisons / 5

            results_dict[algorithm.__name__][length_pow] = [
                average_time, average_comparisons]

    pprint(results_dict)
    with open(f'{task}.json', 'w') as json_file:
        json.dump(results_dict, json_file)

    return results_dict


if __name__ == '__main__':
    algorithms = [selection_sort, insertion_sort, merge_sort, shellsort]

    test('task_1', algorithms)
    test('task_2', algorithms, num_repetitions=1, ascending=True)
    test('task_3', algorithms, num_repetitions=1, descending=True)
    test('task_4', algorithms, num_repetitions=3, values_list=[1, 2, 3])
