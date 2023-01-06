# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    core.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/03 16:22:38 by kkim              #+#    #+#              #
#    Updated: 2023/01/06 14:19:12 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ------------------------------------------------------------------------------
# import : DSLR
from DSLR.math import ft_count, ft_mean, ft_std, ft_min, ft_max, ft_percentile
from DSLR.colors import colors as c

# ------------------------------------------------------------------------------
# import : library
import csv
import numpy
import matplotlib.pyplot as plt

import pandas

# ------------------------------------------------------------------------------
# util

def ft_read_csv(_file_name):
    dataset = list()
    with open(_file_name) as csv_file:
        reader = csv.reader(csv_file)
        try:
            for line in reader:
                row = list()
                for value in line:
                    try:
                        value = float(value)
                    except:
                        if not value: #
                            value = numpy.nan
                    row.append(value)
                dataset.append(row)
        except csv.Error as exp:
            print("error occured")
    return numpy.array(dataset, dtype=object)

# ------------------------------------------------------------------------------
# describe

def ft_check_house(_x, _house):
    if _x[1] == _house:
        return True
    return False

def ft_describe_print(index, dataset, title):
    title = c.UNDERLINE + title
    print(f"\n{c.BLUE}┌─────────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐{c.RESET}")
    print(f'{c.BLUE}│{c.RESET}{c.BOLD}{title:>25}{c.RESET}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.GREEN }{"Count":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.GREEN }{"Mean":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.GREEN }{"Std":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.YELLOW}{"Min":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.PURPLE}{"25%":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.PURPLE}{"50%":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.PURPLE}{"75%":>12}',
          f'{c.RESET}{c.BLUE}│{c.RESET}{c.BOLD}{c.YELLOW}{"Max":>12} {c.BLUE}│')
    print(f"{c.BLUE}├─────────────────┼─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┴─────────────┤{c.RESET}")

    for i in range(0, len(index)):
        print(f'{c.BLUE}│{c.RESET} {c.BOLD}{index[i]:15.15}{c.RESET}{c.BLUE}', end=' │')
        try:
            data = numpy.array(dataset[:, i], dtype=float)
            data = data[~numpy.isnan(data)]
            if not data.any():
                raise Exception()
            print(f"{c.RESET}{ft_count(data):>12.4f}", end='  ')
            print(f"{ft_mean(data):>12.4f}", end='  ')
            print(f"{ft_min(data):>12.4f}", end='  ')
            print(f"{ft_max(data):>12.4f}", end='  ')
            print(f"{ft_percentile(data, 25):>12.4f}", end='  ')
            print(f"{ft_percentile(data, 50):>12.4f}", end='  ')
            print(f"{ft_percentile(data, 75):>12.4f}", end='  ')
            print(f"{ft_max(data):>12.4f}{c.BLUE}", end=' │\n')
        except:
            print(f"{c.RESET}{ft_count(dataset[:, i]):>12}", end='  ')
            print(f'{"No numerical value to display":>60}                                     {c.BLUE}│')
    print(f"{c.BLUE}└─────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────┘{c.RESET}\n")

def ft_describe(_file_name):
    dataset = ft_read_csv(_file_name)
    index   = dataset[0]
    dataset = dataset[1:, :]

    dataset_gry = numpy.array([x for x in dataset if ft_check_house(x, 'Gryffindor')])
    dataset_huf = numpy.array([x for x in dataset if ft_check_house(x, 'Hufflepuff')])
    dataset_rav = numpy.array([x for x in dataset if ft_check_house(x, 'Ravenclaw')])
    dataset_sly = numpy.array([x for x in dataset if ft_check_house(x, 'Slytherin')])

    ft_describe_print(index, dataset,     c.PURPLE + "Total")
    ft_describe_print(index, dataset_gry, c.RED    + "Gryffindor")
    ft_describe_print(index, dataset_huf, c.YELLOW + "Hufflepuff")
    ft_describe_print(index, dataset_rav, c.CYAN   + "Ravenclaw")
    ft_describe_print(index, dataset_sly, c.GREEN  + "Slytherin")

# ------------------------------------------------------------------------------
# histogram

