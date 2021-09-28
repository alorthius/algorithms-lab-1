"""Module to build the graphics for representing sorting results."""

import json
from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages


def draw_graphics(task: str) -> pyplot.figure:
    """Create a graphic for one task and return it as a figure object."""

    # read results data
    with open(f'{task}.json') as json_file:
        task_dict = json.load(json_file)

    # add subplots for 2 graphics
    fig, (time, comparisons) = pyplot.subplots(2, figsize=(10, 10))
    fig.suptitle(f'Time and comparisons comparison for {task}')
    time.set_title('Time comparison')
    comparisons.set_title('Comparisons comparison')

    line_style = ['b--', 'm:', 'g--', 'c:']
    num = 0

    for subplot in (time, comparisons):
        # set logariphmic scaling for both x and y axis
        subplot.set_yscale('log', base=10)
        subplot.set_xscale('log', base=2)

    for algo, algo_dict in task_dict.items():
        time_points = [0]
        comparisons_points = [0]

        sizes_list = list(algo_dict.keys())
        sizes_list.insert(0, '0')

        for time_res, comparisons_res in algo_dict.values():
            time_points.append(time_res)
            comparisons_points.append(comparisons_res)

        # draw lines for both time and comparisons praphics
        time.plot(sizes_list, time_points,
                  line_style[num], label=algo, lw=1, marker='.')
        comparisons.plot(sizes_list, comparisons_points,
                         line_style[num], label=algo, lw=1, marker='.')
        num += 1

    for subplot in (time, comparisons):
        # display the algorithms names and their line types
        subplot.legend(loc='upper left')

    return fig


if __name__ == '__main__':
    # driver to visualize all tasks and save them into one single pdf file
    pdf_file = PdfPages('results.pdf')

    for task_num in range(1, 5):
        task_fig = draw_graphics(f'task_{task_num}')
        pdf_file.savefig(task_fig)

    pdf_file.close()
