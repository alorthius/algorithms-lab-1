"""Module to test the algorithms."""

import random
import time
import json

# import modules with algorithms implementations
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shellsort import shellsort


def generate_random_array(length: int, ascend=False, descend=False, subset: list = None) -> list:
    """Return randomly generated list with possible options."""
    if subset is None:
        subset = [num for num in range(- (length // 2), length // 2 + 1)]

    generated_list = [random.choice(subset) for _ in range(length)]

    if ascend:
        return sorted(generated_list)
    elif descend:
        return sorted(generated_list, reverse=True)
    return generated_list


def test_one_task(task: str, algorithms: list, repetitiions=5, ascend=False, descend=False, subset: list = None) -> dict:
    """Test all the algorithms and save the results into json files."""
    results_dict = {algorithm.__name__: {} for algorithm in algorithms}

    for length_pow in range(7, 16):
        array_size = 2 ** length_pow

        for algorithm in algorithms:
            average_time = 0
            average_comparisons = 0

            for _ in range(1, repetitiions + 1):
                array = generate_random_array(
                    array_size, ascend=ascend, descend=descend, subset=subset)

                # compute time taken and comparisons number
                start = time.time()
                _, comparisons = algorithm(array)
                end = time.time()

                average_time += end - start
                average_comparisons += comparisons

            # find average time taken and comparisons number
            average_time = average_time / repetitiions
            average_comparisons = average_comparisons / repetitiions

            results_dict[algorithm.__name__][length_pow] = [
                average_time, average_comparisons]

    # save the results
    with open(f'{task}.json', 'w') as json_file:
        json.dump(results_dict, json_file)

    return results_dict


if __name__ == '__main__':
    algorithms_list = [selection_sort, insertion_sort, merge_sort, shellsort]

    test_one_task('task_1', algorithms_list)
    test_one_task('task_2', algorithms_list, repetitiions=1, ascend=True)
    test_one_task('task_3', algorithms_list, repetitiions=1, descend=True)
    test_one_task('task_4', algorithms_list, repetitiions=3, subset=[1, 2, 3])