def ft_histogram(_file_name, _index):
    # data reading
    dataset = ft_read_csv(_file_name)
    data    = dataset[1:, :]
    data    = data[data[:, 1].argsort()]

    if _index.isnumeric() == True:
        index = int(_index)
    else:
        index = numpy.where(dataset[0] == _index)[0][0]

    # parameter setting
    x       = numpy.array(data[:, index], dtype=float)
    legend  = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    title   = dataset[0, index]
    x_label = "Marks"
    y_label = "Number of student"
    alpha   = 0.3

    # drawing
    h1 = x[:327]
    h1 = h1[~numpy.isnan(h1)]
    plt.hist(h1, color='red', alpha=alpha)

    h2 = x[327:856]
    h2 = h2[~numpy.isnan(h2)]
    plt.hist(h2, color='orange', alpha=alpha)

    h3 = x[856:1299]
    h3 = h3[~numpy.isnan(h3)]
    plt.hist(h3, color='blue', alpha=alpha)

    h4 = x[1299:]
    h4 = h4[~numpy.isnan(h4)]
    plt.hist(h4, color='green', alpha=alpha)

    plt.legend(legend, loc='upper right', frameon=False)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# ------------------------------------------------------------------------------
# scatter plot

def ft_scatter_plot(_file_name, _index_x, _index_y):
    # data reading
    dataset = ft_read_csv(_file_name)
    data    = dataset[1:, :]
    data    = data[data[:, 1].argsort()]

    # parameter setting
    x       = numpy.array(data[:, _index_x], dtype=float)
    y       = numpy.array(data[:, _index_y], dtype=float)
    legend  = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    x_label = dataset[0, _index_x]
    y_label = dataset[0, _index_y]
    title   = "x=" + x_label + ', y=' + y_label

    alpha   = 0.5
    size    = 8
    # flg, axes = plt.subplot(2)
    # axes[0, 0].plot()

    # drawing
    plt.scatter(x[:327],    y[:327],    s=size, color='red', alpha=alpha)
    plt.scatter(x[327:856], y[327:856], s=size, color='orange', alpha=alpha)
    plt.scatter(x[856:1299],y[856:1299],s=size, color='blue', alpha=alpha)
    plt.scatter(x[1299:],   y[1299:],   s=size, color='green', alpha=alpha)

    plt.legend(legend, loc='lower right', frameon=False)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.show()

# ------------------------------------------------------------------------------
# pair plot

def ft_ax_histogram_plot(_ax, _dataset, _index):

    # data reading
    data    = _dataset[1:, :]
    data    = data[data[:, 1].argsort()]

    # parameter setting
    x       = numpy.array(data[:, _index], dtype=float)
    x_label = _dataset[0, _index]
    y_label = "Number of student"
    #title   = dataset[0, _index]

    alpha   = 0.3

    # drawing
    _ax.hist(x[:327],    color='red', alpha=alpha)
    _ax.hist(x[327:856], color='orange', alpha=alpha)
    _ax.hist(x[856:1299],color='blue', alpha=alpha)
    _ax.hist(x[1299:],   color='green', alpha=alpha)


    #_ax.legend(legend, loc='lower right', frameon=False)
    _ax.set_title("histgoram of " + x_label)
    #_ax.set_xlabel(x_label)
    #_ax.set_ylabel(y_label)

def ft_ax_scatter_plot(_ax, _dataset, _index_x, _index_y):

    # data reading
    data    = _dataset[1:, :]
    data    = data[data[:, 1].argsort()]

    # parameter setting
    x       = numpy.array(data[:, _index_x], dtype=float)
    y       = numpy.array(data[:, _index_y], dtype=float)
    #legend  = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    x_label = _dataset[0, _index_x]
    y_label = _dataset[0, _index_y]
    title   = "x=" + x_label + ', y=' + y_label

    alpha   = 0.5
    size    = 8
    # flg, axes = plt.subplot(2)
    # axes[0, 0].plot()

    # drawing
    _ax.scatter(x[:327],    y[:327],    s=size, color='red', alpha=alpha)
    _ax.scatter(x[327:856], y[327:856], s=size, color='orange', alpha=alpha)
    _ax.scatter(x[856:1299],y[856:1299],s=size, color='blue', alpha=alpha)
    _ax.scatter(x[1299:],   y[1299:],   s=size, color='green', alpha=alpha)

    #_ax.legend(legend, loc='lower right', frameon=False)
    _ax.set_title(title)
    #_ax.set_xlabel(x_label)
    #_ax.set_ylabel(y_label)

def ft_pair_plot(_file_name, _indices):

    dataset = ft_read_csv(_file_name)
    data    = dataset[1:, :]
    data    = data[data[:, 1].argsort()]

    # parameter setting
    legend  = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    # drawing
    x, y = [len(_indices), len(_indices)]
    _, axes = plt.subplots(x, y, figsize=(13/3*len(_indices), 13/3*len(_indices)))

    for i in range(0,x):
        idx = _indices[i]
        for j in range(0,y):
            jdx = _indices[j]
            ax=axes[i, j]
            if i == j:
                ft_ax_histogram_plot(ax, dataset, idx)
            else:
                ft_ax_scatter_plot(ax, dataset, idx, jdx)

    plt.legend(legend, loc='lower right', frameon=True)
    plt.show()
